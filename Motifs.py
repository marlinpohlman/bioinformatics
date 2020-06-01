import sys, argparse
from gooey import Gooey, GooeyParser

CL_Flag = False  
init_length = len(sys.argv)
if init_length >= 2:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')
        CL_Flag = True
else:
    CL_Flag = False 

@Gooey(program_name="Motifs(Profile, Dna)", program_description='Motifs(Profile, Dna)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Motifs(Profile, Dna)")       
        parser.add_argument('input1', nargs='?', help='Dna', widget="FileChooser") 
        parser.add_argument('input2', nargs='?', help='Profile') 
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')       
        parser.add_argument('input1', nargs='?', help='Dna') 
        parser.add_argument('input2', nargs='?', help='Profile')      

    args = parser.parse_args()
    Flag_1 = False
    while Flag_1 == False:
        if args.input2 != None: 
             s1 = args.input2
             if validSequence(s1) == True:
                 Text = str(args.input2[0])
                 Flag_1 = True
             if validFileName(args.input2[0]) == True:
                 filename = str(args.input2[0])                 
                 file = open(filename, "r")
                 Text = file.read()
                 Flag_1 = True
             else:
                 print("input error")
                 Text = "input error"
                 Flag_1 = True
                
                
    Dna = TextCleaner(Text)

    Flag_1 = False
    while Flag_1 == False:
        if args.input1 != None: 
             s1 = args.input1
             if validSequence(s1) == True:
                 Text = str(args.input1[0])
                 Flag_1 = True
             if validFileName(args.input1[0]) == True:
                 filename = str(args.input1[0])                 
                 file = open(filename, "r")
                 Text = file.read()
                 Flag_1 = True
             else:
                 print("input error")
                 Text = "input error"
                 Flag_1 = True
                
                
    Profile = TextCleaner(Text)

    print(Motifs(Profile, Dna))    
    return Motifs(Profile, Dna)
    
# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    motifs = []
    for s in Dna:
        motifs.append(ProfileMostProbablePattern(s, len(Profile['A']), Profile))
    return motifs

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.

def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
    mostProbable = ""
    maxPr = float(-1);
    for i in range(len(Text)-k+1):
        p = Pr(Text[i:i+k],Profile)
        if p > maxPr:
            mostProbable = Text[i:i+k]
            maxPr = p
    return mostProbable

def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def validSequence(s1):
    valid = 'ACTGU'
    for letter in s1:
        if letter not in valid:
            return False
    return True

def validFileName(s1):
    valid = '/.'
    for letter in s1:
        if letter in valid:
            return True
    return False

def TextCleaner(Text):
    Text = Text.replace("{[","[")
    Text = Text.replace("]}","]")
    Text = Text.replace("[\"[\'","[\'")
    Text = Text.replace("\']\"]","\']")
    Text = Text.replace("\',\",","\',")
    Text = Text.replace("\"\'","\'")
    return Text
            
if __name__ == '__main__':
    main() 