import tensorflow as tf

from keras.layers import Input, Dense, Conv2D, BatchNormalization, concatenate, MaxPooling2D
from keras.models import Model, Sequential

# This code won't work until Conv2D dimensions are specified

def get_resnet_conv_block(input):
  x = Conv2D()(input)
  x = BatchNormalization(activation='relu')(x)
  x = Conv2D()(x)
  x = BatchNormalization(activation='relu')(x)
  x = Conv2D()(x)
  x = BatchNormalization(activation='relu'(x)
  return x

# ResNet config 1 block
def get_resnet_config_1_block(input):
  x = Conv2D()(input)
  x = BatchNormalization(activation='relu')(x)
  x = MaxPooling2D()(x)
  
  l = get_resnet_conv_block(x)

  r = Conv2D()(x)
  r = BatchNormalization(activation='relu')(r)

  y = keras.layers.add([l, r])

  return y

# ResNet config 2 block
def get_resnet_config_2_block(input):
  x = get_resnet_conv_block(input)

  y = keras.layers.add([input, x])

  return y

# ResNet
def create_res_net():
  input = Input(shape = (13, 7))

  x = Conv2D()(input)
  x = BatchNormalization(activation='relu')(x)

  conv2ay = model_resnet_1()(x)

  x = keras.layers.add([x, conv2ay])

  conv2by = model_resnet_2()(x)

  x = keras.layers.add([x, conv2by])

  conv2cy = model_resnet_2()(x)

  x = keras.layers.add([x, conv2cy])

  No_of_outputs = 10

  y = Dense(No_of_outputs, activation='softmax')(x)

  model_resnet = Model(input, y)

  return model_resnet
