import numpy as np
import button_pos_script as btp

def sequence(m, n):
    li = []
    for i in range(len(m)-n+1):
        li.append(m[i:i+n])
    return np.array(li)

def get_trainy(trainx):
    li = []
    
    # [-1, -1] : 0
    # [-1, 0] : 1
    # [-1, 1] : 2
    # [0, -1] : 3
    # [0, 0] : 4
    # [0, 1] : 5
    # [1, -1] : 6
    # [1, 0] : 7
    # [1, 1] : 8
    
    for i in range(len(trainx) - 1):
        i += 1
        
        if (trainx[i][0] == [0, 0]).all():
            li.append(4)
            continue
        
        if (np.sign(trainx[i][0] - trainx[i][-1]) == [-1, -1]).all():
            li.append(0)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [-1, 0]).all():
            li.append(1)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [-1, 1]).all():
            li.append(2)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [0, -1]).all():
            li.append(3)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [0, 0]).all():
            li.append(4)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [0, 1]).all():
            li.append(5)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [1, -1]).all():
            li.append(6)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [1, 0]).all():
            li.append(7)
        elif (np.sign(trainx[i][0] - trainx[i][-1]) == [1, 1]).all():
            li.append(8)
    # if (np.sign(posty[1][0] - posty[-1][0]) == [-1, 1]).all():
    #    print("works")