import re
import requests
import time
from bs4 import BeautifulSoup

def getRate(player):
    # 対象のURLを入力
    player_list = {"Glitter":"https://smashmate.net/user/96773/?ts={int(time.time())",
                    "まぐろ":"https://smashmate.net/user/68917/?ts={int(time.time())}", 
                    "あまね":"https://smashmate.net/user/152292/?ts={int(time.time())}",
                    "氏家":"https://smashmate.net/user/163721/?ts={int(time.time())}",
                    "クロダイ":"https://smashmate.net/user/163237/?ts={int(time.time())}",
                    "k-z":"https://smashmate.net/user/27914/?ts={int(time.time())}",
                    "k-zサブ":"https://smashmate.net/user/118406/?ts={int(time.time())}",
                    "ナカ":"https://smashmate.net/user/51055/?ts={int(time.time())}",
                    "まよまよ":"https://smashmate.net/user/132494/?ts={int(time.time())}"
                    }
    url = player_list[player]

    # Webページの内容を取得
    headers = {
        'Cache-Control': 'no-cache, no-store,must-revalidate, max-age=0',
        'Pragma': 'no-cache',
        'Expires': '0',
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers = headers)

    # ステータスコードが200（成功）なら処理を続行
    if response.status_code == 200:
        # HTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # ページ内のレートテキストをすべて取得
        results = soup.select("span.rate_text") 
        text_1 = results[0].get_text()
        text_2 = results[1].get_text()
        
        # 数字だけ抽出
        
        now_rate = re.findall(r"\d+", text_1)
        #print(now_rate)
        max_rate = re.findall(r"\d+", text_2)
        #print(max_rate)
        return(now_rate[0], max_rate[0]) 
    else:
        print(f'ページの取得に失敗しました。ステータスコード: {response.status_code}')

