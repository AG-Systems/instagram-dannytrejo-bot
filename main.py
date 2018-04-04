from InstagramAPI import InstagramAPI
import os
from datetime import date


d0 = date(2018, 2, 4)

d1 = date.today()
delta = d1 - d0
print delta.days


InstagramAPI = InstagramAPI(os.environ['USERNAME_IG'], os.environ['PASSWORD_IG'])
InstagramAPI.login()  # login

photo_path = 'picture.jpg'
caption = str(delta.days-1)
InstagramAPI.uploadPhoto(photo_path, caption=caption)
