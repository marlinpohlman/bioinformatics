import sys, argparse, random
from gooey import Gooey, GooeyParser

CL_Flag = False  
init_length = len(sys.argv)
if init_length >= 2:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')
        CL_Flag = True
else:
    CL_Flag = False 

@Gooey(program_name="ProfileGeneratedString(Text, profile, k)", program_description='ProfileGeneratedString(Text, profile, k)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="ProfileGeneratedString(Text, profile, k)")       
        parser.add_argument('input1', nargs='?', help='Text', widget="FileChooser") 
        parser.add_argument('input2', nargs='?', help='profile') 
        parser.add_argument('input3', nargs='?', help='k')
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')       
        parser.add_argument('input1', nargs='?', help='Text') 
        parser.add_argument('input2', nargs='?', help='profile') 
        parser.add_argument('input3', nargs='?', help='k')

    args = parser.parse_args()
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
                
                
    Text = TextCleaner(Text)
    profile = args.input2
    k = args.input3

    print(ProfileGeneratedString(Text, profile, k))    
    return ProfileGeneratedString(Text, profile, k)


def Normalize(Probabilities):
    sum = 0
    for key in Probabilities:
        sum += Probabilities[key]
    for key in Probabilities:
        Probabilities[key] /= sum
    return Probabilities


def WeightedDie(Probabilities):
    kmer = ''  # output variable
    num = random.uniform(0, 1)
    for i in Probabilities:
        num -= Probabilities[i]
        kmer = i
        if num <= 0:
            return kmer


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n - k + 1):
        probabilities[Text[i:i + k]] = Pr(Text[i:i + k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

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