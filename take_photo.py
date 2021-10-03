# import the opencv library
import cv2
from datetime import datetime
import time
import copy
import os

SUB_FOLDER = 'single_hand'
FOLDER = './dataset_check_mp/'+SUB_FOLDER
USE_COUNTER = False
INTERVAL_SEC = 2

def draw_text(image, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (100, 100)
    fontScale = 1
    color = (0, 255, 255)
    thickness = 2
    image = cv2.putText(image, text, org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    return image
class MyCounter:
    def __init__(self, interval_sec):
        self.start = time.time()
        self.interval_sec = interval_sec
        self.is_active = False
    def turn_off(self):
        self.is_active = False
    def is_timeout(self):
        now = time.time()
        if now - self.start > self.interval_sec and self.is_active:
            self.turn_off()
            return True
        else:
            return False
    def start_count(self):
        self.start = time.time()
        # turn on
        self.is_active = True

class MyText:
    def __init__(self, init_text='hello'):
        self.init_text = init_text
        self.text = self.init_text
        self.t0 = time.time()
    def set_text(self, text):
        self.t0 = time.time()
        self.text = text
    def check_timeout(self):
        now = time.time()
        if now - self.t0 > 1:
            self.text = self.init_text
if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)
vid = cv2.VideoCapture(0)
my_text = MyText(FOLDER)
counter = MyCounter(INTERVAL_SEC)
count = 0
while True:
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    ori_frame = copy.deepcopy(frame)

    # Display the resulting frame
    my_text.check_timeout()
    frame = draw_text(frame, my_text.text)
    cv2.imshow('frame', frame)

    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    key = cv2.waitKey(1)
    # print('key pressed', key)
    if key == ord('a'):
        break
    if key == ord('b') and USE_COUNTER:
        # start counter
        counter.start_count()
        
    # for using counter
    if USE_COUNTER:
        if counter.is_timeout():
            key = 32 # take photo

    if key == 32: # spacebar
        # take photo
        now = datetime.now()
        name = now.strftime("%m%d%YT%H%M%S")
        count += 1
        cv2.imwrite('%s/%s%d.jpg'%(FOLDER,name, count), ori_frame)
        my_text.set_text('%d %s/%s%d.jpg'%(count,FOLDER, name, count))
    

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

