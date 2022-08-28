from os import link
from urllib import response
import requests
from bs4 import BeautifulSoup

def dl_file(url):
    url_temp = url.split('.')
    file_name = url_temp[-2].split('/')[-1]
    file_ext = url_temp[-1]
    r = requests.get(url, allow_redirects=True)
    open(f'files/{file_name}.{file_ext}', 'wb').write(r.content)

def get_links(url):
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    span_ls = page.findAll('span', attrs={'class':'filenamereply'})
    link_list = []
    for span in span_ls:
        element = str(span.findAll('a')).split(' ')
        link = element[1].split('"')[1]
        link_list.append(link)
    return link_list

main_url = input('URL: ')
links = get_links(main_url)
link_count = 1
for l in links:
    print(f'Downloading file {link_count} of {len(links)}')
    dl_file(l)
    link_count+=1
print('Done!')

