from selenium import webdriver
from bs4 import BeautifulSoup as BS

Y = '2017'

def get_page_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

def pars(html):
    soup = BS(html, 'lxml')
    try:
        r = soup.find('div', class_='info-date ng-binding ng-scope').text.strip()
        return 1 if r.split('.')[-1] == Y else 0
    except:
        try:
            r = soup.find('div', class_='ng-binding ng-scope').text.strip()
            return 1 if r.split('.')[-1] == Y else 0
        except:
            try:
                r = soup.find('div', class_='info-date').text.strip()
                return 1 if r.split('.')[-1] == Y else 0
            except:
                return '-'




