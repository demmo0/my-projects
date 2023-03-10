
import json
import shutil
import os
from time import perf_counter
import pandas as pd

start=perf_counter()

src_path = "C:/Users/User/Desktop/my projects/davalebebi/data"
des_path = "davalebebi/"

def chawera(src_path,des_path):

    with open(src_path,'r') as f:
        data=json.load(f)

    df = pd.DataFrame({'count' : data})
    #vaketebt python dictad jsons
    path = des_path
    path += df['count']['sourceplatform']+'/'
    path += df['count']['action']+'/'
    path += str(df['count']['year'])+'/'
    path += str(df['count']['month'])+'/'
    path += str(df['count']['day'])+'/'
    path += str(df['count']['hour'])+'/'
    path += str(df['count']['minute'])+'/'

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
