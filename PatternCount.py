import sys, argparse
from gooey import Gooey

init_length = len(sys.argv)
if init_length >= 3:
    if not '--ignore-gooey' in sys.argv:
        sys.argv.append('--ignore-gooey')

@Gooey(program_name="Pattern Count", program_description='Stand Alone Pattern Count Routine')
def main():


    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('Pattern', nargs='?', type=str, help="Pattern to Search Text For")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('RAW_input', nargs='?', type=str, help='DNA or FileName' )
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'))

    try:
        args = parser.parse_args()
    except:
        args.infile = None
        args = parser.parse_args()    
            
    Pattern = args.Pattern

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
            Text = str(file)
            Flag = True
        elif (args.RAW_input != None) and (Flag == False):   
            for letter in str(args.RAW_input):
                if letter not in valid_DNA:
                    Text = args.RAW_input
                    Flag = True
            if all(i in valid_DNA for i in str(args.RAW_input)) == True:
                Text = args.RAW_input
                Flag = True
            elif any(i in valid_PathName for i in str(args.RAW_input)) == True:
                filename = str(args.RAW_input)
                file = open(filename,'r')
                Text = str(file.read())
                Flag = True
            elif any(i in valid_FileName for i in str(args.RAW_input)) == True:
                filename = str(args.RAW_input)
                file = open(filename,'r')
                Text = str(file.read())
                Flag = True
        else:
            Flag = True    

#    print("debug1:"," Pattern=", Pattern, " Text=", Text, "PatternCount=", str(PatternCount(Pattern, Text)) )     
    print(PatternCount(Pattern,Text))
    return PatternCount(Pattern,Text)
#   
# ActualCode from here on  
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return str(count)

if __name__ == '__main__':
    main() 