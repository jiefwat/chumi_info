

import requests
import matplotlib.pyplot as plt

def get_stock_price(stock_code):
    url = f"https://stock.finance.sina.com.cn/realstock/company/{stock_code}/gsgs.shtml"
    response = requests.get(url)
    data = response.text
    print(data)
    start_price = float(data.split('开盘价:')[1].split()[0])
    end_price = float(data.split('现价:')[1].split()[0])
    return start_price, end_price

def plot_stock_price(stock_code):
    # 获取股票价格
    start_price, end_price = get_stock_price(stock_code)
    
    # 绘制价格变化图
    plt.figure(figsize=(10, 6))
    plt.plot(['开盘价', '现价'], [start_price, end_price], marker='o')
    plt.title(f"{stock_code} 股票价格")
    plt.xlabel('时间')
    plt.ylabel('价格')
    plt.grid(True)
    plt.show()

# 使用股票代码查询并绘制图形
stock_code = "603536"  # 举例: 贵州茅台的股票代码
plot_stock_price(stock_code)
