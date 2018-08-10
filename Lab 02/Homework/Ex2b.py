from Ex2a import musi, post
from youtube_dl import YoutubeDL

hang_cho = []
for post in musi:
    cho =  post['Name'] + ' ' + post['Artist']
    hang_cho.append(cho)

for i in range(len(hang_cho)):
    options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
    }
    dl = YoutubeDL(options)
    dl.download([hang_cho[i]])