import os
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import pandas as pd
import csv
import time
import datetime
from datetime import timedelta
import glob
import palettable
import matplotlib.colors as mcolors

import mplhep as hep 
hep.style.use(hep.style.ROOT)
from pandas import NaT

fn2 = glob.glob("*stress*.txt")
split_name_stress = fn2[0].split('.txt')
chamber_name_stress= split_name_stress[0]

### function that returns the rows with delta above threshold ####
def sampling(df, thresh):

    thresh = pd.to_timedelta(thresh)
    time_diff = df.diff().fillna(pd.Timedelta(seconds=0))
    ret = [0]
    running_total = pd.to_timedelta(0)
    
    for i in df.index:
        running_total += time_diff[i]
        #c += 1
        if running_total >= thresh:
            c = 0
            ret.append(i)
            running_total = pd.to_timedelta(0)
        #print(c)

    return df.loc[ret].copy()


def plot_long_stability_trip_info(chamberName):

    chamber_name = chamberName
    barplot_results = []
    chamber_list_plot = []
    len_histo = 30
    #If the name of the folders/files doesn't follow the template, change them
    current_path_name= str(chamber_name)+'.txt'   
    current_path_name_plot= str(chamber_name.split('_20')[0])

    print(current_path_name)        

    if (os.path.isfile(current_path_name)==True):
        list_string_times =[]
        list_delta_times=[]
        
        df = pd.read_csv(current_path_name,header=None, delimiter = " ", on_bad_lines='skip')

        datetimeFormat='%d/%m/%Y %H:%M:%S'

        #Remove the data without "Tripped during stability test at:'

        df= pd.DataFrame(np.array(df[df[2]!="scan"]))

        df[6] = df[6].str.replace(",","")


        df['datetime']=df[5]+' '+df[6]
        df['datetime']=pd.to_datetime(df['datetime'])

        #Remove the values created after less than 2 minutes
        df['datetime'] = pd.DataFrame(sampling(df['datetime'],'2M'))

        df = df.dropna(subset=['datetime'])
        df['hour']=pd.DataFrame(sampling(df['datetime'],'1h'))
        df = df.reset_index(drop=True)

        df = df.dropna(subset=['hour'])
        idx = np.array(df.index)
        trips_per_hour = []
        
        for i in range(1,len(idx)):
            trips_per_hour.append(idx[i]-idx[i-1])
            
         
        #list_histogram=trips_per_hour[:] #The last hour is not always complete, so we remove it.
        #plt.figure(figsize=(25, 20))
        fig1, ax_trip = plt.subplots(figsize=(10, 8))
        plt.bar(np.arange(1,len(trips_per_hour)+1),trips_per_hour,width=0.5, color='green')#, edgecolor='black', linewidth=2)
        plt.xlabel('Time [h]')
        plt.ylabel('Number of trips')
        plt.xticks(np.arange(1,16))#len(list_histogram)+1))
        plt.xlim(0, 16)
        plt.ylim(0, 30)
        #plt.text(4, 4, 'Preliminary',fontsize=35, color='gray',alpha=0.5)
        hep.cms.text("Preliminary", fontsize=21)
        hep.cms.lumitext('GE21-MODUELE-'+fn2[0].split('_')[1]+'-'+fn2[0].split('_')[2],fontsize=21)
        plt.savefig("plots/"+current_path_name_plot)
        plt.savefig("plots_pdf/"+current_path_name_plot+'.pdf')
        
        #plt.show()
        
    else:
        print("ERROR: The file doesn't exist")
        
   