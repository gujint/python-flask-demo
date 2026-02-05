import requests
from typing import List, Dict, Optional

# 923-新闻列表查询 - 代码参考（根据实际业务情况修改）

def fetch_hot_news(api_key:str, news_type:str, page:int, page_size: int,is_filter:int)-> Optional[List[Dict]]:
    """
    从聚合数据API获取热点新闻
    Args:
        api_key: 聚合数据API密钥
        news_type: 新闻类型，默认为'top'(头条)
        page: 当前页数, 默认1, 最大50
        page_size: 每页返回条数, 默认30 , 最大30
        is_filter: 是否只返回有内容详情的新闻, 1:是, 默认0
    Returns:
        成功时返回包含新闻字典的列表，失败时返回None
    """
    # 基本参数配置
    apiUrl = 'http://v.juhe.cn/toutiao/index'  # 接口请求URL
    
    # 接口请求入参配置
    requestParams = {
        'key': api_key,
        'type': news_type,
        'page': page,
        'page_size': page_size,
        'is_filter': is_filter,
    }
    try:
        # 发起接口网络请求
        response = requests.get(apiUrl, params=requestParams, timeout=10)
        response.raise_for_status()  # 如果状态码不是200，抛出异常
        
        # 网络请求成功。执行下面的代码
        responseResult = response.json()

        if responseResult['error_code'] != 0:
            print(f"API返回错误: {responseResult['reason']}")
            return None

        # 正常 获取新闻列表
        news_list = []
        # 循环
        for item in responseResult['result']['data']:
            news_list.append({
                'title': item.get('title'),
                'author': item.get('author_name', '未知'),
                'url': item.get('url'),
                'date': item.get('date')
            })
        return news_list
    
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"数据解析失败: {e}")
        return None