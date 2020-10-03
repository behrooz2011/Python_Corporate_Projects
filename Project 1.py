

#!/usr/bin/env python3
from PIL import Image
import os
import shutil
import time

print("hellllllo")
dir ='/opt/icons/'
if not os.path.exists(dir):
    os.makedirs(dir)
    print('success')

for file in os.listdir('/home/student-00-05fc48bce2fa/images/'):
 if not file.endswith('DS_Store')and not file.endswith('.py'):

  try:
  #print(file)
   im=Image.open(file).rotate(90).resize((128,128))
   rgb_im=im.convert('RGB')
   file = file+'.jpg'
   rgb_im.save(file)
  except:
   print("Error while saving")
  #print(file)
  #time.sleep(1)
  #print('/home/student-00-05fc48bce2fa/images/'+file)
  if '/home/student-00-05fc48bce2fa/images/'+file not in dir:
   shutil.move('/home/student-00-05fc48bce2fa/images/'+file,dir)

