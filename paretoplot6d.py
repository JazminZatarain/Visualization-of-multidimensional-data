import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
#import seaborn

# Importing data
data= np.loadtxt('sample_data.txt')

#This part is specific to the data, you can call
#any column of your data.
obj6 = data[:,0]*-1
obj2 = data[:,1]*-1
obj5 = data[:,2]*-1
obj4 = data[:,3]*-1
obj1 = data[:,4]*-1
obj3 = data[:,5]

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

#Marker options:

#Marker styles, in order to use rotation to represent an additional objective 
#it's preferable if the marker  has a single axis of symmetry so that the
#rotation is distinguishable.
pie=r'$\pi$' #Pie Day theme
arrow = u'$\u2193$' # Arrows
clover=r'$\clubsuit$' #Saint Patrick's theme
heart=r'$\heartsuit$' # Valentine's theme
marker=clover

#Colormap obtions: jet, hsv, spectral, to change the color map do cmap= plt.cm.hsv
#To reverse the colormap attach an _r like so:  cmap= plt.cm.hsv_r
rot_angle=180 #rotation multiploer
scale=2000 #size objective multiplier  

#Plotting 6 objectives:
im= ax.scatter(obj1, obj2, obj3, c=obj4, s= obj5*scale, marker=marker, angles=obj6*rot_angle, alpha=1, cmap=plt.cm.Blues)
#Plotting 5 objectives:
#im= ax.scatter(obj1, obj2, obj3, c=obj4, s= obj5*scale, marker=clover, alpha=1, cmap=plt.cm.summer_r)
#Plotting the ideal point:
ax.scatter(1,1,0, marker=pie, c='seagreen', s=scale, alpha=1) 

objs=obj5 #size objective
objr=obj6 #rotation objective

#Main axis labels:
ax.set_xlabel('Objective 1')
ax.set_ylabel('Objective 2')
ax.set_zlabel('Objective 3')

#Axis limits:
plt.xlim([0,1])
plt.ylim([0,1])
ax.set_zlim3d(0, 1)

# set the color limits - not necessary here, but good to know how.
im.set_clim(0.0, 1.0)

#Colorbar label:
cbar = plt.colorbar(im)
cbar.ax.set_ylabel('Objective 4')

#Get artists and labels for legend and chose which ones to display
handles, labels = ax.get_legend_handles_labels()
display = (0,1,2)


#Code for size and rotation legends begins here for Objectives 5 and 6:
#The size min and max may require some scaling to improve visibility,
#But if it is implemented like so, it will keep the size properties
min_size=np.amin(objs)# *3000000 
max_size=np.amax(objs)# *30
markersize=15

#Custom size legend:
size_max = plt.Line2D((0,1),(0,0), color='k', marker=marker, markersize=max_size,linestyle='')
size_min = plt.Line2D((0,1),(0,0), color='k', marker=marker, markersize=min_size,linestyle='')
legend1= ax.legend([handle for i,handle in enumerate(handles) if i in display]+[size_max,size_min],
          [label for i,label in enumerate(labels) if i in display]+["%.2f"%(np.amax(objs)), "%.2f"%(np.amin(objs))], labelspacing=1.5, title='Objective 6', loc=1, frameon=True, numpoints=1, markerscale=1)

#Custom rotation legend
rotation_max = plt.Line2D((0,1),(0,0),color='k',marker=r'$\Uparrow$', markersize=15, linestyle='')
rotation_min = plt.Line2D((0,1),(0,0),color='k', marker=r'$\Downarrow$', markersize=15, linestyle='')
ax.legend([handle for i,handle in enumerate(handles) if i in display]+[rotation_max,rotation_min],
          [label for i,label in enumerate(labels) if i in display]+["%.2f"%(np.amax(objr)), "%.2f"%(np.amin(objr))], labelspacing=1.5, title='Objective 5',loc=2, frameon=True, numpoints=1, markerscale=1)

# This is to plot a second legend:
plt.gca().add_artist(legend1)

plt.show()

# The custom rotation legend shown in lines 79 to 88 will only show an up and down arrow for the largest and lowest objective values
# in order to show the actual rotation in your legend, you can do the following for now: 
#rotation_max = plt.Line2D((0,1),(0,0),color='k', marker=(3,0,np.max(objr)*rot_angle), markersize=markersize, linestyle='')
#rotation_min= plt.Line2D((0,1),(0,0),color='k', marker=(3,0,np.min(objr)*rot_angle), markersize=markersize, linestyle='')
