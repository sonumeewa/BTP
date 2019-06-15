import numpy as np
import math
from skimage.transform import resize
import scipy.ndimage

def foot_reshape(arr):
    # 88 + 3 zeros = 91 which is reshaped to 13 x 7
    arr = np.append(arr, np.zeros((arr.shape[0], 3)), axis = 1)    
    return np.reshape(arr, (arr.shape[0], 13, 7))

def prepare_data(mat):
    # Left footstep
    dataL = foot_reshape(mat['dataL'])
    # Right footstep
    dataR = foot_reshape(mat['dataR'])    
    return (dataL, dataR)

def calGRF(data):
    tme, height, breadth = len(data), len(data[0]), len(data[0][1])
    grf = data.copy()
    #grf = np.abs(data).copy()    
    for t in range(1, tme):
        for h in range(height):
            for b in range(breadth):
                grf[t][h][b]+=grf[t-1][h][b]    
    return grf

def max_index_in_range(arr, start_i, end_i):
    x, y, m = start_i, 0, len(arr[0])
    for i in range(start_i, end_i):
        for j in range(m):
            if(abs(arr[i][j]) > abs(arr[x][y])):
                x, y = i, j
    return (x, y)

def rotate_image(img):
    x1, y1 = max_index_in_range(img, 0, len(img)//2)
    x2, y2 = max_index_in_range(img, len(img)//2, len(img))
    theta = (math.atan2(y2 - y1, x2 - x1) * 180) / math.pi
    return scipy.ndimage.rotate(img, -theta, reshape=True)

def shift_image(img):
    x1, y1 = max_index_in_range(img, 0, len(img)//2)
    x2, y2 = max_index_in_range(img, len(img)//2, len(img))
    dx = (x1 + x2) / 2 - len(img) / 2
    dy = (y1 + y2) / 2 - len(img[0]) / 2    
    return scipy.ndimage.shift(img, (-dx, -dy))

def process_foot(data):
    Tmax = 1600
    data = data[:Tmax]    
    grf = calGRF(data)
    spatial = np.sum(grf, axis = 0)
    scaled_spatial = resize(spatial, (450, 300))
    rotated = rotate_image(scaled_spatial)
    shifted = shift_image(rotated)
    processed = scipy.ndimage.gaussian_filter(shifted, sigma = 14)
    processed = resize(processed, (450, 300))
    return processed    

def process_matlab(mat):
    dataL, dataR = prepare_data(mat)
    footL, footR = process_foot(dataL), process_foot(dataR)    
    processed = np.append(footL, footR, axis = 1)
    processed /= np.max(np.abs(processed))
    processed = resize(processed, (88, 88))
    return processed
