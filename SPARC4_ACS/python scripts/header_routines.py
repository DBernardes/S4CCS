import astropy.io.fits as fits
import numpy as np
import pandas as pd
import os


		

def write_header(file, header_content):
	header_content = np.asarray(header_content)
	file = reformat_string(file)		
	with fits.open(file, mode='update') as hdu:				
		for i in range(np.shape(header_content)[0]):
			line = [reformat_string(value) for value in header_content[i]]
			_type = line[1]
			card = tuple(np.delete(line,1))			
			hdu[0].header.append(card)
	return

def reformat_string(string):
	string = str(string)[2:-1]
	return string



def save_image(file, data):
	fits.writeto(file, data, overwrite= True)
	return
	
#image = np.zeros((1000,1000))
#fits.writeto("image.fits", image, clobber=True)
#file = r"C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv"
#ss = pd.read_csv(file, delimiter='\t', header=None, squeeze=True, keep_default_na=False)
#header_content = [["AAA", "STRING", "", "COMMENT"]]
#write_header("image.fits", header_content)

# path = r"C:\Users\observer\Desktop"
# file = "image.fits"
# image = np.zeros((1000,1000))
# fits.writeto(path+"\\"+file, image, clobber=True)
# hdu = fits.open(path+"\\"+file)
# print(hdu[0])