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

def plot_short_stability(chamberName):
    #fn = glob.glob("*stress.txt")
    #split_name = fn[0].split('-stress')
    #chamber_name = split_name[0]
    chamber_name = chamberName
    current_path_name=str(chamber_name+'.txt')   
    current_path_name_plot=str(chamber_name.split('_20')[0])
#

    print(current_path_name_plot) 


    if (os.path.isfile(current_path_name)==True):
        list_string_times =[]
        list_delta_times=[]
    
        with open(str(current_path_name), newline='') as csv_file:
            #csv_content = csv.reader(csv_file, delimiter=' ')
            df = pd.read_csv(csv_file, delimiter = "\t")


        #print(df)

        #print(df['G3T Vmon'])
        list_range = [5,50,150]

       
        x = range(1100)
        y = range(-5,5)

        fig = plt.figure(figsize=(15,12))
        ax1 = fig.add_subplot(111)

        ax1.set_xlabel('Vmon[V]', fontsize=32)
        ax1.set_ylabel('Imon[$\mu$A]', fontsize=32)
        #ax1.xlim([0,5])
        ax1.set_xlim([0,1100])
        ax1.set_ylim([-5-0.5,5+0.5])
        #plt.ylim([400,800])
        ax1.plot(df['G3B Vmon'], df['G3B Imon'], c='b', marker="s", label='G3B', linestyle='-',linewidth=0.5)
        ax1.plot(df['G3T Vmon'], df['G3T Imon'], c='r', marker="d", label='G3T', linestyle='--',linewidth=0.5)
        ax1.plot(df['G2B Vmon'], df['G2B Imon'], c='g', marker="o", label='G2B', linestyle='-.',linewidth=0.5)
        ax1.plot(df['G2T Vmon'], df['G2T Imon'], c='y', marker="v", label='G2T', linestyle=':',linewidth=0.5)
        ax1.plot(df['G1B Vmon'], df['G1B Imon'], c='c', marker="*", label='G1B', linestyle=(0,(5,2,1,2)),linewidth=0.5)
        ax1.plot(df['G1T Vmon'], df['G1T Imon'], c='m', marker="+", label='G1T', linestyle=(1,(1,2,3,4)),linewidth=0.5)
        ax1.plot(df['DRIFT Vmon'], df['DRIFT Imon'], c='k', marker="^", label='DRIFT', linestyle=(2,(2,1,2,1)),linewidth=0.5)

        ax1.text(700, -4, 'CMS GE2/1 Triple-GEM Detector'"\n""Gas = $CO_{2} 100$%",fontsize=18, color='black')#,alpha=0.5)
        hep.cms.text("Preliminary", fontsize=23)
        hep.cms.lumitext('GE21-MODUELE-'+fn2[0].split('_')[1]+'-'+fn2[0].split('_')[2],fontsize=23)

        ax1.legend(frameon=True)
        ax1.figure.savefig("plots/"+current_path_name_plot+'_'+str(5))
        ax1.figure.savefig("plots_pdf/"+current_path_name_plot+'_'+str(5)+'.pdf')
        #fig.savefig(current_path_name_plot)
        #---plot number2
        fig1 = plt.figure(figsize=(15,12))
        ax1 = fig1.add_subplot(111)

        ax1.set_xlabel('Vmon[V]', fontsize=32)
        ax1.set_ylabel('Imon[$\mu$A]', fontsize=32)
        #ax1.xlim([0,5])
        ax1.set_xlim([0,1100])
        ax1.set_ylim([-50-0.5,50+0.5])
        #plt.ylim([400,800])
        ax1.plot(df['G3B Vmon'], df['G3B Imon'], c='b', marker="s", label='G3B', linestyle='-',linewidth=0.5)
        ax1.plot(df['G3T Vmon'], df['G3T Imon'], c='r', marker="d", label='G3T', linestyle='--',linewidth=0.5)
        ax1.plot(df['G2B Vmon'], df['G2B Imon'], c='g', marker="o", label='G2B', linestyle='-.',linewidth=0.5)
        ax1.plot(df['G2T Vmon'], df['G2T Imon'], c='y', marker="v", label='G2T', linestyle=':',linewidth=0.5)
        ax1.plot(df['G1B Vmon'], df['G1B Imon'], c='c', marker="*", label='G1B', linestyle=(0,(5,2,1,2)),linewidth=0.5)
        ax1.plot(df['G1T Vmon'], df['G1T Imon'], c='m', marker="+", label='G1T', linestyle=(1,(1,2,3,4)),linewidth=0.5)
        ax1.plot(df['DRIFT Vmon'], df['DRIFT Imon'], c='k', marker="^", label='DRIFT', linestyle=(2,(2,1,2,1)),linewidth=0.5)
        
        ax1.text(700, -40, 'CMS GE2/1 Triple-GEM Detector'"\n""Gas = $CO_{2} 100$%",fontsize=18, color='black')#,alpha=0.5)
        hep.cms.text("Preliminary", fontsize=23)
        hep.cms.lumitext('GE21-MODUELE-'+fn2[0].split('_')[1]+'-'+fn2[0].split('_')[2],fontsize=23)
        
        ax1.legend(frameon=True)
        ax1.figure.savefig("plots/"+current_path_name_plot+'_'+str(50))
        ax1.figure.savefig("plots_pdf/"+current_path_name_plot+'_'+str(50)+'.pdf')
        #fig.savefig(current_path_name_plot)
        #---plot number3
        fig2 = plt.figure(figsize=(15,12))
        ax1 = fig2.add_subplot(111)

        ax1.set_xlabel('Vmon[V]', fontsize=32)
        ax1.set_ylabel('Imon[$\mu$A]', fontsize=32)
        #ax1.xlim([0,5])
        ax1.set_xlim([0,1100])
        ax1.set_ylim([-150-0.5,150+0.5])
        #plt.ylim([400,800])
        ax1.plot(df['G3B Vmon'], df['G3B Imon'], c='b', marker="s", label='G3B', linestyle='-',linewidth=0.5)
        ax1.plot(df['G3T Vmon'], df['G3T Imon'], c='r', marker="d", label='G3T', linestyle='--',linewidth=0.5)
        ax1.plot(df['G2B Vmon'], df['G2B Imon'], c='g', marker="o", label='G2B', linestyle='-.',linewidth=0.5)
        ax1.plot(df['G2T Vmon'], df['G2T Imon'], c='y', marker="v", label='G2T', linestyle=':',linewidth=0.5)
        ax1.plot(df['G1B Vmon'], df['G1B Imon'], c='c', marker="*", label='G1B', linestyle=(0,(5,2,1,2)),linewidth=0.5)
        ax1.plot(df['G1T Vmon'], df['G1T Imon'], c='m', marker="+", label='G1T', linestyle=(1,(1,2,3,4)),linewidth=0.5)
        ax1.plot(df['DRIFT Vmon'], df['DRIFT Imon'], c='k', marker="^", label='DRIFT', linestyle=(2,(2,1,2,1)),linewidth=0.5)

        ax1.text(700, -120, 'CMS GE2/1 Triple-GEM Detector'"\n""Gas = $CO_{2} 100$%",fontsize=18, color='black')#,alpha=0.5)
        hep.cms.text("Preliminary", fontsize=23)
        hep.cms.lumitext('GE21-MODUELE-'+fn2[0].split('_')[1]+'-'+fn2[0].split('_')[2],fontsize=23)

        ax1.legend(frameon=True)
        ax1.figure.savefig("plots/"+current_path_name_plot+'_'+str(150))
        ax1.figure.savefig("plots_pdf/"+current_path_name_plot+'_'+str(150)+'.pdf')
        #fig.savefig(current_path_name_plot)
    else:
        print("ERROR: The file doesn't exist") 