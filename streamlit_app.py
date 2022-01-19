# This py file enables me to run my model on a streamlit app and display the results, 
# to better enable a user (especially a non-technical user) to understand the model

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import h5py
import IPython.display
import streamlit as st

import tensorflow as tf
from tensorflow.python.keras.preprocessing import image as kp_image
from tensorflow.python.keras import models 
from tensorflow.python.keras import losses
from tensorflow.python.keras import layers
from tensorflow.python.keras import backend as K


# Setup Prior to Streamlit Code

# Image Handling Code
def load_img(path_to_img):
	max_dim = 512
	img = Image.open(path_to_img)
	long = max(img.size)
	scale = max_dim/long
	img = img.resize((round(img.size[0]*scale), round(img.size[1]*scale)), Image.ANTIALIAS)
	img = kp_image.img_to_array(img)

	# We need to broadcast the image array such that it has a batch dimension 
	img = np.expand_dims(img, axis=0)
	return img

# Showing the image
def imshow(img, title=None):
	# Remove the batch dimension
	out = np.squeeze(img, axis=0)
	# Normalize for display 
	out = out.astype('uint8')
	plt.imshow(out)
	if title is not None:
		plt.title(title)
		plt.imshow(out)


if __name__ == "__main__":
	st.title('Neural Algorithm of Artistic Style')
	st.subheader('Fuse A Picture of Yourself with Any Style You Like!')

	st.subheader('Content Image')
	content_image_file = st.file_uploader("Upload Content Image (A Picture of You)", type=["png","jpg","jpeg"])

	st.subheader('Style Image')
	style_image_file = st.file_uploader("Upload Style Image (Art of your Choosing, Traditional or NFT)", type=["png","jpg","jpeg"])

# 	if content_image_file is not None and style_image_file is not None:
# 		# To Prepare Images for Modeling
# 		content = load_img(content_image_file).astype('uint8')
# 		style = load_img(style_image_file).astype('uint8') 

# 		# To View Uploaded Image
# 		st.image(imshow(content, 'Content Image')),width=250)
# 		st.image(imshow(style, 'Style Image')),width=250)

  
  
  
