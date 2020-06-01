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

@Gooey(program_name="Motifs(Profile, Dna)", program_description='Motifs(Profile, Dna)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Motifs(Profile, Dna)")       
        parser.add_argument('input1', nargs='?', help='Dna', widget="FileChooser") 
        parser.add_argument('input2', nargs='?', help='k') 
        parser.add_argument('input3', nargs='?', help='t')
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')       
        parser.add_argument('input1', nargs='?', help='Dna') 
        parser.add_argument('input2', nargs='?', help='k') 
        parser.add_argument('input3', nargs='?', help='t')

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
                
                
    Dna = TextCleaner(Text)
    k = args.input2
    t = args.input3

    print(RandomMotifs(Dna, k, t))    
    return RandomMotifs(Dna, k, t)

def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
	M = RandomMotifs(Dna, k, t)	
	BestMotifs = M
	while True:
		Profile = ProfileWithPseudocounts(M)		
		M = Motifs(Profile, Dna)		
		if Score(M) < Score(BestMotifs):
			BestMotifs = M
		else:
			return BestMotifs

    
def RandomMotifs(Dna, k, t):
    r_list = []
    for s in Dna:
        index = random.randint(0,len(Dna[0])-k)
        r_list.append(s[index:index+k])
    return r_list

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