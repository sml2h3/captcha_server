# captcha_server
一个免费开源一键搭建的通用验证码识别平台，大部分常见的中英数验证码识别都没啥问题。

## 使用方法
python >= 3.8 以上环境

`pip install -r requirements.txt -i https://pypi.douban.com/simple`

### Linux系统下可以直接用以下代码部署

`gunicorn -c conf.py ocr_server:app`

### Windows下就老老实实的

`python ocr_server.py`

知识星球搜索ID： 4198635

赶快来加入我们吧