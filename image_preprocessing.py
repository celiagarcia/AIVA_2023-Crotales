'''
AIVA_2023-Crotales
@author: Rebeca Villarraso / Celia Garcia
'''
import cv2

def show_image(txt, image):
    cv2.imshow(txt, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def preprocessing(img_gray):

    #binarizar imagen
    ret, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    show_image('otsu', img_bin)

    '''
    im = cv2.medianBlur(img_gray,5)
    im2= cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((5,5),np.uint8)
    im3=  cv2.dilate(im2, kernel, iterations = 1)
    kernel = np.ones((5,5),np.uint8)
    im4 = cv2.erode(im3, kernel, iterations = 1)
    kernel = np.ones((5,5),np.uint8)
    im5= cv2.morphologyEx(im4, cv2.MORPH_OPEN, kernel)
    im6= cv2.Canny(im5, 100, 200)
    
    '''
    return img_bin