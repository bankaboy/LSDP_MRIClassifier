import numpy as np 
import cv2

f = open('binary_brain','rb')
image_bytes = f.read()
f.close()

recovered_image = np.frombuffer(image_bytes,dtype='uint8').reshape(512,512,3)
print(recovered_image.dtype)
print(recovered_image.shape)

cv2.imshow('after bytes',recovered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()