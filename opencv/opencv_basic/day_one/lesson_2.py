import numpy as np
import cv2

"""
    Add two image
"""
img = cv2.imread(r"..\images\cat3.jpg", 1);
imga = cv2.imread(r"..\images\cat4.jpg", 1);
cv2.imshow("anh 1", img)
cv2.waitKey(0)
cv2.imshow("anh 2", imga)
img1 = img[300:900, 600:1200]  # đoạn này là cắt ảnh
img2 = imga[300:900, 600:1200]  # cắt 2 tấm ảnh có cùng kích thước với nhau - có thể khác vị trí nhưng cùng kích thước
img3 = cv2.add(img1, img2)  # lệnh ghép 2 ảnh với nhau - thực hiện phép cộng 2 pixcel
cv2.imshow("anh ghep", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
