import datetime
import picamera
import time
import sys

pic_filename = '{:%Y-%m-%dT%H-%M-%S}.img'.format(datetime.datetime.now())
print('%s' % pic_filename)
#sys.exit(0)

with picamera.PiCamera() as camera:
  camera.start_preview()
  time.sleep(5)
  pic_filename = '{:%Y-%m-%dT%H-%M-%S}.img'.format(datetime.datetime.now())
  camera.capture(pic_filename)
  time.sleep(2)
  camera.stop_preview()
  
  