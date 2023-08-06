from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.blacktailstudio.com/blog/a-table-with-good-jeans').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

print(article.prettify())
# headline = article.h2.a.text
# print(headline)

# summary = article.find('div', class_='row sqs-row').p.text
# print(summary)
