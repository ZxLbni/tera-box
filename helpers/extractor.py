import requests
from config import Config

async def terabox(link):
    redirects = requests.get(url=link)
    inp = redirects.url
    dom = inp.split("/")[2]
    fxl = inp.split("=")
    key = fxl[-1]
    URL = f'https://{dom}/share/list?app_id=250528&shorturl={key}&root=1'
    header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': f'https://{dom}/sharing/link?surl={key}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    url = requests.get(url=URL, headers=header, cookies=Config.COOKIES).json()['list'][0]['dlink']
    resp = requests.head(url,allow_redirects=True,stream=True).headers
    length = int(resp.get('Content-Length',0))
    file_name = resp.get('Content-Disposition').split("filename=")[-1].replace('"','')
    return url, length, file_name