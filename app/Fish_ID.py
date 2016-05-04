import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

#-------------------------------
# Create directory
#-------------------------------
def create_fish_dir(fn):

  d = os.path.dirname(fn)
  if not os.path.exists(d):
    os.makedirs(d)

#-------------------------------
# Function to process image
#-------------------------------
def process_fish_image(fn):
  img = cv2.imread(fn)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  # Use first image
  n = gray.shape
  a = []
  for i in range(0,n[1]):
    a.append(255-np.mean(gray[:,i]))
  
  i = 0;
  while (a[i] < 1):
    i = i + 1
  
  if(a[i+20] > 10):
    print "Tuna"
    src = fn
    dst = 'Tuna/' + fn
    shutil.move(src,dst)
  else:
    print "Billfish"
    src = fn
    dst = 'Billfish/' + fn
    shutil.move(src,dst)

#----------------------------------------------------------------
#                           Application
#----------------------------------------------------------------


#-------------------------------
# Process all images
#-------------------------------
for i in range(1,21):
  process_fish_image("Fish_ ("+str(i)+").png")


