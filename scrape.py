from lxml import html
import requests

page = requests.get('http://twitter-trends.iamrohit.in/india')
tree = html.fromstring(page.content)
trends = []

for x in range(5):
    path = '//*[@id="copyData"]/tr['+str(x+1)+']/th[2]/a/text()'
    trends.append(tree.xpath(path)[0])

print(trends)