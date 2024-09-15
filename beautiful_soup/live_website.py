import re

from bs4 import BeautifulSoup
import requests
# ycombinator hacker news website to get latest tech news and handy things people might have built

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article = ""
all_titles = soup.find_all(name="span", class_="titleline")
alllink = []
alltitles = []
allupvote=[]
for title in all_titles:
    title_link = title.find('a')
    alltitles.append(title_link.get_text())
    alllink.append(title_link.get('href'))

allupvote=[int(upvote.get_text().split()[0]) for upvote in soup.find_all(name="span", class_="score")]

max_upvote = allupvote.index(max(allupvote))
print(alltitles[max_upvote])
print(alllink[max_upvote])
print(allupvote[max_upvote])

# for i in range(len(allupvote)):
#     print(alltitles[i])
#     print(alllink[i])
#     print(allupvote[i])
#     print()