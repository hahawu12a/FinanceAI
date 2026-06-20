# FinanceAI - 智能财经投资顾问系统

一个基于大语言模型的AI财经经理系统，提供投资建议、政策分析和具体投资标的推荐。

## 🎯 功能模块

- 📊 **金融知识库** - 向量化存储投资理论、政策文档、行业分析
- 📈 **数据集成** - 实时获取股票、基金、宏观经济数据
- 🎯 **政策分析** - 解读政策内容并评估投资影响
- 💡 **投资推荐** - 生成具体的标的推荐（股票代码、基金代码、公司）
- 📉 **风险评估** - 多维度评估投资风险
- 🤖 **AI对话** - 实时与投资顾问交互

## 📁 项目结构

```
FinanceAI/
├── config/                 # 配置文件
│   ├── __init__.py
│   └── settings.py
├── data/                   # 数据目录
│   ├── raw/               # 原始数据
│   ├── processed/         # 处理后的数据
│   └── knowledge_base/    # 知识库
│       └── policies/      # 政策文档
├── src/                   # 源代码
│   ├── __init__.py
│   ├── advisor.py         # 主AI顾问类
│   ├── data_integration/  # 数据集成模块
│   │   ├── __init__.py
│   │   ├── stock_data.py
│   │   ├── fund_data.py
│   │   ├── macro_data.py
│   │   └── policy_data.py
│   ├── knowledge_base/    # 知识库模块
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   └── document_loader.py
│   ├── analysis/          # 分析模块
│   │   ├── __init__.py
│   │   ├── policy_analyzer.py
│   │   ├── stock_analyzer.py
│   │   └── fund_analyzer.py
│   ├── prompts/           # 提示词模板
│   │   ├── __init__.py
│   │   ├── system_prompts.py
│   │   ├── analysis_prompts.py
│   │   └── recommendation_prompts.py
│   └── utils/             # 工具函数
│       ├── __init__.py
│       ├── logger.py
│       └── helpers.py
├── scripts/               # 脚本
│   ├── init_knowledge_base.py
│   └── data_update.py
├── tests/                 # 测试
│   ├── __init__.py
│   ├── test_data_integration.py
│   ├── test_knowledge_base.py
│   └── test_advisor.py
├── notebooks/             # Jupyter笔记本
│   └── exploration.ipynb
├── main.py               # 入口点
├── requirements.txt      # 依赖
├── setup.py             # 安装脚本
├── .env.example         # 环境变量示例
└── .gitignore          # Git忽略文件
```

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/hahawu12a/FinanceAI.git
cd FinanceAI
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
```bash
cp .env.example .env
# 编辑.env填入你的API密钥
```

### 4. 初始化知识库
```bash
python scripts/init_knowledge_base.py
```

### 5. 运行系统
```bash
python main.py
```

## 📚 核心功能使用

### 政策分析
```python
from src.advisor import FinanceAdvisor

advisor = FinanceAdvisor()
policy_analysis = advisor.analyze_policy(
    policy_text="最新货币政策内容",
    industry_focus=["科技", "消费"]
)
```

### 投资推荐
```python
recommendation = advisor.recommend_investment(
    user_profile={
        "risk_level": "中等",
        "investment_amount": 100000,
        "time_horizon": "2年",
        "industry_preference": ["科技", "新能源"]
    }
)
```

### AI对话
```python
response = advisor.chat("如何看待当前的科技股行情？")
print(response)
```

## 🛠 技术栈

- **LLM框架**: LangChain
- **向量数据库**: Milvus / Pinecone
- **数据获取**: Tushare, AkShare
- **嵌入模型**: OpenAI Embeddings / Huggingface
- **API框架**: FastAPI (可选)
- **数据处理**: Pandas, NumPy
- **日志**: Loguru

## 📊 主要数据源

| 数据类型 | 来源 | 说明 |
|---------|------|------|
| A股行情 | Tushare | 实时股票数据、财报 |
| 基金数据 | AkShare | 基金净值、持仓 |
| 宏观数据 | 国家统计局 | GDP、CPI等经济指标 |
| 政策文档 | 新华网、央行 | 政策解读文档 |
| 投资理论 | 自建 | 投资框架、案例分析 |

## 🎓 模块说明

### data_integration（数据集成）
负责从各个数据源获取实时数据：
- `stock_data.py` - A股数据、技术指标计算
- `fund_data.py` - 基金净值、持仓、业绩
- `macro_data.py` - GDP、CPI、PMI等宏观指标
- `policy_data.py` - 政策文档分类和存储

### knowledge_base（知识库）
实现向量化知识存储和检索：
- `embeddings.py` - 文本嵌入管理
- `vectorstore.py` - 向量数据库管理
- `document_loader.py` - 知识库文档加载

### analysis（分析）
提供不同维度的分析能力：
- `policy_analyzer.py` - 政策影响分析
- `stock_analyzer.py` - 个股基本面、技术面分析
- `fund_analyzer.py` - 基金评估

### prompts（提示词）
管理AI的系统提示和任务提示：
- `system_prompts.py` - 系统级提示词
- `analysis_prompts.py` - 分析任务提示词
- `recommendation_prompts.py` - 投资推荐提示词

## ⚙️ 配置说明

### 环境变量（.env）
```bash
# OpenAI API
OPENAI_API_KEY=your_key_here

# Tushare API
TUSHARE_API_TOKEN=your_token_here

# Milvus向量数据库
MILVUS_HOST=localhost
MILVUS_PORT=19530

# LLM配置
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2000

# 日志配置
DEBUG=True
LOG_LEVEL=INFO
```

## 🧪 测试

运行测试套件：
```bash
pytest tests/
```

## 📈 项目进度

- [x] 基础项目架构
- [x] 数据集成模块
- [x] 知识库系统
- [x] 提示词框架
- [x] AI顾问类
- [ ] LLM集成（GPT-4/Claude）
- [ ] 前端UI界面
- [ ] 实时更新脚本
- [ ] 性能优化
- [ ] 部署到云平台

## ⚠️ 免责声明

**重要**: 本系统生成的分析和建议仅供参考，**不构成任何投资建议**。
- 使用者需自行承担所有投资风险
- 市场存在不确定性，过往表现不代表未来收益
- 建议在投资前进行充分的尽职调查

## 📝 使用许可

MIT License - 详见 LICENSE 文件

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 贡献流程
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📞 联系方式

- GitHub: [@hahawu12a](https://github.com/hahawu12a)
- 问题反馈: [Issues](https://github.com/hahawu12a/FinanceAI/issues)

## 🙏 致谢

感谢以下开源项目的支持：
- LangChain - LLM应用框架
- Tushare - A股数据接口
- AkShare - 金融数据聚合
- Milvus - 向量数据库
