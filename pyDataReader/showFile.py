from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import glob
import sys

from PIL import Image

import numpy as np

def readShowFile(dir_file):
  
  im = Image.open(dir_file)

  im.show()
  
  im_array = np.array(im)
  
  print(im_array.shape)  
  
  im_array1 = im_array.reshape([-1,20,20])
  im_array1 = im_array.reshape([-1])
  
  print(im_array1.shape)
  
  return True

if __name__ == '__main__':
    readShowFile(sys.argv[1])