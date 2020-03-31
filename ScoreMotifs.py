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

@Gooey(program_name="Score(Motifs)", program_description='Stand Alone Score(Motifs) Routine')
def main():


    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Enter DNA or select or type a filename")
        parser.add_argument('input2', type=str, nargs='*', help='Text' , widget="FileChooser") 
        parser.add_argument('input1', type=str, nargs='*', help='Profile: DNA without \' \" or , (s) or FileName of a properly formatted data dictionary' , widget="FileChooser")       
        
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')
        parser.add_argument('input2', type=str, nargs='*', help="Text file or raw" ) 
        parser.add_argument('input1', type=str, nargs='*', help="Profile file or raw" )
   
    args = parser.parse_args()
    valid_File = '.'
    Flag_1 = False
    while Flag_1 == False:
        if args.input1 != None:
          if any(i in valid_File for i in str(args.input1)) == True:
             filename = str(args.input1[0])
             file = open(filename, "r")
             Profile = file.read()
             Flag_1 = True
          else:
             Profile = str(args.input1)
# Clean it up if its alredy in data dictionary format
             Profile = Profile.replace("{[","[")
             Profile = Profile.replace("]}","]")
             Profile = Profile.replace("[\"[\'","[\'")
             Profile = Profile.replace("\']\"]","\']")
             Profile = Profile.replace("\',\",","\',")
             Profile = Profile.replace("\"\'","\'")
             Flag_1 = True
             
    Profile = eval(Profile)
             
    Flag_2 = False
    while Flag_2 == False:
        if args.input2 != None:
          if any(i in valid_File for i in str(args.input2)) == True:
             filename = str(args.input2[0])
             file = open(filename, "r")
             Text = file.read()
             Flag_2 = True
          else:
             Text = str(args.input2)

    print(Pr(Text, Profile))
    return Pr(Text, Profile)
#   
# ActualCode from here on https://stepik.org/lesson/23065/step/11?unit=6798
#

def Pr(Text, Profile):
     
    
    c=0
    Pr=1
    for letter in Text:
        Pr=Pr*Profile[letter][c]
        c+=1
    
    return Pr





if __name__ == '__main__':
    main() 