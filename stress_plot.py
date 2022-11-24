import os
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import csv
import glob
import pandas as pd
import mplhep as hep 
hep.style.use(hep.style.ROOT)

fn2 = glob.glob("*stress*.txt")
split_name_stress = fn2[0].split('.txt')
chamber_name_stress= split_name_stress[0]

def plot_stress(chamberName):
    #fn = glob.glob("*stress.txt")
    #split_name = fn[0].split('-stress')
    #chamber_name = split_name[0]
    chamber_name = chamberName
    current_path_name=str(chamber_name)+'.txt'   
    current_path_name_plot=str(chamber_name.split('_20')[0])
    

    print(current_path_name)        

    stress_GEM1 = []
    stress_GEM2 = []
    stress_GEM3 = []
    steps = [1, 2, 3, 4, 5]
    
    if (os.path.isfile(current_path_name)==True):
        list_string_times =[]
        list_delta_times=[]
        
        
    df = pd.read_csv(current_path_name,header=None, delimiter = " ")
    
    if ('PM,'or'AM,') in df[2].values:
        df.drop([2], axis=1, inplace=True)
        df.columns = [0,1,2,3,4,5,6,7,8]
    
    
            
    stress_GEM3 = np.array(df[(df[5] == '#3,') & (df[7]>1.)][7])
    stress_GEM2 = np.array(df[(df[5] == '#2,') & (df[7]>1.)][7])
    stress_GEM1 = np.array(df[(df[5] == '#1,') & (df[7]>1.)][7])


    fig1, ax_stress = plt.subplots(figsize=(10, 8))
    #fig = plt.figure(figsize=(8, 6), constrained_layout=False)
    plt.xlabel('iterative steps')
    ax_stress.set_xticks([1,2,3,4,5,6])
    plt.ylabel('Trip voltage [V]')
    plt.xlim([0,6])
    plt.ylim([400,1000])
    #if (len(stress_GEM1) <= 5):
    plt.plot(steps[:len(stress_GEM1)], stress_GEM1,linestyle='--', label='GEM1', marker='o')
    #if (len(stress_GEM2) <= 5):
    plt.plot(steps[:len(stress_GEM2)], stress_GEM2,linestyle=':', label='GEM2',  marker='v')
    #if (len(stress_GEM3) <= 5):
    plt.plot(steps[:len(stress_GEM3)], stress_GEM3,linestyle='-.', label='GEM3',  marker='s')
       
    plt.text(2, 500, 'CMS GE2/1 Triple-GEM Detector'"\n""Gas = $CO_{2} 100$% ",fontsize=18, color='black')#,alpha=0.5)
    hep.cms.text("Preliminary", fontsize=21)
    hep.cms.lumitext('GE21-MODUELE-'+fn2[0].split('_')[1]+'-'+fn2[0].split('_')[2],fontsize=21)
    ax_stress.legend(frameon=True) 
   
    plt.savefig("plots/"+current_path_name_plot)
    plt.savefig("plots_pdf/"+current_path_name_plot+".pdf")
    
  
   
 
