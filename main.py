# from asyncio.base_subprocess import WriteSubprocessPipeProto
# from pickletools import bytes4
# from sys import api_version
# from winreg import REG_RESOURCE_REQUIREMENTS_LIST

# import requests


# If we want to scrap a website:
# 1. Use the API
# 2. HTML web scrapping using tools like BS4

# Step 0 : Install all the Requirements
# pip install requests
# pip install bs4
# pip install html5lib

# from weakref import ref
import requests
from bs4 import BeautifulSoup
url = "https://code1o1.github.io/en/"

with open("/home/gautam/Data Structures and Algo/BeautifulSoup/refrence.html") as ref:
    soup2=BeautifulSoup(ref, 'html.parser')
# print(soup2)
# print(soup2.prettify())

# print(soup2.find('p').get_text())


# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print (soup.prettify())


# Step 3 : HTML tree traversal
# Commonly used type of Objects
# Tag print(type(title))
# NavigableString print(type(title.string))
# BeaytifulSoupObject print(type(soup))
# Comment

# markup="<p>this is a comment</p>"
# soup2=BeautifulSoup(markup)
# print(type(soup2.p.string))


# Get the title of Html page
# print(type(soup))
t = soup.title
# t.name="Gautam"
# print(type(t))

# # Get all the Paragraphs from the page
paras = soup.find_all('a')
# print(paras)




# # Get all the Anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

# all_links=set()

# for links in soup.find_all('a'):
#     if(links.get('href') != None) :
#         print("https://code1o1.github.io"+links.get('href'))

# print(soup.find('a')) #returns first paragraph tag in html
# print(soup.find('a')['href']) #returns class in paragraph tag in html

soup.find('a')['href'] = "www.google.com"
# print(soup.find('a'))

# print(soup.find_all("a",class_="active")) #returns class lead in paragraph tag in html

# # Get the text from the tags
# print(soup.find('a').get_text())
# print(soup.get_text())

# #Get all the links on the page
# all_links = set()
# for link in anchors:
#     if(link.get('href') != '#'):
#         linkText = "https://search.com"+link.get('href')
#         all_links.add(linkText)
        # print(linkText)
        # print(link.get('href'))
