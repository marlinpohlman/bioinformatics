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

@Gooey(program_name="GreedyMotifSearch(Dna, k, t)", program_description='GreedyMotifSearch(Dna, k, t)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Enter DNA or select or type a filename")
       
        parser.add_argument('input0', type=int, nargs='?', help='t') 
        parser.add_argument('input1', type=int, nargs='?', help='K') 
        parser.add_argument('input2', type=str, nargs='*', help='DNA without \' \" or , (s) or FileName of a properly formatted data dictionary' , widget="FileChooser")       
        
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')       
        parser.add_argument('input0', type=int, nargs='?', help="t" ) 
        parser.add_argument('input1', type=int, nargs='?', help='K')        
        parser.add_argument('input2', type=str, nargs='*', help="DNA file or raw" )
   
    args = parser.parse_args()
    print("Debug:",args.input0," ",args.input1," ",args.input2)
    valid_File = '/.tx'
    Flag_1 = False
    while Flag_1 == False:
        if args.input2 != None: 
             s1 = args.input2
             if validSequence(s1) == True:
                 Text = str(args.input2)
                 Flag_1 = True
             if any(i in valid_File for i in str(args.input2)) == True:
                 filename = str(args.input2)
                 file = open(filename, "r")
                 Text = file.read()
                 Flag_1 = True
                    
    Dna = str(Text)   
    k = int(args.input1)
    t = int(args.input0)
    Dna = "GGCGTTCAGGCA AAGAATCAGTCA CAAGGAGTTCGC CACGTCAATCAC CAATAATATTCG"   
    k = 3
    t = 5
    
    print("Debug:",args.input0," ",args.input1," ",args.input2)
                
    print(GreedyMotifSearch(Dna, k, t))
    return GreedyMotifSearch(Dna, k, t)

#   
# ActualCode from here onhttps://stepik.org/lesson/23066/step/5?unit=6799
#


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def validSequence(s1):
    valid = "ACTGU[]\'/'"
    for letter in s1:
        if letter not in valid:
            return False
    return True

def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Profile(Motifs):
    count = {} # initializing the count dictionary
    profile = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    ## divide the number of motif strings to get frequency
    for letter in count.keys():
        profile[letter] = [x/ float(t) for x in count[letter]]
    return profile

def ProfileMostProbableKmer(Text, k, Profile):
    p_dict = {}
    for i in range(len(Text)- k +1):
        p = Pr(Text[i: i+k], Profile)
        p_dict[i] = p
    m = max(p_dict.values())
    keys = [k for k,v in p_dict.items() if v == m]
    ind = keys[0]
    return Text[ind: ind +k]

def Score(Motifs):
    consensus = Consensus(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    score = 0
    for i in range(k):
        FrequentSymbol = consensus[i]
        for j in range(t):
            if Motifs[j][i] != FrequentSymbol:
                score = score + 1
    return score

def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

if __name__ == '__main__':
    main()