from colorama import Fore
import sys
import os
import json
global ddat
ddat={}
print(Fore.GREEN + """
                                                                                                  
                                                                                                  
                               ,--,                                    ___                        
                             ,--.'|             ,--,                 ,--.'|_                      
            ,---.     ,---.  |  | :           ,--.'|         ,---,   |  | :,'   __  ,-.   ,---.   
           '   ,'\   '   ,'\ :  : '           |  |,      ,-+-. /  |  :  : ' : ,' ,'/ /|  '   ,'\  
   ,---.  /   /   | /   /   ||  ' |           `--'_     ,--.'|'   |.;__,'  /  '  | |' | /   /   | 
  /     \.   ; ,. :.   ; ,. :'  | |           ,' ,'|   |   |  ,"' ||  |   |   |  |   ,'.   ; ,. : 
 /    / ''   | |: :'   | |: :|  | :           '  | |   |   | /  | |:__,'| :   '  :  /  '   | |: : 
.    ' / '   | .; :'   | .; :'  : |__         |  | :   |   | |  | |  '  : |__ |  | '   '   | .; : 
'   ; :__|   :    ||   :    ||  | '.'|        '  : |__ |   | |  |/   |  | '.'|;  : |   |   :    | 
'   | '.'|\   \  /  \   \  / ;  :    ;        |  | '.'||   | |--'    ;  :    ;|  , ;    \   \  /  
|   :    : `----'    `----'  |  ,   /         ;  :    ;|   |/        |  ,   /  ---'      `----'   
 \   \  /                     ---`-'          |  ,   / '---'          ---`-'                      
  `----'                                       ---`-'                                             
                                                                                                  
""")
def terminal():
    print(Fore.BLUE + "[1] custom image")
    print("[2] animated welcome")
    print("[3] color")
    print("[4] save intro")
    print("[5] exit")
    print("[6] delete intro")
    print("[7] see json data in this moment")
    usr=input(Fore.WHITE + "> ")
    if usr=="1":
        print("Want to show image?")
        choice=input("(y/n)> ")
        if choice=="y":
            if os.path.exists("../home")==True:
                pass
            else:
                print(Fore.RED + "You are not in main directory.(home)")
                terminal()
            ddat.update({"big_text_show": True})
            img=input("img_path> home/")
            if os.path.exists(img)==True:
                print("IMG found.")
                os.system("termimage " + img)
                ddat.update({"img_path": str(img)})
                print("Image setted up.")
                terminal()
            else:
                print(Fore.RED + "Not Found.")
                terminal()
        elif choice=="n":
            ddat.update({"big_text_show": False})
            terminal()
        else:
            print(Fore.RED + "Invalid option, operation denied.")
            terminal()
    elif usr=="2":
        print("Want to show animated welcome?")
        choice=input("(y/n)> ")
        if choice=="y":
            ddat.update({"animated_text": True})
            usr=input("Insert your nickname for the welcome>> ")
            ddat.update({"animation_text": f"Welcome in termux, {usr}"})
            terminal()
        elif choice=="n":
            ddat.update({"animated_text": False})
            terminal()
        else:
            print(Fore.RED + "Invalid option, operation denied.")
            terminal()
    elif usr=="3":
        pass
    elif usr=="4":
        data=open("CoolIntro/.assets/scripts/data.json", "w")
        data.write(json.dumps(ddat))
        data.close()
        print("data saved")
        terminal()
    elif usr=="5":
        sys.exit(0)
    elif usr=="6":
        try:
            os.remove("CoolIntro/.assets/scripts/data.json")
            print("Data removed.")
            terminal()
        except FileNotFoundError:
            print(Fore.RED + "FileNotFound: data.json doesnt exists!")
            terminal()
    elif usr=="7":
        print(json.dumps(ddat, indent=4))
        terminal()
    else:
        print(Fore.RED + "Invalid Function: '" + str(usr) + "'")
        terminal()
terminal()
