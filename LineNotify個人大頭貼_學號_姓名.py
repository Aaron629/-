import requests

def lineNotifyMessage_image(token, msg, image_path):
    headers = {
        "Authorization":"Bearer " + token,
    }
    
    payload = {'message' : msg}
    files = {'imageFile' :open(image_path, 'rb')}
    r = requests.post("https://notify-api.line.me/api/notify",
                         headers = headers, params=payload, files=files)
    print(r.status_code)
    return r.status_code

image_path = r'C:\Users\haolun.DESKTOP-673FV82\Downloads\pic1.jpg'

message = '這是你的大頭貼, 學號:A10923004, 姓名:許皓倫'

token = 'cm1GDyiLRyfDeZMzpnQxblvuVnI3knoSr3EnccmzLE8'

lineNotifyMessage_image(token, message, image_path)