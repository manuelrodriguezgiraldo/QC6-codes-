
import os
import sys         
  

sys.path.append('/home/manuel/Documents/GE21QC61')        
  
# now we can import mod
import discharge    
  
from short_stability import *
from trip_info import *
from stress_plot import *
from discharge import *
os.makedirs("plots", exist_ok=True)
os.makedirs("plots_pdf", exist_ok=True)

fn1 = glob.glob("*short*.txt")
split_name_short = fn1[1].split('.txt')
chamber_name_short = split_name_short[0]

fn2 = glob.glob("*stress*.txt")
split_name_stress = fn2[0].split('.txt')
chamber_name_stress= split_name_stress[0]

fn3 = glob.glob("*trip-info-night*.txt")
split_name_long = fn3[0].split('.txt')
chamber_name_long= split_name_long[0]

fn4 = glob.glob("*discharge*.txt")
split_name_discharge = fn4[0].split('.txt')
chamber_name_discharge= split_name_discharge[0]

plot_discharge(chamber_name_discharge)
plot_short_stability(chamber_name_short)
plot_stress(chamber_name_stress)
plot_long_stability_trip_info(chamber_name_long)



