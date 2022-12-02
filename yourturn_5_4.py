import requests
from bs4 import BeautifulSoup

class WeaG:
    
    def __init__(self):
        self._url = 'https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/TBD.html'
        self._load()
    
    def grab(self, location):
        rtn = {}
        if location in self._sites:
            url = self._url.replace('TBD', self._sites[location])
            r = requests.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                try:
                    rtn['O'] = soup.find(headers="time").text
                    rtn['T'] = float(soup.find(class_="tem-C").text)
                    rtn['H'] = float(soup.find(headers="hum").text)/100
                    rtn['R'] = float(soup.find(headers="rain").text)
                except:
                    pass
            r.close()
        return rtn
    
    def _load(self):
        url = 'https://www.cwb.gov.tw/Data/js/Observe/OSM/C/STMap.json'
        j = requests.get(url)
        self._sites = {i['STname']: i['ID'] for i in j.json()} if j.status_code == 200 else {}
        j.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('location', help='location weather to be grabbed')
    args = parser.parse_args()
    
    w = WeaG()
    r = w.grab(args.location)
    if r:
        print(f'{args.location} 觀測時間: {r["O"]} 溫度: {r["T"]:.1f}°C, 濕度: {r["H"]:.0%}, 雨量: {r["R"]:.1f}mm')
    else:
        print(f'{args.location} 查無此站！')
