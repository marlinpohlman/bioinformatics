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
        
@Gooey(program_name="Approximate Pattern Matching", program_description='Stand Alone Approximate Pattern Matching Routine')
def main():


    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Enter DNA or select or type a filename")
        parser.add_argument('infile_1', nargs='?', help='Text: DNA or FileName' , widget="FileChooser")
        parser.add_argument('infile_2', nargs='?', help='Pattern: DNA or FileName' , widget="FileChooser")
        parser.add_argument('d', nargs='?', help='Number', type=int)        
        args = parser.parse_args()
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')
        parser.add_argument('infile_1', nargs='?', help="Text" )
        parser.add_argument('infile_2', nargs='?', help="Pattern" )
        parser.add_argument('d', nargs='?', type=int, help="d" )
        args = parser.parse_args()
    
        
#    print("Debug 1"," args.infile_1:",args.infile_1," args.infile_2:", args.infile_2)
    valid_DNA = 'ACTGU'
    d = args.d
    Flag_1 = False
    while Flag_1 == False:
#        if args.infile_1 != None and  args.infile_2 != None:
           for letter in str(args.infile_1):
               if letter not in valid_DNA:
                   infile_lst_1 = args.infile_1
                   filename_1 = str(infile_lst_1)
                   file_1 = open(filename_1, "r")
                   Text = str(file_1.read())
                   Flag_1 = True
               elif all(i in valid_DNA for i in str(args.infile_1)) == True:
                   Text = str(args.infile_1)
                   Flag_1 = True
               else:
                   Text = args.infile_1
                   Flag_1 = True
                   
    Flag_2 = False
    while Flag_2 == False:
#        if args.infile_1 != None and  args.infile_2 != None:
           for letter in str(args.infile_2):
               if letter not in valid_DNA:
                   infile_lst_2 = args.infile_2
                   filename_2 = str(infile_lst_2)
                   file_2 = open(filename_2, "r")
                   Pattern = str(file_2.read())
                   Flag_2 = True
               elif all(i in valid_DNA for i in str(args.infile_2)) == True:
                   Pattern = str(args.infile_2)
                   Flag_2 = True        
               else:
                   Pattern = args.infile_2
                   Flag_2 = True
       
#    print("Debug 2"," q:",q," p:",p," args.infile_1:",args.infile_1," args.infile_2:", args.infile_2)
  
    
    
    print(ApproximatePatternMatching(Text, Pattern, d))
    return ApproximatePatternMatching(Text, Pattern, d)
#   
# ActualCode from here on  
#
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    for i in range(len(Text)- len(Pattern) +1):
        if HammingDistance(Pattern, Text[i:i + len(Pattern)]) <= d:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    return sum(1 for i, j in zip(p,q) if i != j)

if __name__ == '__main__':
    main() 