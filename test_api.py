import requests

api_url = "http://127.0.0.1:9898/api"
#
# # 方式一
file = open(r'C:\Users\sml2h3\Desktop\20210521172450.png', 'rb').read()

resp = requests.post(api_url, files={'image': file})
print(resp.text)

# 方式二

# 获取验证码图片
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4195.1 Safari/537.36"
# }
# resp = requests.get('https://data.gdcic.net/Dop/CheckCode.aspx?codemark=408.15173910730016', headers=headers, verify=False)
# captcha_img = resp.content
#
# # 识别
# resp = requests.post(api_url, files={'image': captcha_img})
# print('验证码结果', resp.text)
#
# # 保存验证码图片以供验证
# with open('captcha.jpg', 'wb') as f:
#     f.write(captcha_img)
