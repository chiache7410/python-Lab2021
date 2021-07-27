import urllib.request as req
import bs4
import datetime
import os
def web_crawler(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
    })
    with req.urlopen(request) as responese:
        data=responese.read().decode("utf-8")
    #print(data)
    root=bs4.BeautifulSoup(data, "html.parser")
    currency = root.find_all("td", class_="lt")[0].string.replace(" ", "")
    exchangerate = root.find_all("td", class_="rt")[2].string
    return([currency, exchangerate])

def write_file(filename, lines):
    filename = filename + '.csv'
    fflag = os.path.isfile(filename)
    with open(filename, 'a', encoding='utf-8') as f:
        if not fflag:
            f.write('日期' + ',' + '匯率' + '\n')
        f.write(str(datetime.date.today()) + ',' + lines[1] + '\n')

def main():
    #抓取TCB官網上美元的即期買入匯率
    d = web_crawler('https://ibank.tcbbank.com.tw/PIB/cb5/cb501005/CB501005_01.faces')
    #print(d)
    write_file(d[0], d)
    print('OK')

if __name__ == '__main__':
    main()
