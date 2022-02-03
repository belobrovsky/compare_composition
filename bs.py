from bs4 import BeautifulSoup
import requests
import re

znpDict = {}
articleList = []
articleInfoDict = {}
znpNumberList = []
rows = []
articleSet = set()


def delete():
    znpDict.clear()
    articleList.clear()
    znpNumberList.clear()
    rows.clear()
    articleSet.clear()

    
def pars_znp(number):
    global znpDict
    global articleSet
    global znpNumberList
    global articleInfoDict
    path = 'http://portal18/sup/Invoice/Info/Invoice/' + str(number)
    r = requests.get(path)
    contents = r.text
    soup = BeautifulSoup(contents, 'html.parser')

    znpNumber = soup.find('h2', id="InvoiceInfo").findNext('a', href=True).text.split('-')[-1]
    znpNumberList.append(znpNumber)

    ellem = soup.find_all('tr', class_=['nopereborka', 'consumable'])

    znp = {}
    for i, el in enumerate(ellem):
        try:
            article = el.find('a', class_='sku').text
            if el.find('td', style='text-align:right;width:1%;'):
                count = el.find('td', style='text-align:right;width:1%;').findNext('span').findNext('nobr').findNext('b').text
            else:
                count = el.find('td', style='text-align:right;').findNext('span').findNext('nobr').findNext('b').text
            article_count = {'article': article, 'count': count}
            article_info = {'article': article,
                       'link': el.find('a', class_='sku').get('href'),
                       'name': el.find('div', class_='element_name').text.strip()}
            articleSet.add(article)
            znp.update({article: article_count})
            try:
                articleInfoDict[article]
            except KeyError:
                articleInfoDict.update({article: article_info})
        except AttributeError as e:
			continue

    znpDict.update({znpNumber: znp})
 
def getElements():
    global articleList
    global znpNumberList
    global rows
    rows.clear()
    articleList.clear()
    articleList = list(articleSet)
    articleList.sort()
    link = ''
    name = ''
    for article in articleList:
        row = []
        for znp in znpNumberList:
            try:
                row.append({'znp': znp, 'article': article, 'count': znpDict[znp][article]['count']})
            except KeyError:
                row.append({'znp': znp, 'article': article, 'count': 'НЕТ'})
                
        rows.append(row)
	return (rows, articleInfoDict)

