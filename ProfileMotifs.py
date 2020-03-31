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

@Gooey(program_name="Count", program_description='Stand Alone Profile Motifs Routine')
def main():


    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Enter DNA or select or type a filename")
        parser.add_argument('input', type=str, nargs='*', help='Motif: DNA without \' \" or , (s) or FileName of a properly formatted data dictionary' , widget="FileChooser")       
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')
        parser.add_argument('input', type=str, nargs='*', help="Motif file or raw" )
    
    
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

    Motifs = eval(Text) 
    print(Profile(Motifs))
    return Profile(Motifs)
#   
# ActualCode from here on https://stepik.org/lesson/23065/step/8?unit=6798
#
def Count(Motifs):
    count = {} # initializing the count dictionary
    
    k = len(Motifs[0])
    t = len(Motifs)
    
    for symbol in "ACGT":
        count[symbol] = []
        for i in range(k):
            count[symbol].append(0)
            
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    
    return count

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Count(Motifs)
   
    
    for symbol in "ACGT":
        for i in range(k):
            profile[symbol][i]=profile[symbol][i]/t            
       
    return profile


if __name__ == '__main__':
    main() 