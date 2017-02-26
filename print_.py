def get_print(i, org, lst):
    l = [i for i in lst if i != '-']
    pr = sum(l) * 100 / 8
    with open('otchet.txt', 'a') as f:
        print('-' * 127, file=f)
        print(f'|{i:^{5}}|{org:^{65}}|{lst[0]:^{5}}|{lst[1]:^{5}}|{lst[2]:^{5}}|{lst[3]:^{5}}|{lst[4]:^{5}}|{lst[5]:^{5}}|'
              f'{lst[6]:^{5}}|{lst[7]:^{5}}|{pr:^{5}}|', file=f)
