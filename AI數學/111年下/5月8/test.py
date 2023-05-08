import numpy as np
import cv2

def show_compare_image(original_Img, new_Img):
    cv2.imshow("ROC_rule_China",original_Img)
    cv2.imshow("ROC",new_Img)

def main():
    M = np.array([[1, 0, 200], [ 0, 1, 0]], dtype=float)
    img= cv2.imread( 'ROC_rule_China.jpg' )
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dsize = img.shape[:2] [::-1]
    newImg = cv2.warpAffine( img, M, dsize, borderValue=(255, 255, 255))
    show_compare_image(img, newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows ()
    cv2.waitKey (1)

if __name__=='__main__':
    main()