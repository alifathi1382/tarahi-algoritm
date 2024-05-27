import numpy as np
import matplotlib.image as mpimg
import matplotlib.pylab as plt

# im1 = np.zeros([200, 200, 3]) + 0
# im2 = np.zeros([200, 200, 3]) + 50
# im2 = np.uint8(im2)
# plt.figure(figsize=(5, 5))
# plt.imshow(im1)
# plt.axis('off')
# plt.show()
# plt.figure(figsize=(5, 5))
# plt.imshow(im2)
# # plt.axis('off')
# plt.show()
# im3 = np.zeros([200, 200, 3])
# im3[:, :, 0] = 0
# im3[:, :, 1] = 0
# im3[:, :, 2] = 0
# plt.figure(figsize=(5, 5))
# plt.imshow(im3)
# plt.axis('off')
# plt.show()
im3 = np.zeros([200, 200, 3])
im3[0:100, 0:100,0] = 0
im3[1:50, 1:50, 1] = 1
im3[0:150, 0:150, 2 ] = 1
plt.figure(figsize=(5, 5))
plt.imshow(im3)
plt.axis('off')
plt.show()
