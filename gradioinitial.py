import os
import json
from typing import List, Dict, Tuple

import openai
import gradio as gr

# TODO: 设置你的 OPENAI API 密钥，这里假设 DashScope API 被配置在了 OPENAI_API_KEY 环境变量中
OPENAI_API_KEY = ""
# 不填写则默认使用环境变量
if not OPENAI_API_KEY:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# 初始化 OpenAI 客户端，使用阿里云 DashScope API
client = openai.OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里云的 API 地址
)

# 检查 API 设置是否正确
try:
    response = client.chat.completions.create(
        model="qwen-turbo",  # 使用通义千问-Turbo 大模型，可以替换为 Deepseek 系列：deepseek-v3 / deepseek-r1
        messages=[{'role': 'user', 'content': "测试"}],
        max_tokens=1,
    )
    print("API 设置成功！！")
except Exception as e:
    print(f"API 可能有问题，请检查：{e}")