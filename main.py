# 2017 Alti, Kurya (c)Vigi-Soft
#------------------------------
from selenium import webdriver
from bs4 import BeautifulSoup as BS
from datetime import datetime



def get_pages(urls):
    st = datetime.now()
    driver = webdriver.Chrome()
    driver.set_window_size(0, 0)
    driver.set_window_position(1000, 0)

    for url in urls:
        driver.get(url)
        while True:
            req = pars(driver.page_source)
            if req != '-':
                break
        print(req)
    driver.quit()
    en = datetime.now()
    print(f'Using Time:{str(en - st)}')


def pars(html):
    soup = BS(html, 'lxml')
    try:
        r = soup.find('div', class_='info-container info-container_np').find('div', class_='info-date ng-binding ng-scope').text.strip()
        return r
    except:
        try:
            r = soup.find('div', class_='info-date').find('span', class_='ng-binding ng-scope').text.strip()
            return r
        except:
            return '-'


if __name__ == '__main__':
    urls = ['http://bus.gov.ru/pub/agency/206030/tasks/3573224',
            'http://bus.gov.ru/pub/agency/206030/plans',
            'http://bus.gov.ru/pub/agency/206030/operations/',
            'http://bus.gov.ru/pub/agency/206030/annual-balances-F0503721',
            'http://bus.gov.ru/pub/agency/206030/annual-balances-F0503730',
            'http://bus.gov.ru/pub/agency/206030/annual-balances-f0503737',
            'http://bus.gov.ru/pub/agency/206030/reports',
            'http://bus.gov.ru/pub/agency/206030/measures'
            ]
    get_pages(urls)