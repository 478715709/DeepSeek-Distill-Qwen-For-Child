from openai import OpenAI
import os

# 初始化 OpenAI 客户端，使用阿里云 DashScope API
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'), # 如果你没有配置环境变量，使用 api_key="your-api-key" 替换
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", # 这里使用的是阿里云的大模型，如果需要使用其他平台，请参考对应的开发文档后对应修改
)

# 调用 API 获取模型回复
response = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}]
    )

# 打印模型回复内容
print(response.choices[0].message.content)