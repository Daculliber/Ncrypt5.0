
def check(inp,exp):
    ind=0
    sim=0
    while len(exp)<len(inp):
        exp+="/"
    while len(exp)>len(inp):
        inp+="/"
    exp+="/"
    for i in inp:
        if i== exp[ind]:
            sim+=1
        ind+=1

    return sim
def about(inp,expec,sim=50,rt="exp"):
    exp=expec
    inp.replace(" ","")

    inp=inp.lower()
    exp=exp.lower()
    if len(exp)<len(inp):
        inte=exp
        exp=inp
        inp=inte
    sc=0
    lsc=0
    abs=len(exp)
    for i in exp:
        sc=check(inp,exp)
        inp="/"+inp
        if sc>lsc:
            lsc=sc
        
    sc=lsc/abs*100
    if rt=="exp":
        if sc>= sim:
            ret=expec
        else:
            ret=False
    elif rt=="prc":
        ret=sc
    return ret
def lst_about(inp,exp,sim=50):
    lval=0
    ret=False
    if type(inp)==list:
        for i in inp:
            val=about(i,exp,sim)
            if val!=False:
                ret=val
    elif type(exp)==list:
        for i in exp:
            val=about(inp,i,sim,"prc")
            if val>lval:
                lval=val
                ret=i        
    else:
        ret=about(inp,exp,sim)



    return ret        
def enter_pin():
    try:
        pins=input("enter pin: ")
        if len(pins)<4:
            print("pin must have at least 4 numbers")
            pins=input("enter pin: ")
        pin=int(pins[0])
        for i in pins:
            pin+=int(i)
            if int(pins[3])<pin:
                pin-=int(pins[3])
            elif int(pins[2])<pin:
                pin-=int(pins[2])
            else:
                pin+=2
            if pin==0 or pin==1:
                pin=4
    except:
        print('error')
    return pin

def printhelp():
    print('''======================================================================
/  XXX    XX    ######  #####    ##  #####   #######         oo==oo  /
/  XXXX   XX   ####     ##   #   XX  ##   #    ##    ###    OO    OO /
/  XX XX  XX   ##       ### #    XX  ### #     ##   #####   ######## /
/  XX  XX XX   ##       ## ##    XX  ##        ##   #####   ##(  )## /
/  XX   XXXX   ####     ##  ##   XX  ##        ##    ###    ###()### /
/  XX    XXX    ######  ##   ##  XX  ##        ##           ######## /
======================================================================

Welcome to Ncrypt 5.1
=======================================================================
This is a CLI encryption tool that will help you keep your secrets safe.

WHAT IS NEW
-----------------------------------------------------------------------
>> Pin bug solved. In the previous version, puting the wrong pin crashed
   the program but decrypted the file anyway. Now it will destroy the 
   file. Sometimes it just doesn't decrypt it though, but still, have 
   backups.
>> Interface design changed a bit.

FEATURES
------------------------------------------------------------------------
>> Encrypts files using a powerful encryption algorithm. It uses a key 
   file and a PIN.
>> Encrypts text using a simpler algorithm, with just a PIN, without using
   a key.
>> It can open the file automatically after decryption, and re-encrypt it
   with one command.
>> it has a bult-in file explorer.
>> It can save the settings. Close the program with 'exit' to save.


KNOWN ISSUES
-------------------------------------------------------------------------
>> There is a chance that some PIN combinations will give the same value,
   and thus sme other combunations might match. 
>> in text mode, some PIN combinations don't encrypt. They give the same
   output.

WARNING
-------------------------------------------------------------------------
>> Using the wrong key file or PIN might CORRUPT YOUR DATA.
>> Please make sure you back-up important files and keys.
>> Please don't store your key files together with the files. You can use 
   the explorer to select a key without setting it as default.
>> Please don't rely on the PIN. The PIN is safe only against a kid, any 
   hacker will break the PIN in five minutes. The KEY is what secures the 
   files.

USE AT YOUR OWN RISK
------------------------------------------------------------------------------
>> I offer this program open-source for free in the hope that will be useful, 
   and I offer no guaranties that it will work perfectly. 
>> I take no liability for any loss of data that the use of this program may
   cause. 
===============================================================================''')
    input('Press enter to exit')
# it checks how similar is 'inp' to 'exsp', and if it is similar enough, returns exsp.
#inp  = input
#exsp = expected input
#sim  = match percent (sensibility)
#rt   = retun 'exp' exected, or 'prc' match percent

#for i in range(1234432):
#    abc=input(">>> ")


