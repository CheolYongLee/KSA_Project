import os
import sys
import requests

def ImageService(ImageName):
    client_id = "dc1er7xa9q"  # 고정 id
    client_secret = "MJHgxtGQACF7EHPRTUE9IpgRllyiOn4RtYC2jKzy"  # 고정 키
    url = "https://naveropenapi.apigw.ntruss.com/vision-pose/v1/estimate"  # 사람 인식
    files = {'image': open(ImageName, 'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if (rescode==200):
        print(response.text)  # 손가락이 인식되었습니다.
    else:
        print("Error Code:" + rescode)

    # if 4 >= 0.7 or 7 >= 0.7:
    #     massage = 확인하세요
    #
    # else:
    #
    # return message
