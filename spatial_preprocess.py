import numpy as np
from skimage.transform import resize
import scipy.ndimage
import math

def foot_reshape(arr):
    # 88 + 3 zeros = 91 which is reshaped to 13 x 7
    arr = np.append(arr, np.zeros((arr.shape[0], 3)), axis = 1)
    
    return np.reshape(arr, (arr.shape[0], 13, 7))

def process_footstep(arr):
    arr = foot_reshape(arr)
    Tmax = 1600

    spatial = arr[:Tmax]

    # Accumulated Pressure gives spatial representation
    spatial = np.add.accumulate(np.abs(spatial), axis = 0)
    spatial = np.sum(spatial, axis = 0)

    # 45 mm x 30 mm
    scaled_spatial_img = resize(spatial, (450, 300))

    # Smoothening using Gaussian filter
    # Doing here only for the purpose of calculating center and rotation angle
    # Will be actually applied on output after translation and rotation
    processed_spatial = scipy.ndimage.gaussian_filter(scaled_spatial_img, sigma = 14)

    front = processed_spatial[:225]
    heel = processed_spatial[225:]

    front_max = np.unravel_index(np.argmax(front), front.shape)

    heel_max = np.unravel_index(np.argmax(heel), heel.shape)
    heel_max = (heel_max[0] + 225, heel_max[1])

    req_center = (processed_spatial.shape[0] / 2, processed_spatial.shape[1] / 2)

    angle = math.atan2(heel_max[0] - front_max[0], heel_max[1] - front_max[1])
    center = ((front_max[0] + heel_max[0])/2, (front_max[1] + heel_max[1])/2)

    dx = center[0] - req_center[0]
    dy = center[1] - req_center[1]
    req_angle = math.pi / 2
    theta = req_angle - angle

    transform_mat = np.array([
        [math.cos(theta), -math.sin(theta), dx],
        [math.sin(theta), math.cos(theta), dy]
    ])

    transformed = scipy.ndimage.affine_transform(scaled_spatial_img, transform_mat, mode='constant')

    transformed = scipy.ndimage.gaussian_filter(transformed, sigma = 14)
    
    transformed = resize(transformed, (88, 44))
    
    return transformed
    
def process_footsteps(mat):
    # Left footstep
    dataL = process_footstep(mat['dataL'])

    # Right footstep
    dataR = process_footstep(mat['dataR'])
    
    spatial = np.append(dataL, dataR, axis = 1)
    
    spatial_max = np.max(spatial)

    # Scale to [0, 1]
    spatial /= spatial_max
    
    return spatial