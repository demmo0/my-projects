
import numpy as np


def bigger_is_better(word):

    # stringis listad gardaqmna 
    lword=[]

    for i in word:
        lword.append(i)
    
    i=0
    k=0

    while i < (len(lword)-1):
        #asota mimdevrobashi uknidan moyolebuli klebis dafiqsireba
        if(lword[(-1-i)]>lword[(-2-i)]):


            #klebis adgilidan bolomde asoebis zrdis mixedvit sortireba
            buff=lword[(-1-i):]
            buff.sort()

            #iseti umciresi asos amorcheva romelic shesacvleli asos toli ar aris
            for min_letter in buff:
                if(min_letter>lword[(-2-i)]):
                    break

            #zemot napovni asos indexis modzebna
            for z in word:
                if(z==min_letter):
                    index=k
                k+=1

            #asoebis gadaadgileba
            temp=lword[(-2-i)]
            lword[(-2-i)]=min_letter

            k=0
            for x in buff:
                if(x==min_letter):
                    buff[k]=temp
                k+=1


            #listis isev stringad gadmoqceva
            returnstring=''
            k=1
            for x in buff:
                
                lword[(-2-i+k)]=x

                k+=1

            for x in lword:
                returnstring+=x

            return returnstring
        i+=1
    return 'no answer'

def Exercise2():
    words=[]
    i=0

    #informaciis shetana

    print('sheiyvanet sasurveli sityvebis raodenoba:')

    numofwords=int(input())

    if(numofwords > pow(10,5) or numofwords < 1):
        print('error')
        return 0

    while i<numofwords:
        i+=1
        print('gtxovt sheiyvanot sityva nomeri ',i,':')
        words.append(input())
        length=len(words[i-1])
        if(length<=1 or length>=100):
            print('error')
            return 0

    for i in words:
        print(bigger_is_better(i))

Exercise2()

