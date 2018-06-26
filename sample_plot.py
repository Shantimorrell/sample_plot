import numpy as np
import matplotlib.pyplot as plt

fileName = '/home/luroot/sample_plot/sample_data.txt'       #sets location for data file

#reads and prints the data in the data file
file = open(fileName, 'r')
text = file.read()
print(text)

rows = text.split('\n')
'''for n in rows:
    for character in len(n):
    '''
print(rows)

'''
xvals = np.arange(-5, 5, 1)
yvals = np.arange(-10, 10, 2)
plt.plot(xvals, yvals)
plt.show()
'''

'''
plt.plot([1, 2, 3, 4])                              #line plot with specified y-coordinates and cooresponding default x-coordinates [0, 1, 2, 3]
plt.ylabel('some numbers')                          #labels y-axis
plt.show()                                          #displays plot
plt.scatter([1, 2, 3, 4], [1, 2, 3, 4])             #scatter plot with the parameters (x-values, y-values)
plt.show()                                          #displays plot
'''
