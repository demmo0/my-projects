import os
from time import perf_counter

start=perf_counter()

src_path = "davalebebi/"
datasettemplate = {
    "sourceplatform":"livo",
    "fromdate":"2022-04-07",
    "action":"cartadd",
    "todate":"2023-01-15"
}

def amogeba(src_path,datasettemplate):
    path = src_path

    path += datasettemplate["sourceplatform"] + '/'
    path += datasettemplate["action"] + '/'

    from_date = datasettemplate['fromdate'].split('-')
    to_date = datasettemplate['todate'].split('-')

    if os.path.isdir(path) == False:
        print("no files were found")
        return 0

    #sachiro wlebis amogeba
    years = os.listdir(path)
    for i in years:
        if from_date[0] > i or i>to_date[0]:
            years.remove(i)


    for i in years:
        pathwyear = path+i+'/'

       
        for k in os.listdir(pathwyear):
            # vamushavebt tvis siswores
            if i==from_date[0] and k < from_date[1]:
                continue
            elif i==to_date[0] and k>to_date[1]:
                break
            
            pathwmonth=pathwyear+k+'/'


            for j in os.listdir(pathwmonth):

                # vamushavebt dgis siswores
                if i==from_date[0] and k==from_date[1] and j < from_date[2]:
                    continue
                elif i==to_date[0] and k==to_date[1] and j > to_date[2]:
                    break

                pathwday=pathwmonth+j+'/'

                for a in os.listdir(pathwday):
                    pathwmin=pathwday+a+'/'

                    for b in os.listdir(pathwmin):
                        pathwsec=pathwmin+b+'/'
                        
                        for c in os.listdir(pathwsec):
                            print(pathwsec+c)

          

amogeba(src_path,datasettemplate)

print('time taken = ' + str(perf_counter()-start))