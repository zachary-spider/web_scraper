import pandas as pd
from docx import Document

doc = Document()
import requests
lst = []
error1 = []
error2 = []
text = ''
from bs4 import BeautifulSoup
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'}
for page in range(1,2):
    try:
        url = 'https://fintechs.fi/page/{}/'.format(page)
        html = requests.get(url=url,headers=headers,timeout=10)
        soup = BeautifulSoup(html.text,'lxml')
        sj_lst = soup.select('.blog-post-content h2 a')
        for m in sj_lst:
            try:
                url2 = m['href']
                html2 = requests.get(url=url2,headers = headers,timeout=10)
                soup2 = BeautifulSoup(html2.text,'lxml')
                title = soup2.select('h1.entry-title')[0].text.strip()
                content = soup2.select('.body-content.post-content-wrap')[0].text.strip().replace('\n','')
                text1 = 'title:\n'+title+'\n'+'content:\n'+content
                text = text+text1+'\n------------------------------\n'
                print(url2,'success')
            except:
                error2.append(url2)
    except:
        error1.append(page)
        
for page in error1:
    try:
        url = 'https://fintechs.fi/page/{}/'.format(page)
        html = requests.get(url=url,headers=headers,timeout=10)
        soup = BeautifulSoup(html.text,'lxml')
        sj_lst = soup.select('.blog-post-content h2 a')
        for m in sj_lst:
            try:
                url2 = m['href']
                html2 = requests.get(url=url2,headers = headers,timeout=10)
                soup2 = BeautifulSoup(html2.text,'lxml')
                title = soup2.select('h1.entry-title')[0].text.strip()
                content = soup2.select('.body-content.post-content-wrap')[0].text.strip().replace('\n','')
                text1 = 'title:\n'+title+'\n'+'content:\n'+content
                text = text+text1+'\n------------------------------\n'
                print(url2,'success')
            except:
                error2.append(url2)
    except:
        error1.append(page)
for url in error2:
    try:
        html2 = requests.get(url=url2,headers = headers,timeout=10)
        soup2 = BeautifulSoup(html2.text,'lxml')
        title = soup2.select('h1.entry-title')[0].text.strip()
        content = soup2.select('.body-content.post-content-wrap')[0].text.strip().replace('\n','')
        text1 = 'title:\n'+title+'\n'+'content:\n'+content
        text = text+text1+'\n------------------------------\n'
        print(url2,'success')
    except:
        pass
doc.add_paragraph(text)
doc.save("example.docx")
