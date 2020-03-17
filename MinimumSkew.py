import sys, argparse
from gooey import Gooey

init_length = len(sys.argv)
if init_length >= 2:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')

@Gooey(program_name="Minimum Skew", program_description='Stand Alone Minimum Skew Routine')
def main():


    parser = argparse.ArgumentParser(conflict_handler='resolve')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('RAW_input', nargs='?', type=str, help='Genome or FileName' )
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'))

    try:
        args = parser.parse_args()
    except:
        args.infile = None
        args = parser.parse_args()    

    valid_DNA = 'ACTGU'
    valid_FileName = 'tx.do'
    valid_PathName = 'DC:\/'
    Flag = False
    while Flag == False:
        if (args.infile != None) and (args.RAW_input != None):
            print("two conflicting entries please retry")
            Flag = True
        elif args.infile != None:
            infile_lst = args.infile[0]
            filename = str(infile_lst.name)
            file = open(filename,'r')
            Pattern = str(file)
            Flag = True
        elif (args.RAW_input != None) and (Flag == False):   
            for letter in str(args.RAW_input):
                if letter not in valid_DNA:
                    Pattern = args.RAW_input
                    Flag = True
            if all(i in valid_DNA for i in str(args.RAW_input)) == True:
                Pattern = args.RAW_input
                Flag = True
            elif any(i in valid_PathName for i in str(args.RAW_input)) == True:
                filename = str(args.RAW_input)
                file = open(filename,'r')
                Pattern = str(file.read())
                Flag = True
            elif any(i in valid_FileName for i in str(args.RAW_input)) == True:
                filename = str(args.RAW_input)
                file = open(filename,'r')
                Pattern = str(file.read())
                Flag = True
        else:
            Flag = True

    Genome = Pattern   
    print(MaxSkew(Genome))
    return MaxSkew(Genome)
#   
# ActualCode from here on  
#
def MaxSkew(Genome):
    positions = [] # output variable
    Skew = SkewArray(Genome)
    m = max(Skew)
    #positions = Skew.index(m)
    for s in range(len(Skew)):
        if Skew[s] == m:
            positions.append(s)
    return positions    

def SkewArray(Genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for i in range(1,len(Genome)+1):
            skew.append(score[Genome[i-1]] + skew[i-1])
    return skew

if __name__ == '__main__':
    main() 