# captcha_server
一个免费开源一键搭建的通用验证码识别平台，大部分常见的中英数验证码识别都没啥问题。

## 使用方法
python >= 3.8 以上环境

`pip install -r requirements.txt -i https://pypi.douban.com/simple`

`gunicorn -c conf.py ocr_server:app`