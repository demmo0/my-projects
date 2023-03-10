
import json
import shutil
import os
from time import perf_counter

start=perf_counter()

src_path = "C:/Users/User/Desktop/my projects/davalebebi/data"
des_path = "davalebebi/"

def chawera(src_path,des_path):
    f = open(src_path,'r')
    #with open --------------------------------------------------------------------------

    #vaketebt python dictad jsons
    df = json.load(f)
    path = des_path
    #json filis wakitxva pirdapir dataframad---------------------------------------------

    #jsonshi informaciidan vaketebt paths
    for i in df:
        if i == "timestamp":
            continue
    
        path += str(df[i]) + '/'
    #dataframidan pirdapir amorcheba columnebis ---------------------------------------------

    #tu ar arsebobs vqmnit
    try:
        os.makedirs(path)
    except:
        pass
    #makedirs garda sxva metodebi-----------------------------------

    #vakopirebt files sachiro adgilas
    path += src_path.split('/')[-1]
    shutil.copyfile(src_path,path)

for i in os.listdir(src_path):
    chawera(src_path+'/'+i,des_path)

print('time taken = ' + str(perf_counter()-start))
#.../livo/itemview/year/month/day/hour/minute/
