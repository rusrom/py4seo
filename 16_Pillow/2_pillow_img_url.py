from PIL import Image
# from urllib import request
# import requests
import urllib3

from io import BytesIO


img_url = 'https://www.worldtravelguide.net/wp-content/uploads/2018/06/shu-NorthAmerica-DominicanRepublic-CapCana-411057478-PretoPerola-1441x823px.jpg'

# response = request.urlopen(img_url)  # urllib from standard library
# response = requests.get(img_url)  # requests
http = urllib3.PoolManager()  # urllib3
response = http.request('GET', img_url)  # urllib3

# image_file = BytesIO(response.read())  # urllib from standard library
# image_file = BytesIO(response.content)  # requests
image_file = BytesIO(response.data)  # urllib3

img_from_url = Image.open(image_file)
img_from_url.show()