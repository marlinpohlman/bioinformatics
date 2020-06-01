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

@Gooey(program_name="Count", program_description='WeightedDie(Probabilities)')
def main():


    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="WeightedDie(Probabilities)")
        parser.add_argument('input', type=str, nargs='*', help=Normalize(Probabilities)' , widget="FileChooser")       
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')
        parser.add_argument('input', type=str, nargs='*', help="WeightedDie(Probabilities)" )
    
    
    args = parser.parse_args()
    valid_File = '.'
    Flag_1 = False
    while Flag_1 == False:
        if args.input != None:
          if any(i in valid_File for i in str(args.input)) == True:
             filename = str(args.input[0])
             file = open(filename, "r")
             Text = file.read()
             Flag_1 = True
          else:
             Text = str(args.input)
# Clean it up if its alredy in data dictionary format
             Text = Text.replace("{[","[")
             Text = Text.replace("]}","]")
             Text = Text.replace("[\"[\'","[\'")
             Text = Text.replace("\']\"]","\']")
             Text = Text.replace("\',\",","\',")
             Text = Text.replace("\"\'","\'")
             Flag_1 = True

    Probabilities = eval(Text) 
    print(WeightedDie(Probabilities))
    return WeightedDie(Probabilities)
#   
# ActualCode from here on https://stepik.org/lesson/23065/step/6?thread=solutions&unit=6798 
#
# first, import the random package
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers

# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0,1)
    i = 0
    cumProb = {}
    for key in Probabilities:
        if i == 0:
            cumProb[i] = Probabilities[key]
        else:
            cumProb[i] = Probabilities[key] + cumProb[i-1]
        if p < cumProb[i]:
            kmer = key
            return kmer
        i = i + 1

    return kmer

def Normalize(Probabilities):
    # your code here
    count = 0
    for i in Probabilities.keys():
        count = count + Probabilities[i]
    for i in Probabilities.keys():
        Probabilities[i] = Probabilities[i]/count
    return Probabilities        
        
def Pr(Text, Profile):
    # insert your code here
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p




if __name__ == '__main__':
    main() 