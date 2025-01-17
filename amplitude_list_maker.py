import numpy as np



new_amplitude_list = []
new_cantilever_loc = []

np.savez('amplitude_list.npz', amplitude_list=new_amplitude_list, cantilever_loc=new_cantilever_loc)