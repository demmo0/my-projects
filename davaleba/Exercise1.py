import numpy as np

def Exercise1():
    words=[]
    i=0

    #informaciis shetana

    print('sheiyvanet sasurveli sityvebis raodenoba:')

    numofwords=int(input())

    if(numofwords>=pow(10,5) or numofwords <=1):
        print('error')
        return 0

    while i<numofwords:
        i+=1
        print('gtxovt sheiyvanot sityva nomeri ',i,':')
        words.append(input())


    # shetanili informaciis gadamushaveba
    unique_words, indexes=np.unique(words,return_index=True)
    
    unique_words_sorted=[]
    # sortireba 
    for i in sorted(indexes):
        unique_words_sorted.append(unique_words[np.where(indexes==i)])

    unique_words_sorted=[x for xs in unique_words_sorted for x in xs]
    

    word_count=[]
    for sityva in unique_words_sorted:

        word_count.append(words.count(sityva))

    print(len(unique_words_sorted))
    

    # gamotanis formati rom emtxvevodes magalits
    mystring=''
    for c in word_count:

        mystring+=str(c)+" "

    print(mystring)




Exercise1()

