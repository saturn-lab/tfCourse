from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import glob
import sys

def readFileFromDir(dir_in):

  if not os.path.exists(dir_in):
    raise(ValueError(dir_in + ' does not exist'))
  
  dirs = os.listdir(dir_in)
  
  print(dirs)
  
  for d in dirs:
    d = os.path.join(dir_in, d)
    if os.path.isfile(d):
      continue
    
    images = glob.glob(os.path.join(d, '*.*'))
    if (len(images) < 20) or (len(images) > 24):
        continue
    
    for image in images:
	
      fname = os.path.basename(image)
      print(fname)
      fname = fname.split('.')
	
      if len(fname) != 2:
        return False

      fname = fname[0]
      fname1= fname[1]
      fname2= fname[2]      
      print(fname)
      print(fname1)
      print(fname2)
      
      fname = fname.split('_')
      fname = fname[len(fname) - 1]

      print(fname)
	  
  return True

def parseName(filename): # ./xx/yy/10000_12.wav
    filename = filename.split(os.sep)
    filename = filename[len(filename) - 1]
    filename = filename.split('.')[0]
    filename = filename.split('_')
    filename = filename[len(filename) - 1]
    print(filename[0])

if __name__ == '__main__':
    readFileFromDir(sys.argv[1])
