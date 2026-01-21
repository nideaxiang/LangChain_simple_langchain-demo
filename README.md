# LangChain 翻译服务示例项目

这是一个基于 LangChain、FastAPI 和 LangServe 构建的简单翻译服务示例项目。项目展示了如何使用 LangChain Expression Language (LCEL) 构建链式处理流程，并通过 REST API 提供服务。

## 项目结构

```
.
├── LCEL_translator.py      # 服务端：FastAPI + LangServe 翻译服务
├── LCEL_translator_client.py  # 客户端：调用翻译服务的示例
└── README.md               # 项目说明文档
```

## 功能特点

- 使用 LangChain Expression Language (LCEL) 构建 `prompt → model → parser` 处理链
- 通过 FastAPI + LangServe 提供 RESTful API 服务
- 支持调用兼容 OpenAI API 的第三方模型服务
- 集成 LangSmith 进行链路追踪和监控
- 提供客户端调用示例

## 快速开始

### 1. 环境准备

```bash
# 安装依赖
pip install fastapi langchain-core langchain-openai langserve uvicorn
```

### 2. 配置环境变量

在运行前，请设置以下环境变量：

```bash
# LangSmith 配置（可选，用于链路追踪）
export LANGCHAIN_TRACING=true
export LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
export LANGSMITH_API_KEY="your_langsmith_api_key"
export LANGSMITH_PROJECT="TEST"

# OpenAI 兼容 API 配置
export OPENAI_API_BASE="https://api.zhizengzeng.com/v1"
export OPENAI_API_KEY="your_openai_api_key"
```

### 3. 启动服务端

```bash
python LCEL_translator.py
```

服务将在 `http://localhost:8000` 启动。

### 4. 使用客户端调用

```bash
python LCEL_translator_client.py
```

示例输出：
```
Ciao
```

## API 接口说明

### 翻译接口

- **端点**: `POST /chain`
- **请求格式**:
```json
{
  "language": "目标语言（如：Italian, French, Spanish 等）",
  "text": "需要翻译的文本"
}
```
- **响应**: 返回翻译后的字符串

### 自动生成的 API 文档

启动服务后，可以通过以下地址访问 API 文档：
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 项目核心代码解析

### 服务端 (LCEL_translator.py)

1. **提示模板构建**：创建可接收 `language` 和 `text` 参数的翻译提示
2. **模型配置**：使用 `ChatOpenAI` 连接兼容 OpenAI 的 API 服务
3. **输出解析**：使用 `StrOutputParser` 解析模型输出
4. **链式组合**：使用 `|` 运算符组合 `prompt_template | model | parser`
5. **服务部署**：通过 `add_routes` 将链暴露为 API 端点

### 客户端 (LCEL_translator_client.py)

使用 `RemoteRunnable` 轻松调用远程 LangChain 服务，无需手动处理 HTTP 请求。

## 配置说明

### LangSmith 集成

项目已集成 LangSmith 用于：
- 跟踪和可视化 LangChain 链的执行
- 监控模型性能和调用统计
- 调试和分析处理流程

### 模型服务配置

默认使用兼容 OpenAI API 的第三方服务，可替换为：
1. 官方 OpenAI API
2. Azure OpenAI
3. 其他兼容服务

修改 `OPENAI_API_BASE` 和 `OPENAI_API_KEY` 即可切换服务。

## 扩展建议

1. **添加认证**：在 `add_routes` 中配置认证中间件
2. **支持流式响应**：使用 `stream` 方法实现实时翻译
3. **批量处理**：添加批量翻译接口
4. **多语言支持**：扩展支持的语言列表和语言检测
5. **缓存机制**：添加翻译结果缓存提高性能

## 依赖项

- fastapi >= 0.104.0
- langchain-core >= 0.1.0
- langchain-openai >= 0.0.2
- langserve >= 0.0.34
- uvicorn >= 0.24.0

## 许可证：无
