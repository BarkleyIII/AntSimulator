from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#initialize paramenter here
plt.rcParams["figure.figsize"] = (12,10)
plt.rcParams["axes.labelsize"] = 16
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
mal_frac = str(("%.6f" % (2**-10)))
hell_evpr_multi = str(1000)
iteration = str(0)
filename = "AntSimData_SIM_STEPS-50000_SIM_ITERS-20_mal_frac-"+mal_frac+"_mal_delay-100_mal_ants_focus-1_ant_tracing-1_ctr_pherm-0_hell_phermn_intens-1.000000_hell_phermn_evpr-"+hell_evpr_multi+".000000_dil_max-1000_dil_incr-1000_iter-"+iteration+".csv"
foldername = "./data_recreate_no_defense_max_dil_min_inc_8/"
data = pd.read_csv(foldername+filename,header=None).T
data = np.array(data)
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)
par1 = host.twinx()
plt.yscale('log')
par1.set_yscale('log')
par1.axis["right"].toggle(all=True)
#define which one will get plot
l1,l2 = host.plot(data[0:2].T) #this is the left axis data
l3,l4 = par1.plot(100*data[2:4].T) #this is the right axis data, multiply by 100 to make it percentage.
#change the style of line here
plt.setp(l2,linestyle='--', linewidth=2)
plt.setp(l3, linestyle=':', linewidth=2)
plt.setp(l4, linestyle='-.', linewidth=2)
host.set_ylim(0.001, 100) #set y range from 10^-3 to 10^2
par1.set_ylim(0.001, 100) #set y range from 10^-3 to 10^2
plt.xlabel('Percentage of Simulation completed') #x axis
plt.ylabel('Food bits per ants', fontsize=20) #left axis
par1.set_ylabel("Percentage of cooperators", fontsize=20) #right axis
par1.legend()
host.legend([l1,l2],['Food bits per ant collected from source','Food bits per ant delivered food to nest'], loc='upper left') #change legends here for left data
par1.legend([l3,l4],['Successful collectors', 'Successful deliverers'], loc='upper right')  #change legends here for right data
plt.savefig(foldername+"graphs/"+filename+".png",dpi = 400, facecolor=host.get_facecolor())
#plt.savefig(foldername+"graphs/1.png",dpi = 400, facecolor=host.get_facecolor()) #modified for windows, need to change back
