from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
# 1. Download Webpage

#1.1 Create a connection
url = "http://dantri.com"

#1.2
html_content = urlopen(url).read().decode('utf8')
# print(type(html_content))

# save html_content to file
# f = open('dantri2.html','wb')
# f.write(html_content)
# f.close()

# urlretrieve(url,"dantri.html")

# 2. Extract ROI (region of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")

# print(soup.prettify())
ul = soup.find("ul","ul1 ulnew")

li_list = ul.find_all("li")
a_list_of_dict = []
for li in li_list:
    # print(li.prettify())
    # print()
    dict_ = {}
    h4 = li.h4
    a = h4.a
    # a = li.h4.a
    # print(a.prettify())
    link = url + a['href']
    title = a.string
    dict_["title"] = title
    dict_["link"] = link
    a_list_of_dict.append(dict_)
    print(dict_)

pyexcel.save_as(records=a_list_of_dict, dest_file_name="title_link.xlsx")
# print(ul.prettify())
# 3. Extract info