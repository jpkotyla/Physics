from physics.research.astro.astro_import import *
import numpy as np
import matplotlib.pyplot as plt


image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
hdu_list = fits.open(image_file)
hdu_list.info()
image_data = hdu_list[0].data
#or
image_data = fits.getdata(image_file)


plt.imshow(image_data, cmap='gray')
plt.colorbar()



# image list
image_list = Ned.get_image_list("3C186")

# getting the images
images = Ned.get_images("3C186")

header = images[1][0]
sci_img = images[1][1]
from matplotlib.colors import LogNorm
plt.imshow(sci_img,cmap = 'grey',NORM = LogNorm)
