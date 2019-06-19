import numpy as np
import math
from skimage.transform import resize
import scipy.ndimage
import warnings
warnings.filterwarnings('ignore')

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

# Downsample using order 8 Chebyshev type I filter
def downsample(data):
    return scipy.signal.decimate(data, 6, axis = 0)

def calGRF(data):
    tme, height, breadth = len(data), len(data[0]), len(data[0][1])
    grf = data.copy()
    #grf = np.abs(data).copy()    
    for t in range(1, tme):
        for h in range(height):
            for b in range(breadth):
                grf[t][h][b]+=grf[t-1][h][b]    
    return grf

def cal_theta(img):
    img = np.sum(img,axis=0)
    img = resize(img, (450, 300))
    x1, y1 = max_index_in_range(img, 0, len(img)//2)
    x2, y2 = max_index_in_range(img, len(img)//2, len(img))
    dx = (x1 + x2) / 2 - len(img) / 2
    dy = (y1 + y2) / 2 - len(img[0]) / 2
    theta = (math.atan2(y2 - y1, x2 - x1) * 180) / math.pi
    return (theta,dx,dy)

def max_index_in_range(arr, start_i, end_i):
    x, y, m = start_i, 0, len(arr[0])
    for i in range(start_i, end_i):
        for j in range(m):
            if(abs(arr[i][j]) > abs(arr[x][y])):
                x, y = i, j
    return (x, y)

def rotate_image(img,theta):
    return scipy.ndimage.rotate(img, -theta, reshape=True)

def shift_image(img,dx,dy):    
    return scipy.ndimage.shift(img, (-dx, -dy))

def process_foot(data):
    Tmax = 1600
    data = data[:Tmax]    
    grf = calGRF(data)
    #grf = calGRF(grf)
    theta,dx,dy = cal_theta(grf)
    temporal = downsample(grf)[50:150]
    new_temporal = np.zeros(shape=[temporal.shape[0],450,300])
    for i in range(len(temporal)):
        frame = temporal[i]
        scaled = resize(frame, (450, 300))
        rotated = rotate_image(scaled,theta)
        shifted = shift_image(rotated,dx,dy)
        processed = scipy.ndimage.gaussian_filter(shifted, sigma = 14)
        processed = resize(processed, (450, 300))
        new_temporal[i] = processed
    return new_temporal    

def process_matlab(mat):
    dataL, dataR = prepare_data(mat)
    footL, footR = process_foot(dataL), process_foot(dataR)
    processed = np.append(footL, footR, axis = 2)
    processed_frames = np.empty([processed.shape[0],88,88])
    for i in range(len(processed)):
        frame = processed[i]
        frame /= np.max(np.abs(frame))
        processed_frames[i] = resize(frame, (88, 88))
    return processed_frames
