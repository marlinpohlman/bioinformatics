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

@Gooey(program_name="GreedyMotifSearchWithPseudocounts(Dna, k, t)", program_description='GreedyMotifSearchWithPseudocounts(Dna, k, t)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="GreedyMotifSearchWithPseudocounts(Dna, k, t)")       
        parser.add_argument('input1', nargs='?', help='Dna') 
        parser.add_argument('input2', nargs='?', help='k') 
        parser.add_argument('input3', nargs='?', help='t') 
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')       
        parser.add_argument('input1', nargs='?', help='Dna') 
        parser.add_argument('input2', nargs='?', help='k') 
        parser.add_argument('input3', nargs='?', help='t')      

    args = parser.parse_args()
    Dna = args.input1
    k = args.input2
    t = args.input3

    print(GreedyMotifSearchWithPseudocounts(Dna, k, t))    
    return GreedyMotifSearchWithPseudocounts(Dna, k, t)
    
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def ProfileWithPseudocounts(Motifs):
    profile = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    for i in range(k):
        for symbol in "ACGT":
            profile[symbol][i] = profile[symbol][i]/(t+4)
    return profile

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileMostProbablePattern(Text, k, Profile):
    P=[]
    for i in range(len(Text)-k+1):
        P.append(Pr(Text[i:i+k],Profile))
    start_index = P.index(max(P))
    return Text[start_index:start_index+k]

#Text: String
def Pr(Text, Profile):
    p = 1
    i = 0
    for item in Text:
        p = p*Profile[item][i]
        i = i+1
    return p

def Score(Motifs):
    score = 0
    consensus = Consensus(Motifs)
    for i in range(len(consensus)):
        for j in range(len(Motifs)):
            if Motifs[j][i] != consensus[i]:
                score +=1
    return score

def Consensus(Motifs):
    consensus = ""
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
            
if __name__ == '__main__':
    main() 