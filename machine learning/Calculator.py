#biblioteka
import numpy as np

R_Digits={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
Operations=['*','/','+','-']

def Divide(inp):
    buff=[]
    temp=[]
    k=0

    for i in inp:
        #naxulobs plius minuss
        for j in Operations:
            if(j==i):
                k+=1
                break
        #operaciis nishans da operaciis shemdgom mdgoms yops
        if((k%3)!=0):
            buff.append(temp.copy())
            k+=1
            temp.clear()

        temp.append(i)

    buff.append(temp.copy())

    return buff

def Convert(inp):

    temp=[]
    buff=[]

    for i in inp:
        #tu plius minusia pirdapir wers
        if i[0] in Operations:
            buff.append(i[0])
            continue
        #tu araa plius minusi
        for k in i:
            #mowmdeba carieli adgilia tu ara
            #da cdilobs modzebnos asos shesabamisi ricxviti mnishvneloba
            if(k!=' '):
                try:
                    temp.append(R_Digits[k])
                except:
                    return 0
            else:
                continue
        
        buff.append(temp.copy())
        temp.clear()



    return buff

def Convert_plus(inp):

    temp=[]
    buff=[]
    #tu shetanilis sigrdze ertia pirdapir iwereba
    
    for i in inp:
        if(len(i)<=1):
            buff.append(i)
            continue

        #ganixilavs gamoklebis shemtxvevebs
        for j in i:
            temp.append(j)
        
        if(temp[0]<temp[1]):
            temp.clear()
            temp.append(i[1]-i[0])
            if(len(i)>2):
                for j in i[2:]:
                    temp.append(j)

        #bolodhi ari gamoklebiani
        if(temp[len(temp)-2]<temp[len(temp)-1]):
            temp[len(temp)-2]=temp[len(temp)-1]-temp[len(temp)-2]
            temp.pop()
        buff.append(temp.copy())
        temp.clear()
    #tu arasworadaa dawerili romaulad anu bevrjer ari gameorebuli
    for i in range(0,len(buff)):
        a,count=np.unique(buff[i],return_counts=1)
        for k in count:
            if(k>3):
                return 0
    
    temp.clear()
    #dajameba
    for i in buff:
        if(i in Operations):
            temp.append(i)
        else:
            temp.append(sum(i))

        

        
    return temp

def Calculate(inp):

    for i in Operations:
        while i in inp:

            #index of operation
            #mimateb gamoklebebi
            i_of_op=inp.index(i)
            if i=='*':
                inp[i_of_op-1]=inp[i_of_op-1]*inp[i_of_op+1]
            elif i=='/':
                inp[i_of_op-1]=inp[i_of_op-1]/inp[i_of_op+1]
            elif i=='+':
                inp[i_of_op-1]=inp[i_of_op-1]+inp[i_of_op+1]
            elif i=='-':
                inp[i_of_op-1]=inp[i_of_op-1]-inp[i_of_op+1]
            k=0
            #chanacvleba
            for j in inp[i_of_op+2:]:
                inp[i_of_op+k]=j
                k+=1
            inp.pop()
            inp.pop()
            #
    return sum(inp)

def Convert_result(Number):
    #shemowmeba romaulad 
    if(Number<=0):
        return 0

    keys=list(R_Digits.keys())

    k=0
    Dict={}
    for i in keys:
        #pirveli ricxvi daimaxsovra
        if(k==0):
            buff=i
        #poulobs shualeduri ricxvis romaul agweras da mis mnishvnelobas
        elif(k%3!=0):
            Dict[buff+i]=R_Digits[i]-R_Digits[buff]
        else:
            keys1=list(Dict.keys())
            buff=keys1[len(keys1)-1]
            Dict[buff+i]=R_Digits[i]-R_Digits[buff]
            k+=1

        Dict[i]=R_Digits[i]

        k+=1

    #ricxvis gadaromauleba

    keys=list(Dict.keys())
    k=len(keys)-1
    buff=''
    while(Number!=0):
        
        val=Dict[keys[k]]

        if(Number>=val):
            Number=Number-val
            buff+=keys[k]
        elif(k!=0):
            k-=1


    return buff

 #mtavari programa
while(True):

    print('Shemoiyvanet romauli operacia:')
    inp=input()

    if(inp=='Exit'or inp=='exit'):
        break

    Return_value=Divide(inp)
    Return_value=Convert(Return_value)

    if(Return_value==0):
        print('GTXOVT SHEMOITANOT ROMAULI NISHNEBI SWORAD!!!\n\n')
        continue
    
    Return_value=Convert_plus(Return_value)
    narmalni_ricxvebi=Return_value.copy()

    if(Return_value==0):
        print('SHEMOITANET SWORI PORMATIT, DAPIQSIREBULIA BEVRI GAMEOREBA!!!\n\n')
        continue

    Return_value=Calculate(Return_value)

    narmalni_ricxvebi.append('=')
    narmalni_ricxvebi.append(Return_value)

    Return_value=Convert_result(Return_value)
    if(Return_value==0):
        print("SHEDEGIS ROMAULAD CHAWERA SHAUDZLEBELIA!!!\n\n")
        continue

    print(inp+'='+Return_value)

    narmalni_ricxvebi_saboloo=''

    for i in narmalni_ricxvebi:
        narmalni_ricxvebi_saboloo+=str(i)
    print('('+narmalni_ricxvebi_saboloo+')'+'\n')




