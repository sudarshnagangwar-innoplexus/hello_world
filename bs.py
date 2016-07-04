from bs4 import BeautifulSoup
import urllib2
    url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
    page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "lxml")
print soup.find_all("div").text

def 
