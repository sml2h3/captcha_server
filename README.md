# captcha_server
一个免费开源一键搭建的通用验证码识别平台，大部分常见的中英数验证码识别都没啥问题。

## 使用方法

# 为了方便大家使用,已将项目打包成pypi包

```
可以通过以下命令安装
pip install ddddocr==1.0.4

豆瓣源同步需要一些时间,目前建议通过官方源安装(命令后添加 -i https://pypi.org/simple)

使用方式为

import ddddocr

ocr = ddddocr.DdddOcr()

with open('test.png', 'rb') as f:
img_bytes = f.read()

res = ocr.classification(img_bytes)
print(res)
```

--------

python >= 3.8 以上环境

`pip install -r requirements.txt -i https://pypi.douban.com/simple`

### Linux系统下可以直接用以下代码部署

`gunicorn -c conf.py ocr_server:app`

### Windows下就老老实实的

`python ocr_server.py`

知识星球搜索ID： 4198635

赶快来加入我们吧