#MADE WITH PYTHON 3.10.4

import os
import sys
import requests
from platform import system

LOGO = """
██████╗░██████╗░██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗╚════██╗██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗
██████╔╝██████╦╝░░███╔═╝██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║
██╔═══╝░██╔══██╗██╔══╝░░██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║
██║░░░░░██████╦╝███████╗██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═════╝░╚══════╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░
"""

#Windows check
if not system() == "Windows":
    print("\nThis script was made for Windows!\n")
    sys.exit()

os.system("cls")
os.system("color 3")

def get_game(path, mode=1):

    if mode == 1:
        #Classic
        URL = "https://www.plazmaburst2.com/pb2/Plazma Burst 2.zip"
    elif mode == 2:
        #VBS version
        URL = "https://www.plazmaburst2.com/pb2/Plazma Burst 2 vbs.zip"
    elif mode == 3:
        #SWF
        URL = "https://www.plazmaburst2.com/pb2/pb2_re34.swf"
    else:
        os.system("color 4")
        print("\nInvalid mode chosen, try again!")
        return

    name = URL.split("/")[-1]
    PATH = os.path.join(path, name)
    
    with requests.Session() as s:
        req = s.get(URL)
        stream = req.content

        try:
            with open(PATH, 'wb') as manager:
                manager.write(stream)
            print("File {} was succesfully saved in {}!".format(name, path))

            return
        except Exception as ex:
            print("\n" + ex + "\n")
            
    return
         

def main():
    dsk = os.getcwd()
    
    #Argument parse
    if len(sys.argv) == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        try:
            assert arg1 == "-d" or arg1 == "--download","Not a valid argument!"
            arg2 = int(arg2)
        except Exception as ex:
            os.system("color 4")
            print(f"\n{ex}\n")
            return
        print("\nDownloading...\n")

        get_game(dsk, arg2)
            
    else:
        os.system("color E")
        print("""
Please use this as reference:

#Mode# -> 1 (normal), 2 (vbs), 3 (swf file)

Command example:

C:\\Users\\user> python pb2d.py -d 1
""")
        return

#START
if __name__ == "__main__":
    print(LOGO)
    main()
