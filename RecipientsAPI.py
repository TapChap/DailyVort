import requests
from lxml import html

# Load the sheet’s public HTML URL
# URL of the public Google Sheet in HTML view
url = "https://docs.google.com/spreadsheets/d/1E0pIfCzWF7sq-p-pB5h6jokS-W6Vt8lR3G2Kv1Y0-mY/htmlview"

def getRecipients(url=url):
    # Fetch the page
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # Extract all text from the cells in column A (first column)
    ColA = tree.xpath('//table//tr//td[1]/text()')  # Select the first column (A)

    # Clean up the data (remove extra whitespace and empty strings)
    return [cell for cell in ColA]

print(getRecipients())
a = open('recipients.txt', 'r').read().splitlines()
print(a)