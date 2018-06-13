from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

# 1. Download Webpage

#1.1 Create a connection
url = "https://www.apple.com/itunes/charts/songs"

#1.2
html_content = urlopen(url).read().decode('utf8')
new_html_content = html_content.replace("<ul","xxx",3)

# 2. Extract ROI (region of interest)
# # html, xml, xhtml
soup = BeautifulSoup(new_html_content, "html.parser")
# print(soup.prettify())

ul = soup.find("ul")

print(ul.prettify())

li_list = ul.find_all("li")
print(li_list)


a_list_of_dict = []
list_of_query = []
for li in li_list:
    dict_ = {}
    h4 = li.h4
    a1 = h4.a
    a2 = li.h3.a
    name_of_song = a2.string
    author = a1.string
    dict_["author"] = author
    dict_["name of song"] = name_of_song
    a_list_of_dict.append(dict_)
    list_of_query.append(name_of_song +" " + author)
    # print(list_of_query)

pyexcel.save_as(records = a_list_of_dict, dest_file_name = "song_author.xlsx")

# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}

for i in range(len(list_of_query)):
    dl = YoutubeDL(options)
    dl.download(list_of_query[i])

# 3. Extract info

