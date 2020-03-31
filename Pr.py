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

@Gooey(program_name="Pr(Text, Profile)", program_description='Stand Alone Pr(Text, Profile) Routine')
def main():


    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="Enter DNA or select or type a filename")
        parser.add_argument('input2', type=str, nargs='?', help='Text' , widget="FileChooser") 
        parser.add_argument('input1', type=str, nargs='*', help='Profile: DNA without \' \" or , (s) or FileName of a properly formatted data dictionary' , widget="FileChooser")       
        
        
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')
        parser.add_argument('input2', type=str, nargs='?', help="Text file or raw" ) 
        parser.add_argument('input1', type=str, nargs='?', help="Profile file or raw" )
   
    args = parser.parse_args()
    valid_File = '/.tx'
    Flag_1 = False
    while Flag_1 == False:
        if args.input2 != None: 
             s1 = args.input2
             if validSequence(s1) == True:
                 Text = str(args.input2)
                 Flag_1 = True
             if any(i in valid_File for i in str(args.input2)) == True:
                 filename = str(args.input2)
                 file = open(filename, "r")
                 Text = file.read()
                 Flag_1 = True
             

             
    Flag_1 = False
    while Flag_1 == False:
        if args.input1 != None:
          if len(str(args.input1)) < 30:
             if CL_Flag == False:
                 filename = str(args.input1[0])
             if CL_Flag == True:
                 filename = str(args.input1)
             file = open(filename, "r")
             Profile = file.read()
             Profile = eval(Profile)
             Flag_1 = True
          else:
             Profile = str(args.input1)
             Profile = Profile.replace('["{','{')
             Profile = Profile.replace("]}']","]}") 
             Profile = Profile.replace(",', '",", ")
             old = "\':\", \'["
             new = "\': ["
             Profile = Profile.replace(old,new)
             old = "],\', \""
             new = "] \'"
             Profile = Profile.replace(old,new)
             old = "] \'"
             new = "], "
             Profile = Profile.replace(old,new)
             Profile = eval(Profile)
             Flag_1 = True
             

    print(Pr(Text, Profile))
    return Pr(Text, Profile)
#   
# ActualCode from here on https://stepik.org/lesson/23065/step/11?unit=6798
#


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def validSequence(s1):
    valid = 'ACTGU'
    for letter in s1:
        if letter not in valid:
            return False
    return True





if __name__ == '__main__':
    main() 