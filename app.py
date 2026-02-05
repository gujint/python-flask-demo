from flask import Flask, jsonify
from news_fetcher import fetch_hot_news
import os
from dotenv import load_dotenv
# 加载 .env 文件中的配置
load_dotenv()

app = Flask(__name__)

@app.route('/hot-news', methods=['GET'])
def get_hot_news():
    # 从环境变量中获取 API_KEY
    api_key = os.getenv('API_KEY')
    if not api_key:
        return jsonify({'error': 'API密钥未配置'}), 500
    
    # 调用方法 获取新闻信息
    news = fetch_hot_news(api_key,'top',1,5,0)
    if news is None:
        return jsonify({'error': '获取新闻失败'}), 500

    return jsonify({
        'success': 0,
        'count': len(news),
        'data': news
    })

# 注释/删除原来的这一行
# if __name__ == '__main__':
#     app.run(debug=True)  

# 替换成这个部署版启动代码（适配Render，本地运行也兼容）
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # 必须绑定，否则Render内部无法访问你的服务
        port=int(os.getenv('PORT', 5000)),  # 用Render的$PORT环境变量，本地运行默认5000
        debug=False  # 生产环境强制关闭debug，避免安全风险+Render服务异常
    )
