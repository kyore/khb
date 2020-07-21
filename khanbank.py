import requests
import urllib3

from bs4 import BeautifulSoup
from utils.helper import Date

from settings import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MNT = 'MNTD0000000'

ACCOUNT_LIST = [
    f'{MNT}{KHANBANK_ACCOUNT}',
]

# request header
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

# request initial data
request_data = {
    'SM': 'UpPnlLogin|btnLogin',
    '__LASTFOCUS': '',
    '__EVENTTARGET': 'btnLogin',
    '__EVENTARGUMENT': '',
    'txtCustNo': KHANBANK_ACCOUNT,
    'txtPassword': KHANBANK_PASSWORD,
    'ASYNCPOST': 'true',
}

with requests.Session() as session:
    url = "https://e.khanbank.com/"

    # update the session header
    session.headers.update(headers)

    # Main request
    request = session.get(url, verify=False)
    soup = BeautifulSoup(request.content, 'html5lib')

    # Collect Data from the view
    request_data['__VIEWSTATE'] = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    request_data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'name': '__VIEWSTATEGENERATOR'})['value']
    request_data['__EVENTVALIDATION'] = soup.find('input', attrs={'name': '__EVENTVALIDATION'})['value']

    # Login request
    auth_post = session.post(url, data=request_data, verify=False)

    # Session is saved to session variable and download the file from website
    date = Date()

    download_url = url + f'pageMain?content=ucAcnt_Statement3&bd={date.download_start_date}&ed={date.download_end_date}&an={ACCOUNT_LIST[0]}&at=XLS1'
    file = session.get(download_url)

    output = open('khanbank.XLS', 'wb')
    output.write(file.content)
    output.close()
