import requests, json
 
# パラメーター（要書き換え）
DEVICEID="02-202004041939-33"
ACCESS_TOKEN="c31a91ddd5b635a475272d5ffcce20f32b49fdc848d5b1de662b4d1e29854ec2bbcea6e9d1b9562d6040c8fc6f89c89f"
API_BASE_URL="https://api.switch-bot.com"
 
# Send device control commandsコマンド（POST）
def device_control():
    headers = {
        # ヘッダー
        'Content-Type': 'application/json; charset: utf8',
        'Authorization': ACCESS_TOKEN
    }
    url = API_BASE_URL + "/v1.0/devices/" + DEVICEID + "/commands"
    body = {
        # 操作内容
        "command":"turnOn",
        "parameter":"default",
        "commandType":""
    }
    ddd = json.dumps(body)
    print(ddd) # 入力
    res = requests.post(url, data=ddd, headers=headers)
    print(res) # 結果
 
if __name__ == '__main__':
    # 処理呼び出し
    device_control()
