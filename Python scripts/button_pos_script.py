import keyboard as kb
import mouse as ms
import numpy as np
import pandas as pd
import time
import csv
import event_process as epr
import transform_data as trs
import matplotlib.pyplot as plt

max_len = 200

# Converts events from DataFrame to Numpy
def pd_events_to_np(pd_events):
    count_events = int(len(pd_events.columns) / 2)
    return np.asarray(pd_events).transpose(1, 0).reshape(2, count_events, len(pd_events)).transpose(1, 2, 0)
    
# Loads events from file to numpy
def load_event(file):
    return pd_events_to_np(pd.read_csv(file))

def insertTo(arr, insert):
	for i in range(len(insert)):
		arr[i] = insert[i]
	return np.copy(arr)

# Records all the movement of your mouse in a event object to be used into training machine learning
def ms_events():
    # Where all the total events are recorded
    mouse = []
    # Where all onclick events are recorded
    mouse_events = []

    # Block function for input responses
    while True:
        # max size of the onclick events
        arr = np.zeros((max_len, 2), dtype=np.int32)
        # If finished, press "esc" key.
        if kb.is_pressed('esc'):
            return np.array(mouse_events)

        # When holding left click, record all mouse coordinates
        counter = 0
        last_pos = None
        
        # timeout_handler()
        while ms.is_pressed(button='left') and counter < max_len:
            last_pos = ms.get_position() if last_pos is None else last_pos
            pos = ms.get_position()
            # add another condition layer:
            if pos[0] != last_pos[0] or pos[1] != last_pos[1]:
                mouse.append(ms.get_position())
                last_pos = pos
            
            counter += 1
            time.sleep(0.001)
        
        # Saves recording session
        if mouse != []:
            event = insertTo(arr, list(mouse))
            mouse_events.append(event)
            mouse = []
 
def save_events(events, filename):
    column_len = events.shape[0] * events.shape[2]

    # Converts into a 2-D dimensional array
    ev_reshape = events.transpose(2, 0, 1).reshape(column_len, -1).transpose(1, 0)
    with open(filename + '.csv', 'w') as f:
        datawriter = csv.writer(f)
	# Mouse Events header
        datawriter.writerow(range(column_len))
        for row in ev_reshape:
            datawriter.writerow(list(row))
            

def test_ai():
    while True:
        if kb.is_pressed('esc'):
            return "Finished"
        while kb.is_pressed('space'):
            ms.move(ms.get_position()[0] + 1, ms.get_position()[1])
            ms.click()
            time.sleep(0.01)

def testPos():
    while True:
        if kb.is_pressed('esc'):
            return "done"
        while ms.is_pressed(button='left'):
            print(ms.get_position())
            
def ev_stack(*args):
    return np.concatenate(args)

def to_origin(event):
    smallest_x = np.min(event.T[0][event.T[0] > 0])
    smallest_y = np.min(event.T[1][event.T[1] > 0])
    post = event - [smallest_x, smallest_y]
    return np.where(post >= 0, post, 0)

