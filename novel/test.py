import requests
from lxml import etree

repones = requests.get("https://m.biquge5.com/3_3194/")
print(repones.text)
html = etree.HTML(repones.text)
ms = html.xpath('/html/body/div[4]/div/div[2]/child::*')
info = []
info.append(ms[1].text)
info.append(ms[2].text)
info.append(ms[3].text)
info.append(ms[4].text)
info.append(ms[4].xpath("..//a/@href")[1].replace('\n','')+":" +ms[0].xpath("..//a/text()")[0])
print(info)