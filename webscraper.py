from bs4 import BeautifulSoup
import requests
import sys
import shutil
import os

# The links of individual images.
links = []
# url of website from where the images are taken.
url = 'http://www.astronomy.com/photos'
response = requests.get(url,timeout=100)
content = BeautifulSoup(response.content,"html.parser")
#Get all images with the class of preview images.
preview_images = content.find_all('div',attrs={"class": "previewImage"})
for div in preview_images:
    for a in div.find_all('a',href=True):
        #Use the anchor tage with href of photos/picture-of-day to find the
        #absolute path of all the picture-of-day images.
        url_index = a['href'].find('/photos/picture-of-day/')
        if url_index != -1:
            #The image's absolute URL is in style under "background-image".
            img_style = div.get('style')
            if img_style is not None:
                start_img_source = "background-image:url('/-/media/Images/Photo of Day/Large Images/"
                if img_style.find(start_img_source) != -1:
                    end_index = img_style.find(')')
                    img_link = img_style[len(start_img_source) : end_index-1]
                    #Form image link to download and append to links array.
                    links.append("http://www.astronomy.com/photos/-/media/Images/Photo%20of%20Day/Large%20Images/"+img_link+'?mw=1000&mh=800')

counter = 1
path = os.path.join( os.getcwd(), 'images' )
#Make directory images if it does not exists already.
if(os.path.isdir('images')) == False:
    os.mkdir(path)
print("Downloading images ...")
#Downlaod images by streaming.
for link in links:
    request_stream = requests.get(link,stream=True)
    if request_stream.status_code == 200:
                    request_stream.raw.decode_content = True
                    file = open( path + '/' +'astro'+str(counter)+'.jpg', "wb" )
                    shutil.copyfileobj(request_stream.raw, file)
                    counter = counter + 1
                    file.close()
print("Done")
