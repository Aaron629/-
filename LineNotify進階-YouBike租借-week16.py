import requests
import requests as rq

token = 'cm1GDyiLRyfDeZMzpnQxblvuVnI3knoSr3EnccmzLE8'

YouBike_url = 'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/preview'

def NewTaipei_YouBike(url):
    html_content = rq.get(url, timeout=5)
    json_data = html_content.json()
    
    YouBike = '目前更新時間: ' + json_data[0]['mday']+"\n"
    
    for item_detail in json_data:
        YouBike += ("地址 : %-30s, 可借車位 : %+5s\n"%(item_detail['ar'],item_detail['sbi']))
        
    print(YouBike)
    return YouBike


def lineNotifyMessage_text(token, msg):
    headers = {
        "Authorization" : "Bearer "+ token,
        "Content-Type"  : "application/x-www-form-unlencoded"
    }
    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers = headers, params = payload)
    print(r.status_code)
    return r.status_code

YouBike_data = NewTaipei_YouBike(YouBike_url)
print(YouBike_data)
lineNotifyMessage_text(token, str(YouBike_data))
