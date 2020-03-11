import sys, argparse
from gooey import Gooey

init_length = len(sys.argv)
if init_length >= 3:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')

@Gooey(program_name="Pattern Matching", program_description='Stand Pattern Matching Routine')
def main():


    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('pattern', nargs='?', help="pattern" )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('RAW_input', nargs='?', type=str, help='DNA or FileName' )
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'))

    try:
        args = parser.parse_args()
    except:
        args.infile = None
        args = parser.parse_args()    

    Pattern = str(args.pattern)
    
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
            Genome = str(file)
            Flag = True
        elif (args.RAW_input != None) and (Flag == False):   
            for letter in str(args.RAW_input):
                if letter not in valid_DNA:
                    Genome = args.RAW_input
                    Flag = True
            if all(i in valid_DNA for i in str(args.RAW_input)) == True:
                Genome = args.RAW_input
                Flag = True
            elif any(i in valid_PathName for i in str(args.RAW_input)) == True:
                filename = str(args.RAW_input)
                file = open(filename,'r')
                Genome = str(file.read().splitlines())
                Flag = True
            elif any(i in valid_FileName for i in str(args.RAW_input)) == True:
                filename = str(args.RAW_input)
                file = open(filename,'r')
                Genome = str(file.read().splitlines())
                Flag = True
        else:
            Flag = True

    file.close()
    print(PatternMatching(Pattern, Genome))
    return PatternMatching(Pattern, Genome)
#   
# ActualCode from here on  

def PatternMatching(Pattern, Genome):
    list = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            list.append(i)
    return list     



if __name__ == '__main__':
    main() 