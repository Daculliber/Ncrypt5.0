#windows
import random,os
from func import lst_about
def clear():
    os.system ('cls')
def enter_PIN(pasword):
    code=0
    for i in pasword:
        a=int(pasword[3])
        code+=int(i)
    code=code*a
    return code
def Ncrypt(inp,password):
    inp+="/spl/"
    exch = ("abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZăîâșțĂÎÂȘȚ/,.!1234567890?")
    for i in range(enter_PIN(password)):
        Enc=""
        while len(inp)>0:
            while len(inp)<21:
                inp+=random.choice(exch)    
            inpsc=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            a=""
            for i in inpsc:
                a += inp[i]
            inp=inp.replace(a,"")

            enckey=[15,10,19,8,16,3,17,4,12,6,20,2,13,9,1,14,11,18,5,0,7]
            enc=""
            for i in enckey:
                enc += a[i]
            Enc=Enc+enc
        inp=Enc
    return Enc
def Dcrypt(inp,password):
    for i in range(enter_PIN(password)):
        Enc=""
        while len(inp)>0:
            while len(inp)<21:
                inp=inp+"/"
            inpsc=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            a=""
            for i in inpsc:
                a += inp[i]
            inp=inp.replace(a,"")

            deckey=[19,14,11,5,7,18,9,20,3,13,1,16,8,12,15,0,4,6,17,2,10]
            enc=""
            for i in deckey:
                enc += a[i]
            Enc=Enc+enc
        inp=Enc
    try:
        ainp,rv=Enc.split("/spl/",1)
        Enc=ainp
    except:
        Enc="Wrong PIN"
    return Enc

    print()
def text_mode():
    clear()
    print("Text mode")
    print('''====================================
                OPTIONS
====================================
File mode --------------------(back)
Encrypt -------------------(encrypt)
Decrypt -------------------(decrypt)
Save and exit ----------------(exit)
====================================''')
    cmd=input(">> ")
    clear()
    cmd=lst_about(cmd,["back","encrypt","decrypt","exit"])
    if cmd=="encrypt":
        print('''========================================================================''')
        print('''                                ENCRYPT''')
        print('''========================================================================''')
        txt=input('Enter text: ')
        print('''========================================================================''')
        pin=input('Enter pin :')
        res=Ncrypt(txt,pin)
        clear()
        print('''========================================================================''')
        print("                              ENCRYPTED TEXT")
        print('''========================================================================''')
        print(res)
        print()
        print('''========================================================================''')
        print("[enter] = back")
        print('''========================================================================''')
        input()
    elif cmd=="decrypt":
        print('''========================================================================''')
        print('''                                DECRYPT''')
        print('''========================================================================''')
        txt=input('Enter text: ')
        print('''========================================================================''')
        pin=input('Enter pin :')
        res=Dcrypt(txt,pin)
        clear()
        print('''========================================================================''')
        print("                              DECRYPTED TEXT")
        print('''========================================================================''')
        print(res)
        print()
        print('''========================================================================''')
        print("[enter] = back")
        print('''========================================================================''')
        input()
    else:
        pass
    return cmd






