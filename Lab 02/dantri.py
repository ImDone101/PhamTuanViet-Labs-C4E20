from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
#1. Download web
url = 'http://dantri.com.vn'
content = urlopen(url).read().decode('utf-8')
# print(content)
# content = urlopen(url)
# file = open('dantri.html', 'wb')
# file.writelines(content)
# file.close()

#2. Extract ROI (Region of interest)
soup = BeautifulSoup(content, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew')
print(ul.prettify())


#3. Extract data
# dicti = []
# li_list = ul.find_all('li')
# for li in li_list:
#     post = {}
#     a = li.h4.a
#     post['title'] = a.string
#     post['url'] = url + a['href']
#     dicti.append(post)

# pyexcel.save_as(records=dicti, dest_file_name="file.xlsx")