import urllib.request as req
import bs4
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

def write_file(filenaem, lines):
    with open(filenaem, 'w', encoding='utf-8') as f:
        f.write('日期' + ',' + '匯率' + '\n')
        for line in lines:
            f.write(line + '\n')

def main():
    #lines = ['20210722' + ',' + '30.1' + '\n' + '20210723' + ',' + '29.8' + '\n']
    #web_crawler('https://www.ptt.cc/bbs/movie/index.html')
    #抓取TCB官網上美元的即期買入匯率
    d = web_crawler('https://ibank.tcbbank.com.tw/PIB/cb5/cb501005/CB501005_01.faces')
    print(d)
    write_file('usd.csv', d)
    print('OK')

if __name__ == '__main__':
    main()
