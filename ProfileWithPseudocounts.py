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

@Gooey(program_name="ProfileWithPseudocounts(Motifs)", program_description='ProfileWithPseudocounts(Motifs)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="ex. ['AACGTA','CCCGTT','CACCTT','GGATTA','TTCCGG']")       
        parser.add_argument('input1', nargs='?', help='Motifs') 
        
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')       
        parser.add_argument('input1', nargs='?', help='Motifs')           

    args = parser.parse_args()
    motif = str(args.input1)
    Motifs = eval(motif)
    print(ProfileWithPseudocounts(Motifs))    
    return ProfileWithPseudocounts(Motifs)
    
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    profile = {} # output variable
    dict = CountWithPseudocounts(Motifs)
    # your code here
    for key, value in dict.items():
        profile[key] = []
        for x in value:
            profile[key].append(x/(t+4))     
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
            
if __name__ == '__main__':
    main() 