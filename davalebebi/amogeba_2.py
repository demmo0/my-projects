import os
from time import perf_counter

start=perf_counter()

src_path = "davalebebi\\"
datasettemplate = {
    "sourceplatform":"livo",
    "fromdate":"2022-04-07",
    "action":"cartadd",
    "todate":"2023-01-15"
}

def amogeba(src_path,datasettemplate):
    path = src_path

    path += datasettemplate["sourceplatform"] + '\\'
    path += datasettemplate["action"] + '\\'

    from_date = datasettemplate['fromdate'].split('-')
    to_date = datasettemplate['todate'].split('-')

    if os.path.isdir(path) == False:
        print("no files were found")
        return 0

    path_lst=[]

    for root, dirs, files in os.walk(path):
        for filename in files:
            path_lst.append(os.path.join(root, filename))

    for i in path_lst:
        buff=i.split('\\')
        if(buff[-6]>=to_date[0]):
            return 0
        elif(buff[-6]==to_date[0] and buff[-5]>to_date[1]):
            return 0
        elif(buff[-6]==to_date[0] and buff[-5]==to_date[1] and buff[-4]>to_date[2]):
            return 0

        if(buff[-6]>=from_date[0] and buff[-5]>=from_date[1] and buff[-4]>=from_date[2]):
            
            print(i)

amogeba(src_path,datasettemplate)

print('time taken = ' + str(perf_counter()-start))