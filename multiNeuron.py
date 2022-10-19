#import module numpy
import numpy as np

#deklarasi variabel
inputs = [3.0, 8.0, 2.0, 9.0, 4.0, 1.0, 7.0, 5.0, 6.0, 10.0]

#deklarasi bobot per neuron
weights = [[1.2, -3.4, 0.6, 1.8, 2.9, -1.2, 1.3, 2.3, 3.5, -1.4],
           [0.11, 0.14, 0.19, 2.2, 0.8, 3.3, -0.4, 0.22, 1.69, 1.49],
           [3.34, -0.6, 1.7, 0.13, 0.14, -1.29, -3.46, 0.67, 1.86, -1.11],
           [5.0, 1.39, 4.24, 2.3, 2.2, 4.79, 8.76, -2.75, 0.35, 5.22],
           [9.9, -0.32, 0.44, 0.87, -3.33, -2.65, 7.5, -5.19, 2.36, -2.59]]

# deklarasi bias per neuron
bias = [1.5, 2.5, 3.5, 6.5, 5.5]

#tampilkan dengan menggunakan bantuan module numpy
display_outputs = np.dot(weights, inputs) + bias

#print output
print(display_outputs)
