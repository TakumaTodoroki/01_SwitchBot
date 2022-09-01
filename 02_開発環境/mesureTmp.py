# %% get data
import requests
import json

# Please get your access token via switchbot app
header = {"Authorization": "c31a91ddd5b635a475272d5ffcce20f32b49fdc848d5b1de662b4d1e29854ec2bbcea6e9d1b9562d6040c8fc6f89c89f"}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

# Get deviceId for hygrometer of "your hygrometer device name" in all device information 
device_id = [device['deviceId'] for device in devices['body']['deviceList'] if "温湿度計" in device['deviceName']]

# call hygrometer state via switchbot api
url = "https://api.switch-bot.com/v1.0/devices/" + device_id[0] + '/status'
response = requests.get(url, headers=header)
json_respons = json.loads(response.text)

# Get temperature
temp = json_respons['body']['temperature']
# Get humidity
humid = json_respons['body']['humidity']

# output 
print(temp)
print(humid)
# %% tweet

# import tweepy