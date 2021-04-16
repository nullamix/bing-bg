#!/bin/python
import requests as req
import re

base_url = 'https://www.bing.com'
url_patt = r'background-image: url\((.*?\.jpg)'
img_name_patt = r'id\=(.*?\.jpg)'

# find image
url_content = req.get(base_url)
img_url = re.search(url_patt, url_content.text).groups()[0]
fin_url = base_url + img_url

# download image
img = req.get(fin_url)
name = re.search(img_name_patt, img_url).groups()[0]
with open(f'/Path/to/images/directory/{name}', 'wb') as img_file:
    img_file.write(img.content)

# delete old images


