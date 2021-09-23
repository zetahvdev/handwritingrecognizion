import button_pos_script as btp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time

# Takes the raw events and reduces its size to fit training
def shrink(event):
    as_pd = pd.DataFrame(event)
    uniques = as_pd.drop_duplicates()
    
    return np.array(uniques)

def ev_tovec(datax, show_graph=True, shrink_data=True):
    
    stringvec = {"left and up": [1, 0, 0, 0, 0, 0, 0, 0, 0],
"left and straight": [0, 1, 0, 0, 0, 0, 0, 0, 0],
"left and down": [0, 0, 1, 0, 0, 0, 0, 0, 0],
"straight and up": [0, 0, 0, 1, 0, 0, 0, 0, 0],
"no movement": [0, 0, 0, 0, 1, 0, 0, 0, 0],
"straight and down": [0, 0, 0, 0, 0, 1, 0, 0, 0],
"right and up": [0, 0, 0, 0, 0, 0, 1, 0, 0],
"right and straight": [0, 0, 0, 0, 0, 0, 0, 1, 0],
"right and down": [0, 0, 0, 0, 0, 0, 0, 0, 1]}

    if shrink_data:
        datax = shrink(datax)
    
    
    if show_graph:
        plot_events(datax)
        ax = plt.gca()
        ax.invert_yaxis()
    
    li = []
    li_degree = []
    
    for i in range(1, len(datax)):
        diff = datax[i] - datax[i-1]
        deg = np.arctan2(diff[1], diff[0]) * 180 / np.pi
        distance = np.linalg.norm(datax[i] - datax[i-1])
        
        li_degree.append([deg, distance])
        
        if (datax[i] == [0, 0]).all():
            li.append(stringvec["no movement"])
            continue
        
        if (np.sign(datax[i] - datax[i-1]) == [-1, -1]).all():
            li.append(stringvec["left and up"])
        elif (np.sign(datax[i] - datax[i-1]) == [-1, 0]).all():
            li.append(stringvec["left and straight"])
        elif (np.sign(datax[i] - datax[i-1]) == [-1, 1]).all():
            li.append(stringvec["left and down"])
        elif (np.sign(datax[i] - datax[i-1]) == [0, -1]).all():
            li.append(stringvec["straight and up"])
        elif (np.sign(datax[i] - datax[i-1]) == [0, 0]).all():
            li.append(stringvec["no movement"])
        elif (np.sign(datax[i] - datax[i-1]) == [0, 1]).all():
            li.append(stringvec["straight and down"])
        elif (np.sign(datax[i] - datax[i-1]) == [1, -1]).all():
            li.append(stringvec["right and up"])
        elif (np.sign(datax[i] - datax[i-1]) == [1, 0]).all():
            li.append(stringvec["right and straight"])
        elif (np.sign(datax[i] - datax[i-1]) == [1, 1]).all():
            li.append(stringvec["right and down"])
        
    return np.array(li), np.array(li_degree)


vec_num = {0: [1, 0, 0, 0, 0, 0, 0, 0, 0],
1: [0, 1, 0, 0, 0, 0, 0, 0, 0],
2: [0, 0, 1, 0, 0, 0, 0, 0, 0],
3: [0, 0, 0, 1, 0, 0, 0, 0, 0],
4: [0, 0, 0, 0, 1, 0, 0, 0, 0],
5: [0, 0, 0, 0, 0, 1, 0, 0, 0],
6: [0, 0, 0, 0, 0, 0, 1, 0, 0],
7: [0, 0, 0, 0, 0, 0, 0, 1, 0],
8: [0, 0, 0, 0, 0, 0, 0, 0, 1]}

def print_time(func):

    def wrapper(*args, **kwargs):
        seconds = 1
        start = time.time() * seconds
        func(*args, **kwargs)
        print(f"time taken: {time.time() * seconds - start}")
        return func(*args, **kwargs)
        
    return wrapper


def to_scalar(array):
    map_list = vec_num

    map_vals = list(map_list.values())
    index = map_vals.index(list(array))

    return(index)

# @print_time
def compute_conversion(arr):
    return np.array([to_scalar(n) for n in arr])


color_mapping = {0: 'blue',
                 1: 'red',
                 2: 'gray',
                 3: 'green',
                 4: 'yellow',
                 5: 'black',
                 6: 'purple',
                 7: 'magenta',
                 8: 'cyan'}

def plot_events(event, color_pattern = []):
    if color_pattern == []:
        plt.plot(event.T[0], event.T[1])
        return
    
    count_lines = 0
    for i in range(len(event-1)):
        j = i * 1
        if j + 2 > len(event):
            break
        plt.plot(event.T[0][j:j+2], event.T[1][j:j+2], str(color_pattern[i]))
        count_lines = i
    
    print(count_lines)

def avg_non_4(test):
    li = []
    
    for i in range(len(test)):
        vec = ev_tovec(test[i])
        comp = compute_conversion(vec)
        li.append(comp[comp != 4].shape[0])
    
    return np.array(li)

def get_nextpos(coord, pos):
        print(coord)
        print(np.sin(pos[0] * np.pi / 180))
        next_pos = coord + [0, np.sin(pos[0] * np.pi / 180) * pos[1]]
        next_pos = next_pos + [np.cos(pos[0] * np.pi / 180) * pos[1], 0]
        print(next_pos)


