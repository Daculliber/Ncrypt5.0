
import os,time
from file_enc import pin_enc, pin_dec, gen_key,keymanage
from func import lst_about, enter_pin, printhelp
from textencrypt import text_mode
from file_explore import explore
def clear():
    os.system ('cls')
def lin_startfile(file):
    '''outpfile=""
    for i in file:
        if i==" ":
            i="\\"+i
        outpfile+=i
    outpfile="xdg-open"+" "+outpfile
    os.system(outpfile)'''
    os.startfile(file)
clear()
print('''======================================================================
/  XXX    XX    ######  #####    ##  #####   #######         oo==oo  /
/  XXXX   XX   ####     ##   #   XX  ##   #    ##    ###    OO    OO /
/  XX XX  XX   ##       ### #    XX  ### #     ##   #####   ######## /
/  XX  XX XX   ##       ## ##    XX  ##        ##   #####   ##(  )## /
/  XX   XXXX   ####     ##  ##   XX  ##        ##    ###    ###()### /
/  XX    XXX    ######  ##   ##  XX  ##        ##           ######## /
======================================================================''')
time.sleep(1)
clear()
try:                                      
    setfile=open("setup.pyfl",'r')
    setup=setfile.read()
    ato=setup[0]
    rnc=setup[1]
    setfile.close()
except:
    setfile=open("setup.pyfl","w")
    setfile.write("00")
    setfile.close()
    ato="0"
    rnc="0"

try:
    keyfile=open("default.nKey","rb")
    ukey=keyfile.read()
    keyfile.close()
except:
    print("Key not found")
    input("Go to settings and get one. [ENTER]--OK")
    ukey=False

cmd=""
mode="file"
while cmd!="exit":
    clear()
    print('''====================================
             OPTIONS
====================================
Mode -------------------------(mode)
Help -------------------------(help)
Encrypt -------------------(encrypt)
Decrypt -------------------(decrypt)
Save and exit ----------------(exit)
Settings --------------------(setup)
====================================''')
    cmd=lst_about(input(">> "),['mode','help','encrypt','decrypt','exit',"setup"])
    clear()
    if cmd=="help":
        printhelp()
    elif cmd=="encrypt":        
        inp=explore()
        pin=enter_pin()
        pin_enc(inp,ukey,pin)
        print('encrypted')
        time.sleep(0.5) 
    elif cmd=="decrypt":
        print(os.listdir)
        inp=explore()
        pin=enter_pin()
        pin_dec(inp,ukey,pin)
        print('decrypted')
        if ato=="1":
            print("Opening...")
            try:
                lin_startfile(inp)
            except:
                print("Can't open the file")
        if rnc=="1":
            t=input('Do you want to re-encrypt? y/n ')
            if t=='y':
                pin_enc(inp,ukey,pin)
                print("done")
        time.sleep(0.5)            


    elif cmd=="mode":
        print('''=========================
     ENCRYPTION MODE
=========================

File mode ---------(file)
Text mode ---------(text)

=========================''')
        print("<--[back] current: ["+mode+"]")
        print('''=========================''')
        cmd = input(">> ")
        cmd=lst_about(cmd,["back","file","text"])
        if cmd!="back":
            mode=cmd
        if mode =="text":
            while cmd!='exit' and mode=='text':
                cmd=text_mode()
                if cmd=="back":
                    mode="file"
    elif cmd=="setup":
        while cmd!= "back":
            clear()
            print('''===================================================
                     SETTINGS
===================================================
Key management -------------------------------(key)
Open file after decryption -------------(auto-open) 
Ask if re-encrypt after decryption ----(re-encrypt)
===================================================
<--[back]
===================================================''')
            cmd=input(">> ")
            cmd=lst_about(cmd,["key",'back',"auto-open","re-encrypt"])
            if cmd=="key":
                ukey=keymanage(ukey)
                cmd=""
            elif cmd=='auto-open':
                if ato=="0":
                    b='(0   )'
                elif ato=="1":
                    b='(   0)'
                print('''===========================
 AUTO-OPEN | OFF'''+b+'''   ON
===========================''')
                cmd=input("1/0 ")
                if cmd not in["1","0 "]:
                    cmd="0"
                ato=cmd
            elif cmd=="re-encrypt":
                if rnc=="0":
                    b='(0   )'
                elif rnc=="1":
                    b='(   0)'
                print('''============================
 RE-ENCRYPT | OFF  '''+b+''' ON
============================''')
                cmd=input("1/0 ")    
                if cmd not in["1","0 "]:
                    cmd="0"
                rnc=cmd      
            else:
                pass
    elif cmd=="exit":
        setfile=open("setup.pyfl","w")
        setfile.write(ato+rnc)
        setfile.close()
    else:
        pass
