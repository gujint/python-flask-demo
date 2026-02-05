# 热点新闻API服务

一个简单的Flask服务，提供热点新闻数据接口。

## 快速开始

1. 安装依赖：`pip install -r requirements.txt`
2. 复制环境变量文件：`cp .env .env`
3. 在`.env`中配置你的聚合数据API密钥
4. 启动服务：`python app.py`
5. 访问：`http://localhost:5000/hot-news`

## API接口

GET `/hot-news`
返回热点新闻列表
