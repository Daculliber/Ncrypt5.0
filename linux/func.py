
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
    print('''''')
# it checks how similar is 'inp' to 'exsp', and if it is similar enough, returns exsp.
#inp  = input
#exsp = expected input
#sim  = match percent (sensibility)
#rt   = retun 'exp' exected, or 'prc' match percent

#for i in range(1234432):
#    abc=input(">>> ")


