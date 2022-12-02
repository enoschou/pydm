import requests

class WeaG:
    
    def __init__(self, key):
        self.URL = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/'
        self.DATAID = ['O-A0001-001', 'O-A0003-001']
        self.API = [f'{self.URL}/{d}' for d in self.DATAID]
        self.AUTH = key
        self.ELEMENTS = {'TEMP': 'T', 'HUMD': 'H', 'H_24R': 'R', '24R': 'R'}
        self.params = {'Authorization': self.AUTH, 'elementName': ','.join(self.ELEMENTS.keys())}
    
    def grab(self, location):
        self.params['locationName'] = location
        for i, api in enumerate(self.API):
            r = requests.get(api, params=self.params)
            if r.status_code == 200:
                j = r.json()
                r.close()
                locs = j['records']['location']
                wea = self._extract(location, locs)
                if wea:
                    return wea
            else:
                r.close()
        
        return None
    
    def _extract(self, location, locations):
        for loc in locations:
            if loc['locationName'] == location:
                r = {'O': loc['time']['obsTime']}
                for en in loc['weatherElement']:
                    if en['elementName'] in self.ELEMENTS:
                        r[self.ELEMENTS[en['elementName']]] = float(en['elementValue'])
                return r

        return None

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('location', help='氣象站名稱')
    parser.add_argument('-k', '--key', type=str, required=True, help='氣象局授權碼')
    args = parser.parse_args()
    
    w = WeaG(args.key)
    r = w.grab(args.location)
    if r:
        print(f'{args.location} 觀測時間: {r["O"]} 溫度: {r["T"]:.1f}°C, 濕度: {r["H"]:.0%}, 雨量: {r["R"]:.1f}mm')
    else:
        print(f'{args.location} 查無此站！')
