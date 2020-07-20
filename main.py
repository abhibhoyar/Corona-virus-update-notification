from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 4
    )

def getdata(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    # notifyme("abhi ","lets talk the spread of the virus")
    while True:
        myHTMLdata = getdata('https://www.mohfw.gov.in')

        soup = BeautifulSoup(myHTMLdata, 'html.parser')
        # print(soup.prettify())
        mydatastr = ""
        for table in soup.find_all('tbody'):
            mydatastr += table.get_text()
        itemlist = (mydatastr.split('\n\n'))

        states = ['Maharashtra','Delhi']
        # for item in itemlist[1:38]:
        for item in itemlist[1:21]:
            datalist = item.split('\n')
            if datalist[2] in states:
                print(datalist)
                ntitle = 'Case of covid 19'
                ntext = f"{datalist[2]}\nActive Cases* : {datalist[3]} \nCured: {datalist[4]} \nDeaths**: {datalist[5]}\nTotal cases: {datalist[6]}"
                notifyme(ntitle,ntext)
                time.sleep(2)
        time.sleep(3600)
# for 1 Hour
