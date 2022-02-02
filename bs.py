from bs4 import BeautifulSoup
import requests
import re
# r = requests.get('http://portal18/SUP/Queue/PreparationAndVerification')
# r = requests.get('http://portal18/sup/Invoice/Info/Invoice/294156002')

# znpNumber = ''

znpDict = {}
articleList = []
articleInfoDict = {}
znpNumberList = []
# row = []
rows = []
articleSet = set()


def delete():
    znpDict.clear()
    articleList.clear()
    znpNumberList.clear()
    # row = []
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

    # print(ellem[0].find('td', style='text-align:right;width:1%;').find('span').find('nobr').find('b').text)
    # elementList.clear()
    znp = {}
    for i, el in enumerate(ellem):
        # print(el)
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
            # print(i, e)
            continue

    znpDict.update({znpNumber: znp})
    # print(articleInfoDict)
    # print(znpDict)



# d = {'link': el.find('a', class_='sku').get('href'),
#      'article': el.find('a', class_='sku').text,
#      'name': el.find('div', class_='element_name').text.strip()}
# elementList.append(d)


def getElements():
    global articleList
    global znpNumberList
    global rows
    rows.clear()
    articleList.clear()
    articleList = list(articleSet)
    articleList.sort()
    # znpNumberList.sort()
    # row = []
    # rows = []
    # print(znpNumberList)
    link = ''
    name = ''
    for article in articleList:
        row = []
        # row.append(article)

        for znp in znpNumberList:
            try:
                # row.append(znpDict[znp][article]['count'])
                # link = znpDict[znp][article]['link']
                # name = znpDict[znp][article]['name']
                row.append({'znp': znp, 'article': article, 'count': znpDict[znp][article]['count']})
            except KeyError:
                row.append({'znp': znp, 'article': article, 'count': 'НЕТ'})
                # row.append('n')

            # print('row: ', row)
            # print(znpDict[znp][article]['count'])

        rows.append(row)
        # rows += row
        # print('rows: ', rows)

    return (rows, articleInfoDict)


# pars_znp()
# pars_znp(300069000)
# pars_znp(299899000)

# pars_znp(300069000)
# pars_znp(294156002)
# print(znpDict)
# print(articleInfoDict)
# getElements()
# with open('1.txt', 'w') as fd:
#     fd.write(str(getElements()))
#     fd.write(str(articleList))
#     fd.write(str(znpDict))
#     fd.write(str(znpNumberList))
    # for chunk in getElements():
    #     for chun in chunk:
    #         print(chun)
    #         fd.write(str(chun))
# print(getElements())
# pars_znp(294156002)

# for i, el in enumerate(getElements()):
#     print(i, el)

# print(articleList)
# print(articleList, '\n\n\n')
#     row = []
#     elements = soup.find_all('div', class_='element_name')
#     for el in elements:
#         row.append(el.text.strip())
#         # row += el.text.strip()
#     return row


# i = 0
# for el in elements:
#     i += 1
#     # print(i)
#     print(i, el.text.strip())


# for tag in soup.find_all("td"):
#     if tag.text is not None:
#         print("{0}: {1}".format(tag.name, tag.text))


