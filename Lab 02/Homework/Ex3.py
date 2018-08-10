from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
data = soup.find('table', {'id':"tableContent"})
dLieu_list = data.find_all('tr', {"class": ["r_item ", "r_item_a "]})
dLieu = []

ten_cot = soup.find('div', {'id':'divTableHeader'})
a = ten_cot.find_all('td', 'h_t')
ten_cot_list = ["Danh mục"]
for i in range (len(a)):
    ten = a[i].text.strip()
    ten_cot_list.append(ten)

for dl in dLieu_list:
    col={}
    for j in range (len(ten_cot_list)):
        if j == 0:
            col0 = dl.find('td', {'style': ["width:32%;color:#014377;", "width:32%;color:#014377;font-weight:bold;","width:32%;color:#014377;font-style:italic;"]})
            col[ten_cot_list[j]] = col0.text.strip()
        elif j == 1:
            col1 = dl.find('td', {'style': ["width:15%;padding:4px;color:#014377;font-weight:bold;","width:15%;padding:4px;color:#014377;","width:15%;padding:4px;color:#014377;font-style:italic;"]})
            col[ten_cot_list[j]] = col1.string   
        else:
            col_previous = col1
            for k in range (len(ten_cot_list)-2):
                col_next = col_previous.find_next('td', {'style': ["width:15%;padding:4px;color:#014377;font-weight:bold;","width:15%;padding:4px;color:#014377;","width:15%;padding:4px;color:#014377;font-style:italic;"]})
                col[ten_cot_list[j]] = col_next.string
                col_previous = col_next
    
    dLieu.append(col)

pyexcel.save_as(records=dLieu, dest_file_name="vinamilk.xlsx")
