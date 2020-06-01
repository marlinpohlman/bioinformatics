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

@Gooey(program_name="RandomizedMotifSearch(Dna, k, t)", program_description='RandomizedMotifSearch(Dna, k, t)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="RandomizedMotifSearch(Dna, k, t)")       
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

    print(RandomizedMotifSearch(Dna, k, t))    
    return RandomizedMotifSearch(Dna, k, t)

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

    
def Consensus(Motifs):	
	# t = len(Motifs)
	k = len(Motifs[0])
	profile = ProfileWithPseudocounts(Motifs)
	consensus = [""]*k	
	for i in range(k):
		maximum = -1
		for key in profile:			
			if maximum< profile[key][i]:
				consensus[i] = key
				maximum = profile[key][i]
	return "".join(consensus)

def Score(Motifs):
	# Insert code here	
	score=0
	consensus = Consensus(Motifs)	
	for row in Motifs:
		for c1,r1 in zip(consensus,row):			
			if c1!=r1:
				score+=1
	return score

def Pr(Text,Profile):	
	multi = 1.0
	for i in range(len(Text)):
		multi *= Profile[Text[i]][i]
	return multi


def ProfileMostProbableKmer(text, k, profile):
	kmer = text[0:k]
	maximum = -1
	for i in range(len(text)-k+1):
		pr = Pr(text[i:i+k],profile)
		if(maximum<pr):
			maximum = pr
			kmer = text[i:i+k]
	return kmer

def ProfileWithPseudocounts(Motifs):	
	t = len(Motifs)
	# k = len(Motifs[0])	
	#profile = {}	
	count = CountWithPseudocounts(Motifs)	
	profile={}
	for key in count:
		profile[key]= [x / (4.0+t) for x in count[key]]
	return profile


def CountWithPseudocounts(Motifs):
	t = len(Motifs)
	k = len(Motifs[0])
	# insert your code here
	count = {"A":[1]*k,"C":[1]*k,"G":[1]*k,"T":[1]*k}
	# # your code here	
	for i in range(t):		
		for j in range(k):			
			count[Motifs[i][j]][j]+=1
	return count

def Motifs(Profile, Dna):
	return [ProfileMostProbableKmer(text,len(Profile["A"]),Profile) for text in Dna]

def RandomMotifs(Dna, k, t):
	return [text[random.randint(0,len(text)-k-1):][:k] for text in Dna ]

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