from PIL import Image
import numpy as np

img = Image.open('plan.png').convert('L')

np_img = np.array(img)
np_img = ~np_img  # invert B&W
np_img[np_img > 0] = 1
print(np_img)
np.savetxt('pxl-tobinary.txt', np_img)

import cv2

img = cv2.imread('plan.png',2)
ret, bw_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.imshow("Binary Image", bw_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('plan-in-binary.png', bw_img) 