from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.hefzech.com/').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
full_html = soup.prettify()
css_code = '\n'.join([style.string for style in soup.find_all('style')])
print("\nCod CSS:")
print(css_code)
print("Cod HTML:")
print(full_html)
#
# print(article)
# headline = article.h2.a.text
# print(headline)
#
# summary = article.find('div', class_='row sqs-row').p.text
# print(summary)
