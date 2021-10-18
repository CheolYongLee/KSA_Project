import os
import sys
import requests
import json

def ImageService(ImageName):
    client_id = "dc1er7xa9q"  # 고정 id
    client_secret = "MJHgxtGQACF7EHPRTUE9IpgRllyiOn4RtYC2jKzy"  # 고정 키
    url = "https://naveropenapi.apigw.ntruss.com/vision-pose/v1/estimate"  # 사람 인식
    files = {'image': open(ImageName, 'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    json_data = json.loads(response.text)
    if (rescode==200):
        print(response.text)  # 손가락이 인식되었습니다.
        if json_data.get('predictions')[0].get('4').get('score') >= 0.7 or json_data.get('predictions')[0].get('7').get('score') >= 0.7 or json_data.get('predictions')[1].get('4').get('score') >= 0.7 or json_data.get('predictions')[1].get('7').get('score') >= 0.7:
            result = "지문 정보 유출에 주의하세요."
            print("False Alarm")
        else:
            result = "지문 정보가 없습니다."
    else:
        print(response.text)
        print("Error Code:" + str(rescode))
        result = "빈 값입니다."
    return result
