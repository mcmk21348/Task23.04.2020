

import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_ = 'pager-wrap')
    posl = pages.find_all('a')[-1].get('href')
    total_pages = posl.split('=')[1]

    return int(total_pages)


def write_csv(data):
    with open('kivano1.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['Title'], data['Price'], data['foto']) )


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    asd = soup.find('div', class_ = 'list-view').find_all('div', class_ = 'product_listbox')

    for ad in asd:
        #title, KGS, foto
        try:
            title = ad.find('div', class_ = 'listbox_title').find('a').text
        except:
            title = ''
        
        try:
            KGS = ad.find('div',class_ = 'listbox_price').find('strong').text
        
        except:
            KGS = ''

        try:
            foto = ad.find('div', class_ = 'listbox_img').find('a')
        except:
            foto = ''

        data = {'Title': title, 'Price': KGS, 'foto': foto}

        write_csv(data)
    





def main():
    url= 'https://www.kivano.kg/mobilnye-telefony'
    base_url= 'https://www.kivano.kg'
    last_url = base_url + '/mobilnye-telefony'
    page_part = '?page='
    total = get_total_pages(get_html(url))



    
    for i in range(1, total+1):
        url_gen = last_url + page_part + str(i)
        print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)





if __name__ == '__main__':
    main()