import math
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

@Gooey(program_name="entropy of the NF-κB motif matrix", program_description='entropy of the NF-κB motif matrix(A,C,G,T)')
def main():

    if CL_Flag == False:
        parser = GooeyParser(conflict_handler='resolve', description="A file in dict form or raw")       
        parser.add_argument('a', type=str, nargs='?', help='(A) filename or [#,#,#,#]' , widget="FileChooser")              
        parser.add_argument('c', type=str, nargs='?', help='(C) filename or [#,#,#,#]' , widget="FileChooser")  
        parser.add_argument('g', type=str, nargs='?', help='(G) filename or [#,#,#,#]' , widget="FileChooser")  
        parser.add_argument('t', type=str, nargs='?', help='(T) filename or [#,#,#,#]' , widget="FileChooser")          
    if CL_Flag == True:
        parser = argparse.ArgumentParser(conflict_handler='resolve')              
        parser.add_argument('a', type=str, nargs='?', help="(A) filename or [#,#,#,#]" )
        parser.add_argument('c', type=str, nargs='?', help="(C) filename or [#,#,#,#]" )
        parser.add_argument('g', type=str, nargs='?', help="(G) filename or [#,#,#,#]" )
        parser.add_argument('t', type=str, nargs='?', help="(T) filename or [#,#,#,#]" )

    args = parser.parse_args()
    print("Debug: a:",args.a," c:",args.c," g:",args.g," t:", args.t)
    Flag_1 = False
    while Flag_1 == False:
        s1 = args.a
        if validSequence(s1) == True:
            a = str(args.a)
            Flag_1 = True
        if validFileName(args.a[0]) == True:
            filename = str(args.a)                 
            file = open(filename, "r")
            a = file.read()
            Flag_1 = True

                 
    # Clean it up if its alredy in data dictionary format
#    a = a.replace("{[","[")
#    a = a.replace("]}","]")
#    a = a.replace("[\"[\'","[\'")
#    a = a.replace("\']\"]","\']")
#    a = a.replace("\',\",","\',")
#    a = a.replace("\"\'","\'")
    
    Flag_1 = False
    while Flag_1 == False:
        s1 = args.c
        if validSequence(s1) == True:
            c = str(args.c)
            Flag_1 = True
        if validFileName(args.c) == True:
            filename = str(args.c[0])                 
            file = open(filename, "r")
            c = file.read()
            Flag_1 = True

                 
    # Clean it up if its alredy in data dictionary format
#    c = c.replace("{[","[")
#    c = c.replace("]}","]")
#    c = c.replace("[\"[\'","[\'")
#    c = c.replace("\']\"]","\']")
#    c = c.replace("\',\",","\',")
#    c = c.replace("\"\'","\'")
    
    Flag_1 = False
    while Flag_1 == False: 
        s1 = args.g
        if validSequence(s1) != True:
            g = args.g
            Flag_1 = True
        elif validFileName(args.g[0]) == True:
            filename = str(args.g[0])                 
            file = open(filename, "r")
            g = file.read()
            Flag_1 = True

                 
    # Clean it up if its alredy in data dictionary format
#    g = g.replace("{[","[")
#    g = g.replace("]}","]")
#    g = g.replace("[\"[\'","[\'")
#    g = g.replace("\']\"]","\']")
#    g = g.replace("\',\",","\',")
#    g = g.replace("\"\'","\'")
    
    Flag_1 = False
    while Flag_1 == False: 
        if validSequence(s1) == True:
            t = str(args.t)
            Flag_1 = True
        elif validFileName(args.t[0]) == True:
            filename = str(args.t[0])                 
            file = open(filename, "r")
            t = file.read()
            Flag_1 = True

                 
    # Clean it up if its alredy in data dictionary format
#    t = t.replace("{[","[")
#    t = t.replace("]}","]")
#    t = t.replace("[\"[\'","[\'")
#    t = t.replace("\']\"]","\']")
#    t = t.replace("\',\",","\',")
#    t = t.replace("\"\'","\'")
 
    try:
        a = eval(a)
        c = eval(c)
        g = eval(g)
        t = eval(t)
    except:
        print("eval error setting a,c,g,t to arg values")
        a = args.a
        c = args.c
        g = args.g
        t = args.t

    try:
        print("Entropy Value:", entropy(a,c,g,t))
        return entropy(a,c,g,t)
    except:
        print("error")
        return 0


def validSequence(s1):
    valid = "[]"
    s2 = str(s1)
    print(s2)
    for character in str(s2):
        if character in valid:
            print("seq valid")
            return True
    return False

def validFileName(s1):
    valid = 'C:/'
    for letter in str(s1):
        if letter in valid:
             print("file valid")
             return True
    return False

def entropy(a,c,g,t):
#    a=[0.2,0.2,0.9,0.1,0.1,0.1,0.3]
#    c=[0.1,0.6,0.4,0.1,0.2,0.4,0.6]
#    g=[1,1,0.9,0.9,0.1]
#    t=[0.7,0.2,0.1,0.1,0.5,0.8,0.7,0.3,0.4]
    data_list=[a,c,g,t]

    H=0.0
    for j in data_list:
        for i in j:
            H=H+i*(math.log(i,2))
        
    return(-H)

if __name__ == '__main__':
    main() 