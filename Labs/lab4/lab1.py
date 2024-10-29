# Name:  
# Email: 
# Date:  September 2024
# Takes elevation data of NYC and displays using the default color map

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')
#Load the array into matplotlib.pyplot:
plt.imshow(elevations)
#Display the plot:
plt.show()

#Unix Notes: 
# mkdir = make directory
# cd = change directory
# pwd = print working directory
# grep string filename(s) = global regular expression printlook for string in the files
# whoami
