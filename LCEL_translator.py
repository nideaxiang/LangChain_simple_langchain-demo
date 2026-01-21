from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os

# LangSmith tracing
os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"] = 'xxx'
os.environ["LANGSMITH_PROJECT"] = "TEST"
# 非官方 OpenAI 兼容服务
os.environ["OPENAI_API_BASE"] = "https://api.zhizengzeng.com/v1"
os.environ["OPENAI_API_KEY"] = 'xxx'

# 1. 创建提示模板
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. 创建模型
model = ChatOpenAI(model="gpt-3.5-turbo")

# 3. 创建解析器
parser = StrOutputParser()

# 4. 创建链
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces for translation",
)

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)