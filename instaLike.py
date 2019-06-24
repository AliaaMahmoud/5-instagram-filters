import cv2
import numpy as np

# filters are: 1.Inkwell 2.Toaster 3.1977 4.Stinson 5.Sutro 

def alpha_blend(frame_1, frame_2, mask):
    alpha = mask/255.0 
    blended = cv2.convertScaleAbs(frame_1*(1-alpha) + frame_2*alpha)
    return blended

def toaster(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    frame_h, frame_w, frame_c = img.shape
    y = int(frame_h/2)
    x = int(frame_w/2)
    mask = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    cv2.circle(mask, (x, y), int((y/2)*1.7), (255,255,255), -1, cv2.LINE_AA)
    mask = cv2.GaussianBlur(mask, (45,45),50 )
    blured = img
    blue = 10
    green = 80
    red = 90
    intensity = 0.8
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, blured, 1.0, 0, blured)
    hsv2 = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
    value2 = 20
    value3 = hsv2[...,2]
    hsv2[...,2]=np.where((255-value3)<value2,255,value3-value2)
    blured = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
    blured = cv2.cvtColor(blured, cv2.COLOR_BGR2BGRA)
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)
    hsvImg2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    value = 13
    vValue = hsvImg2[...,2]
    hsvImg2[...,2]=np.where((255-vValue)<value,255,vValue+value)
    img = cv2.cvtColor(hsvImg2, cv2.COLOR_HSV2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    blue2 = 10
    green2 = 50
    red2 = 150
    intensity2 = 0.1
    sepia_bgra = (blue2, green2, red2, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity2, img, 1.0, 0, img)
    blended = alpha_blend(img, blured, 255-mask)
    frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    cv2.imshow("Toaster",frame)


def f_1977(img):
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsvImg[:,:,2] = [[max(pixel - 25, 0) if pixel < 255 else min(pixel + 25, 255) for pixel in row] for row in hsvImg[:,:,2]]
    hsvImg[...,2] = hsvImg[...,2]*0.7
    img = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    blue = 30
    green = 90
    red = 230
    intensity = 0.2
    frame_h, frame_w, frame_c = img.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, img, 1.0, 0, img)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imshow("1977",img)
    

def stinson(img):
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsvImg[:,:,2] = [[max(pixel - 25, 0) if pixel < 250 else min(pixel + 25, 255) for pixel in row] for row in hsvImg[:,:,2]]
    hsvImg[...,2] = hsvImg[...,2]*0.8
    img = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    blue = 25
    green = 60
    red = 100
    intensity = 0.5
    frame_h, frame_w, frame_c = img.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, img, 1.0, 0, img)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imshow("Stinson",img)
    
def sutro(img): 
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsvImg[:,:,2] = [[max(pixel - 50, 0) if pixel < 255 else min(pixel + 50, 255) for pixel in row] for row in hsvImg[:,:,2]]
    hsvImg[...,2] = hsvImg[...,2]*0.7
    img = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    frame_h, frame_w, frame_c = img.shape
    y = int(frame_h/2)
    x = int(frame_w/2)
    mask = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    cv2.circle(mask, (x, y), int((y/2)*1.7), (255,255,255), -1, cv2.LINE_AA)
    mask = cv2.GaussianBlur(mask, (45,45),50 )
    blured = img
    blue = 10
    green = 10
    red = 80
    intensity = 0.4
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, blured, 1.0, 0, blured)
    hsv2 = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
    value2 = 20
    value3 = hsv2[...,2]
    hsv2[...,2]=np.where((255-value3)<value2,255,value3-value2)
    blured = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
    blured = cv2.cvtColor(blured, cv2.COLOR_BGR2BGRA)
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)
    hsvImg2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    value = 1
    vValue = hsvImg2[...,2]
    hsvImg2[...,2]=np.where((255-vValue)<value,255,vValue+value)
    img = cv2.cvtColor(hsvImg2, cv2.COLOR_HSV2BGR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    blue2 = 60
    green2 = 60
    red2 = 40
    intensity2 = 0.1
    sepia_bgra = (blue2, green2, red2, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity2, img, 1.0, 0, img)
    blended = alpha_blend(img, blured, 255-mask)
    frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    cv2.imshow("sutro",frame)



def instalike(img,filter_name):
    if filter_name == 'Inkwell':       
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Inkwell",gray)
    elif filter_name == 'Toaster':
        toaster(img)
    elif filter_name == '1977':
        f_1977(img)
    elif filter_name == 'Stinson':
        stinson(img)
    elif filter_name == 'Sutro':
        sutro(img)
    else: 
        cv2.imshow("Original",img)



img_add = input('Enter Image Name:')
# img_add = 'img.jpg'
filter_name = input('Enter Filter Name:')
img = cv2.imread(img_add,1)

instalike(img, filter_name)
cv2.waitKey()
