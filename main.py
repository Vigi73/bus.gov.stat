# 2017 Alti, Kurya (c)Vigi-Soft
#------------------------------
from selenium import webdriver
from datetime import datetime
from libs import pars
from inn_org import inns
from organization import  get_value



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
    st_time = datetime.now()
    driver = webdriver.Chrome()
    driver.set_window_size(0, 0)
    driver.set_window_position(1000, 0)

    for inn in inns:
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
        print(name_org, result)

    driver.quit()
    end_time = datetime.now()
    print(str(end_time - st_time))
