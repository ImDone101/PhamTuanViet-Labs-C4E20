from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'https://www.apple.com/itunes/charts/songs/'
content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(content, 'html.parser')
sec = soup.find('section', 'section chart-grid')

musi = []
li_list = sec.find_all('li')
for li in li_list:
    post ={}
    name = li.h3.a
    artist = li.h4.a
    post['Name'] = name.string
    post['Artist'] = artist.string
    musi.append(post)

pyexcel.save_as(records=musi, dest_file_name='iTunes.xlsx')