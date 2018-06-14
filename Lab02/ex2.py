from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel

# 1. Download Webpage

#1.1 Create a connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

#1.2
html_content = urlopen(url).read().decode('utf8')
new_html_content = html_content.replace("<table","xxx",3)

# print(new_html_content)
# 2. Extract ROI (region of interest)

soup = BeautifulSoup(new_html_content, "html.parser")

ul = soup.find("table")


tr_list = ul.find_all("tr")


list_of_td = []

for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        k=td.string
        list_of_td.append(k)

# print(new_list_of_td)


a_list_of_dict = []

for i in range(0,len(list_of_td),20):
    dictionary = {}

    dictionary['title'] = list_of_td[i]
    dictionary['Quy 4 - 2016'] = list_of_td[i+1]
    dictionary['Quy 1 - 2017'] = list_of_td[i+2]
    dictionary['Quy 2 - 2017'] = list_of_td[i+3]
    dictionary['Quy 3 - 2017'] = list_of_td[i+4]

    a_list_of_dict.append(dictionary)

print(a_list_of_dict)

pyexcel.save_as(records = a_list_of_dict, dest_file_name = "vinamilk.xlsx")