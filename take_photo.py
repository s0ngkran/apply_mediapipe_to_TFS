# import the opencv library
import cv2
from datetime import datetime
import time
import copy
import os

SUB_FOLDER = 'example'
FOLDER = './dataset_for_mp_testing/'+SUB_FOLDER
DO_RECT = True

####### hand keypoint labeling
#   D F H 
#   E G I J
# C   K
#   B
#    A
   
USE_COUNTER = True
INTERVAL_SEC = 0.5

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
        self.count = 0
    def turn_off(self):
        self.is_active = False
    def is_timeout(self):
        now = time.time()
        if now - self.start > self.interval_sec and self.is_active:
            self.turn_off()
            return True
        else:
            return False
    def start_count(self, delay=0):
        self.count += 1
        self.start = time.time() + delay
        # turn on
        self.is_active = True
    def is_count_out(self, count):
        if self.count > count:
            return True
        return False

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

vid = cv2.VideoCapture(1)
my_text = MyText(FOLDER)
counter = MyCounter(INTERVAL_SEC)
count = 0
# # small rect
# start = 500, 234
# x, y = 870, 454
# end = 870, 454
# y_width = 454-234
# end = 500 +y_width, 454

def do_rect():
    start = ((1280-720)/2)-2, 0
    end = start[0]+ 720, 720

    start = start[0]/2 + 300, start[0] + 20
    end = start[0] +360, start[1] + 360
    start = int(start[0]), int(start[1])
    end = int(end[0]), int(end[1])
    print(start, end)
    print(-start[0]+end[0], -start[1]+end[1])
    return start, end
start,end = (0,0),(1280,720)
if DO_RECT: 
    start, end = do_rect()

while True:
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    ori_frame = copy.deepcopy(frame)

    # Display the resulting frame
    my_text.check_timeout()
    frame = draw_text(frame, my_text.text)
    # draw rect
    frame = cv2.rectangle(frame, start, end, (0,200,100), 3)
    cv2.imshow('frame', frame)


    
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    key = cv2.waitKey(1)
    if key == ord('j'):
        y += 2
    if key == ord('q'):
        x += 2
    # print(x, y)
    # print('key pressed', key)
    if key == ord('a'):
        break

    if key == ord('b') and USE_COUNTER:
        # start counter
        counter.start_count(delay=5) # 5 seconds delay
        
    # for using counter
    if USE_COUNTER:
        if counter.is_timeout():
            key = 32 # take photo

            if counter.is_count_out(30): # take 30 images, then stop
                break
            # take again
            counter.start_count()

    if key == 32: # spacebar
        # take photo
        time.sleep(1)
        now = datetime.now()
        name = now.strftime("%m%d%YT%H%M%S")
        count += 1
        cv2.imwrite('%s/%s%d.jpg'%(FOLDER,name, count), ori_frame[start[1]:end[1],start[0]:end[0]])
        my_text.set_text('%d %s/%s%d.jpg'%(count,FOLDER, name, count))
    

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

