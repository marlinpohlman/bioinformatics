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
        
@Gooey(program_name="Hamming Distance", program_description='Stand Hamming Distance Routine')
def main():


    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Enter DNA or select or type a filename")
        parser.add_argument('infile_1', nargs='?', help='p: DNA or FileName' , widget="FileChooser")
        parser.add_argument('infile_2', nargs='?', help='q: DNA or FileName' , widget="FileChooser")
        args = parser.parse_args()
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')
        parser.add_argument('infile_1', nargs='?', help="p" )
        parser.add_argument('infile_2', nargs='?', help="q" )
        args = parser.parse_args()
    
        
#    print("Debug 1"," args.infile_1:",args.infile_1," args.infile_2:", args.infile_2)
    valid_DNA = 'ACTGU'

    Flag_1 = False
    while Flag_1 == False:
#        if args.infile_1 != None and  args.infile_2 != None:
           for letter in str(args.infile_1):
               if letter not in valid_DNA:
                   infile_lst_1 = args.infile_1
                   filename_1 = str(infile_lst_1)
                   file_1 = open(filename_1, "r")
                   p = str(file_1.read())
                   Flag_1 = True
               elif all(i in valid_DNA for i in str(args.infile_1)) == True:
                   p = str(args.infile_1)
                   Flag_1 = True
               else:
                   q = args.infile_1
                   Flag_1 = True
                   
    Flag_2 = False
    while Flag_2 == False:
#        if args.infile_1 != None and  args.infile_2 != None:
           for letter in str(args.infile_2):
               if letter not in valid_DNA:
                   infile_lst_2 = args.infile_2
                   filename_2 = str(infile_lst_2)
                   file_2 = open(filename_2, "r")
                   q = str(file_2.read())
                   Flag_2 = True
               elif all(i in valid_DNA for i in str(args.infile_2)) == True:
                   q = str(args.infile_2)
                   Flag_2 = True        
               else:
                   q = args.infile_2
                   Flag_2 = True
       
#    print("Debug 2"," q:",q," p:",p," args.infile_1:",args.infile_1," args.infile_2:", args.infile_2)
  
    print(HammingDistance(p,q))
    return HammingDistance(p,q)
#   
# ActualCode from here on  
#
def HammingDistance(p, q):
    return sum(1 for i, j in zip(p,q) if i != j)

if __name__ == '__main__':
    main() 