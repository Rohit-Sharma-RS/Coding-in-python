from bs4 import BeautifulSoup

with open('website.html', encoding='utf8') as file:
    r = file.read()

soup = BeautifulSoup(r, 'html.parser')
# print(soup.p)

#but how to find all the tags in the html file
# well just use find_all

# all_anchor = soup.find_all(name="a", id="name")
#
# for anchor in all_anchor:
#     print(anchor.get('href'))

selected = soup.select(selector='#name')# pound size shows that it is an id
select_class = soup.select(selector=".heading")#. is to show it's a class
print(select_class)
print(selected)
    