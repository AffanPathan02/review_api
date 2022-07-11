from bs4 import BeautifulSoup
from flask import jsonify
import requests
import jsonpickle

entries={}

def cpu_benchmark():
    url='https://www.cpubenchmark.net/desktop.html'
    html_text=requests.get(url).text
    soap=BeautifulSoup(html_text,'lxml')
    main_div=soap.find('div',class_='main-cmps')
    ul_list=main_div.find_all('li')
    for index,ul in enumerate(ul_list):
        cpu_name=ul_list[index].find('span',class_='prdname').text.replace('\n','')
        cpu_score=ul_list[index].find('span',class_='count').text.replace(',','')
        entries.update({cpu_name:cpu_score})
    return entries


def check_name_cpu_benchmark(name):
    if name in entries:
        return entries[name]
    if name not in entries:
        return 'False'




