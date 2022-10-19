#import module numpy
import numpy as np

#deklarasi variabel 
inputs = [[3.0, 0.4, 4.0, 0.5, 5.0, 9.0],
          [7.0, 8.0, 9.0, 2.9, 2.9, 9.8],
          [8.0, 2.4, 2.9, 1.7, 1.8, 6.7],
          [1.8, 1.9, 2.7, 0.8, 2.8, 4.3],
          [0.7, 0.2, 0.1, 4.0, 9.0, 6.3]]

#deklarasi bobot per neuron
weights = [[0.3, 2.1, 1.2, 1.1, 1.7, 9.0],
           [5.0, 8.0, 6.0, 4.0, 2.9, 8.9],
           [0.5, 1.9, 1.7, 2.4, 1.8, 7.6],
           [3.0, 1.8, 2.4, 8.0, 1.6, 3.4],
           [1.6, 2.7, 0.2, 1.8, 3.0, 3.6]]

#deklarasi bias per neuron
bias = [1.1, 3.1, 9.5, 4.4, 5.9]

#display output dengan menggunkan bantuan module numpy
display_outputs = np.dot(inputs, np.array(weights).T) + bias

#print ouputs
print(display_outputs)

#develop @mahendrarendi
