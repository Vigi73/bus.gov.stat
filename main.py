from selenium import webdriver
from datetime import datetime
from libs import pars
from inn_org import inns
from organization import get_value
from print_ import get_print, print_main


def get_pages(urls):

    list_answer = []

    for url in urls:
        driver.get(url)
        while True:
            req = pars(driver.page_source)
            if req != '-':
                break
        list_answer.append(req)
    return list_answer


if __name__ == '__main__':

    print_main()

    st_time = datetime.now()
    driver = webdriver.Chrome()
    driver.set_window_size(0, 0)
    driver.set_window_position(1000, 0)

    for i, inn in enumerate(inns, start=1):
        value1, value2, name_org = get_value(inn)

        urls = [f'http://bus.gov.ru/pub/agency/{value1}/tasks/{value2}',
                f'http://bus.gov.ru/pub/agency/{value1}/plans',
                f'http://bus.gov.ru/pub/agency/{value1}/operations/',
                f'http://bus.gov.ru/pub/agency/{value1}/annual-balances-F0503721',
                f'http://bus.gov.ru/pub/agency/{value1}/annual-balances-F0503730',
                f'http://bus.gov.ru/pub/agency/{value1}/annual-balances-f0503737',
                f'http://bus.gov.ru/pub/agency/{value1}/reports',
                f'http://bus.gov.ru/pub/agency/{value1}/measures'
                ]

        result = get_pages(urls)
        pr = sum(result) * 100 / 8
        get_print(i, name_org, result)

    driver.quit()

    with open('otchet.txt', 'a', encoding='utf-8') as f:
        print('-' * 127, file=f)

    end_time = datetime.now()
    print(str(end_time - st_time).split('.')[0])
