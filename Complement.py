import sys, argparse
from gooey import Gooey

init_length = len(sys.argv)
if init_length >= 2:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')

@Gooey(program_name="Complement", program_description='Stand Alone Complement Routine')
def main():


    parser = argparse.ArgumentParser(conflict_handler='resolve')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('RAW_input', nargs='?', type=str, help='DNA or FileName' )
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

    file.close()    
    print(Complement(Pattern))
    return Complement(Pattern)
#   
# ActualCode from here on  
def Complement(Pattern):
    complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    seq_list = list(Pattern)
    seq_list = [complement_dict[base] for base in seq_list]
    answer = ''.join(seq_list)
    return answer

if __name__ == '__main__':
    main() 