from bs4 import BeautifulSoup
import requests
import json

entries={}

def cinebench_r23():
    url = 'https://www.cgdirector.com/cinebench-r23-scores-updated-results/'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    table_box = soup.find('div', class_='tablepress-scroll-wrapper')
    for i in range(56):
        cpu_name = table_box.find_all('td', class_=f'column-1')[i].text
        core_count = table_box.find_all('td', class_=f'column-2')[i].text
        clock_speed = table_box.find_all('td', class_=f'column-3')[i].text
        single_score = table_box.find_all('td', class_=f'column-4')[i].text
        multi_score = table_box.find_all('td', class_=f'column-5')[i].text
        entries.update({cpu_name: {core_count,clock_speed,single_score,multi_score}})
    return entries


def check_name_cinebench_r23(name):
    if name in entries:
        return entries[name]
    if name not in entries:
        return 'failure'
