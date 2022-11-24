import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep 
import glob
hep.style.use(hep.style.ROOT)

fn2 = glob.glob("*stress*.txt")
split_name_stress = fn2[0].split('.txt')
chamber_name_stress= split_name_stress[0]



def plot_discharge(chamberName):

    chamber_name = chamberName
    current_path_name=str(chamber_name)+'.txt'   
    current_path_name_plot=str(chamber_name.split('_20')[0])
    print(current_path_name)
    
    df = pd.read_csv(current_path_name, delimiter='\t')
    df.reset_index(inplace=True, col_level=0)
    df.columns=['counts','Time']
    df.drop(0, axis=0, inplace=True)
    df.Time = df.Time.astype('float')
    df['Time_trunc']=np.trunc(df['Time'].values).astype('float')
    df['counts']= df.counts.astype('float')

    counts = []

    try:
        counts.append(df[df['Time_trunc']==0].iloc[-1][0])
    except:
        counts.append(0) 
    
    try:
        counts.append(df[df['Time_trunc']==1].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==2].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==3].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==4].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==5].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==6].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==7].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==8].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==9].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==10].iloc[-1][0])
    except:
        counts.append(0)

    try:
        counts.append(df[df['Time_trunc']==11].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==12].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==13].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==14].iloc[-1][0])
    except:
        counts.append(0)
        
    try:
        counts.append(df[df['Time_trunc']==15].iloc[-1][0])
    except:
        counts.append(0)
    
    
    x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    counts= pd.Series(counts)
    no_zeros = counts[counts!=0]

    for i in range(len(no_zeros)-1):
        no_zeros.iloc[i+1]= no_zeros.iloc[i+1]-no_zeros.iloc[i] 

    counts.iloc[no_zeros.index] = no_zeros

    plt.bar(x, counts)
    plt.xticks(x)
    plt.yticks(range(int(np.max(counts)+1)))
    plt.ylabel('Number of discharges')
    plt.xlabel('Time[h]')
    plt.text(7, np.max(counts)-0.5, 'CMS GE2/1 Triple-GEM Detector'"\n""Gas = $CO_{2} 100$% ",fontsize=18, color='black')#,alpha=0.5)
    hep.cms.text("Preliminary", fontsize=21)
    hep.cms.lumitext('GE21-MODUELE-'+fn2[0].split('_')[1]+'-'+fn2[0].split('_')[2],fontsize=21)
    
    plt.savefig("plots/"+current_path_name_plot)
    plt.savefig("plots_pdf/"+current_path_name_plot+".pdf")
    #plt.show()