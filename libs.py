
from bs4 import BeautifulSoup as BS

Y = '2017'


def pars(html):
    soup = BS(html, 'lxml')
    try:
        r = soup.find('div', class_='info-container info-container_np').find('div', class_='info-date ng-binding ng-scope').text.strip()
        return 1 if r.split('.')[-1] == Y else 0
    except:
        try:
            r = soup.find('div', class_='info-date').find('span', class_='ng-binding ng-scope').text.strip()
            return 1 if r.split('.')[-1] == Y else 0
        except:
            return '-'









