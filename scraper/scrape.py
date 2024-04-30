import os
import requests
try:
    from bs4 import BeautifulSoup
except:
    #try harder
    os.system("python3 -m pip install beautifulsoup4")
    os.system("python3 -m pip install bs4")
    os.system("easy_install beautifulsoup4")
    os.system("easy_install bs4")
    from bs4 import BeautifulSoup


html_tags = ["html", "head", "body", "title", "h1", "h2", "h3", "h4", "h5", "h6", "p", "a", "img", "ul", "ol", "li", "div", "span",
              "abbr", "address","area", "article","aside","audio","base","bdi","bdo","blockquote","button","canvas","caption","cite",
              "code","col","colgroup","data","datalist","dd","del","details","dfn","dialog","dl","dt","em","embed","fieldset","figcaption",
              "figure","footer","form","header","hgroup","hr","i","iframe", "input", "ins","kbd","label","legend","link","main","map",
              "mark","menu", "meta","meter","nav","noscript","object","optgroup", "option","output","param","picture","pre","progress","q",
              "rp","rt", "ruby","s","samp","script","search","section","select","small","source","strong","style","sub","summary","sup","svg",
              "table","tbody","td","template","textarea","tfoot","th","thread","time","tr","track","u","var","video","wbr"]

url = "https://harlington.org/"

content = requests.get(url).text
soup = BeautifulSoup(content,"html.parser")

#gets all sources to links
def getAllSrc(html_tags, soup):
    all_src = []
    for i in range(len(html_tags)):
        all_of_element = soup.find_all(html_tags[i])
        for el in all_of_element:
            src = el.get("src")
            if src == None:
                continue
            else:
                link = requests.compat.urljoin(url,src)
                all_src.append(link)
    return all_src

#gets all hrefs
def getAllHref(html_tags,soup):
    all_href = []
    for i in range(len(html_tags)):
        all_of_element = soup.find_all(html_tags[i])
        for el in all_of_element:
            href = el.get("href")
            if href == None:
                continue
            else:
                link = requests.compat.urljoin(url,href)
                all_href.append(link)
    return all_href

sources = getAllSrc(html_tags,soup)
hrefs = getAllHref(html_tags,soup)

#writes all sources to folder named after url
try:
    os.mkdir(f"{url}_souces")
except:
    pass


