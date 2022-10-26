#!/usr/bin/env python3
import requests as req
import argparse
import re
import os


base_url = 'https://www.bing.com'
url_patt = r'background-image: url\((.*?\.jpg)'
img_name_patt = r'id\=(.*?\.jpg)'

# argument parser
arg_parser = argparse.ArgumentParser(prog='bing-bg', description='This script will download the Bing background for you :)')
arg_parser.add_argument('-d', '--directory', action='store', help='Choose a path to save')
arg_parser.add_argument('-o', '--only_once', action='store_true', help='Only one image save in directory')
args = arg_parser.parse_args()

# find image
url_content = req.get(base_url)
img_url = re.search(url_patt, url_content.text).groups()[0]
fin_url = base_url + img_url

# download image
img = req.get(fin_url)
if args.only_once == True:
    name = 'bing-bg.jpg'
else:
    name = re.search(img_name_patt, img_url).groups()[0]

# save image
dir = f'./{name}'
if args.directory is not None:
    if not os.path.isdir(args.directory):
        print('The path specified does not exist')
        exit(1)
    dir = f'{args.directory}/{name}'
with open(dir, 'wb') as img_file:
    img_file.write(img.content)

# delete old images
# ...
