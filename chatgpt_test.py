import requests
import random
import string
import json
import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"调用chatgpt耗时{end_time - start_time:.6f} s.")
        return result

    return wrapper


@timer_decorator
def send_chat_message(input_text, avoidRepeatable):
    url = "https://api.nextera.chat/webflux/api/chat"

    headers = {
        'Gpt-Auth-Token': '1c8461e74df9ae38',
        'Content-Type': 'application/json',
        'Accept': 'text/event-stream'
    }

    data = {
        "sessionType": "chat",
        "settingCode": "55c161ef53ff7dfe3fb425a45feebee3",
        "sessionIdentifier": "61dce617c5d3422285e0badfc9964d71",
        "stream": "true",
        "content": input_text,
        "callbackUrl": "callback",
        "avoidRepeatable": avoidRepeatable
    }

    response = requests.post(url, headers=headers, json=data)
    return response


def split_chat_json(data):
    json_blocks = data.strip().split("\ndata:")
    # 取最后一个 JSON 数据块
    last_json_data = json_blocks[-1]

    last_json_object = json.loads(last_json_data)
    output = last_json_object['result']['choices'][0]['message']['content']
    return output

def topic_extraction_model_results(input_text):
    # 调用函数并传入 avoidRepeatable 参数
    common_input_dic_text = """
    假设你现在是一个主题提取模型，当我输入的是一句话时，你只输出这段文字对应的意图和实体。
    现在有两个主题，一个是问某种事物是什么概念，一个是求销量。

    问销量的例子如下，当输入为“我想知道前三个月大众汽车的销量平均值”时的具体输出示例：{
    "主题": "计算销量",   
    "统计指标": "平均值",  
     "时间": "前三个月",  
     "车辆": "大众"}。

    问概念的例子如下，当输入为“我想知道进站客户是什么意思“时的具体输出示例：{
    "类型": "问概念",   
    "主题": "进站客户"}

     以下是我的提问："""
    input_text = common_input_dic_text + input_text
    avoidRepeatable_value = ''.join(random.choice(string.digits) for _ in range(10))
    try:
        response = send_chat_message(input_text, avoidRepeatable_value)
        output = split_chat_json(response.text)
        return output
    except Exception as e:
        print(e)



if __name__ == '__main__':
    input_text_01 = "宝马汽车的上个月的销量总和是多少？"
    input_text_02 = "库存安全线是什么意思？"

    print(topic_extraction_model_results(input_text_01))
    print(topic_extraction_model_results(input_text_02))