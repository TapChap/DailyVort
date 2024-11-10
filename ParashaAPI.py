import requests
from lxml import html

def getParasha():
    kiph_url = 'https://www.kipa.co.il/%D7%99%D7%94%D7%93%D7%95%D7%AA/%D7%A4%D7%A8%D7%A9%D7%AA-%D7%94%D7%A9%D7%91%D7%95%D7%A2/'
    parasha_xpath = '/html/body/div[3]/main/div[1]/aside/ul/li[1]/text()'

    response = requests.get(kiph_url)
    tree = html.fromstring(response.content)

    # Use XPath to extract specific content
    return tree.xpath(parasha_xpath)[0]

if __name__ == '__main__':
    print(getParasha())