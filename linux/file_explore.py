
import os, time

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
     
def print_screen(path,find,note):
    os.system('clear')
    print("===============================================================")
    print(note)
    print("===============================================================")
    print(path)
    print("---------------------------------------------------------------")
    ind=-1
    for i in find:
        ind+=1
        print(ind," -- ",i)
    print("---------------------------------------------------------------")
    print("commands: |#back| |#done| |#reset| |#choose| |#i[index]| |item|")
    print("===============================================================")
    cmd=input(">> ")
    if cmd[0]=="#" and cmd[1]=="i" :
        cmd=cmd.replace(cmd[0],"")
        cmd=cmd.replace(cmd[0],"")
        cmd=int(cmd)
        cmd=find[cmd]
    elif cmd[0]=="#":
        cmd= lst_about(cmd,['#back','#done','#reset',"#choose"])
    else:
        cmd=lst_about(cmd,find)
        
    return cmd
def explore(base="",note="Explorer"):
    
    cmd=""
    if base!="":
        pathcomp.append(base)
    else :
        pathcomp=[]
    path=""
    while cmd!="#done":
        path=""
        try:
            if pathcomp==[]:
                shpath="Base dir/"
                find=os.listdir()
            else:
                path=""
                for i in pathcomp:
                    if path=="":
                        path=i
                    else:
                        path=path+"/"+i
                    shpath="Base dir/"+path
                find=os.listdir(path)
            cmd=print_screen(shpath,find,note)
            if cmd[0]!="#":
                try:
                    if path == "":
                        a= cmd
                    else:
                        a=path+"/"+cmd
                    os.listdir(a)
                    pathcomp.append(cmd)       
                except:
                    path=path+"/"+cmd
                    cmd="#done"
            else:
                if cmd=="#back":
                    pathcomp.remove(pathcomp[-1])
                elif cmd=="#reset":
                    cmd=""
                    pathcomp=[]
                    path=""
                    a=int("w")
                elif cmd=="#choose":
                    base=input("Enter the path for the base directory: ")
                    pathcomp=[base]
        except:
            print ('error') 
            cmd=""
            pathcomp=[]
            path=""
            time.sleep(0.5)  
    if path[0]=="/" and base!= "":
        path=path.replace(path[0],"",1)      
    return path

