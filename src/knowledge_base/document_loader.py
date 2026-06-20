"""Document loader for knowledge base"""
import json
from datetime import datetime
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)


class FinanceDocumentLoader:
    """财经文档加载器"""
    
    def __init__(self, data_dir: str = 'data/knowledge_base/'):
        self.data_dir = data_dir
        self.documents = []
        logger.info(f"FinanceDocumentLoader初始化, 数据目录: {data_dir}")
    
    def load_investment_theory_documents(self) -> List[Dict]:
        """加载投资理论文档"""
        docs = []
        
        theory_content = {
            'value_investing': """
价值投资理论：
1. 核心理念：投资价值低估的公司
2. 评估方法：
   - PE比率（市盈率）
   - PB比率（市净率）
   - DCF贴现现金流模型
3. 风险控制：安全边际（20-30%折扣）
4. 经典投资者：巴菲特、芒格
5. 关键指标：
   - ROE > 12%
   - 负债率 < 40%
   - 现金流充足
            """,
            'growth_investing': """
成长投资理论：
1. 核心理念：投资高增长潜力的公司
2. 关键指标：
   - 营收增长率 > 20%
   - 净利润增长率 > 30%
   - ROE > 15%
3. 适用行业：科技、消费升级、新能源
4. 风险：估值过高、增长放缓
5. 适合时期：经济扩张期
            """,
            'dividend_investing': """
分红投资理论：
1. 核心理念：获取稳定的分红收益
2. 选择标准：
   - 分红率 > 2%
   - 连续分红 > 10年
   - 现金流充足
3. 适用标的：公用事业、房地产信托
4. 优势：稳定现金流、复利效应
5. 风险：利率上升压力
            """,
        }
        
        for theory_type, content in theory_content.items():
            doc = {
                'content': content,
                'metadata': {
                    'source': 'investment_theory',
                    'category': theory_type,
                    'date': datetime.now().isoformat(),
                    'type': 'theory'
                }
            }
            docs.append(doc)
        
        logger.info(f"加载{len(docs)}个投资理论文档")
        return docs
    
    def load_policy_analysis_framework(self) -> List[Dict]:
        """加载政策分析框架"""
        framework = {
            'content': """
政策分析框架：

1. 政策识别
   - 政策类型：货币政策、财政政策、产业政策
   - 发布机构：央行、财政部、发改委
   - 发布时间：紧急vs常规

2. 政策内容解析
   - 核心措施
   - 实施时间表
   - 预期目标
   - 约束条件

3. 影响评估
   - 直接受益方：哪些行业/公司
   - 直接受损方：风险行业
   - 间接效应：连锁反应

4. 市场反应预测
   - 短期冲击（1-3个月）
   - 中期影响（3-12个月）
   - 长期趋势（1-3年）

5. 投资策略调整
   - 增持/新建头寸
   - 减持/止损头寸
   - 回避风险
            """,
            'metadata': {
                'source': 'analysis_framework',
                'category': 'policy_analysis',
                'date': datetime.now().isoformat(),
                'type': 'framework'
            }
        }
        logger.info("加载政策分析框架")
        return [framework]
    
    def load_industry_analysis_framework(self) -> List[Dict]:
        """加载行业分析框架（PEST + SWOT）"""
        framework = {
            'content': """
行业分析框架：

PEST分析：
- Political（政治）：监管政策、税收优惠
- Economic（经济）：GDP增速、通胀率、利率
- Social（社会）：人口结构、消费趋势
- Technological（技术）：创新速度、技术替代

SWOT分析：
- Strengths（优势）：行业竞争优势
- Weaknesses（劣势）：行业短板
- Opportunities（机会）：发展潜力
- Threats（威胁）：风险因素

关键财务指标：
- ROE（净资产收益率）> 10%
- ROIC（投资资本回报率）
- 毛利率、净利率
- 现金流转化率
- 债务杠杆率
            """,
            'metadata': {
                'source': 'analysis_framework',
                'category': 'industry_analysis',
                'date': datetime.now().isoformat(),
                'type': 'framework'
            }
        }
        logger.info("加载行业分析框架")
        return [framework]
    
    def load_valuation_methods(self) -> List[Dict]:
        """加载估值方法"""
        methods = {
            'content': """
估值方法合集：

1. 相对估值法
   PE估值：股价 / 每股收益
   PB估值：股价 / 每股净资产
   PS估值：市值 / 销售收入
   PEG估值：PE / 利润增长率

2. 绝对估值法（DCF）
   企业价值 = 未来现金流折现
   步骤：
   - 预测5-10年FCF
   - 计算终端价值
   - 按WACC折现
   - 减去债务得股权价值

3. 资产估值法
   适用于：房地产、金融资产公司
   净资产价值 = 总资产 - 总负债

4. 可比公司法
   选择可比上市公司
   获取其估值倍数
   应用到目标公司
            """,
            'metadata': {
                'source': 'analysis_framework',
                'category': 'valuation',
                'date': datetime.now().isoformat(),
                'type': 'method'
            }
        }
        logger.info("加载估值方法")
        return [methods]
    
    def load_all_documents(self) -> List[Dict]:
        """加载所有知识库文档"""
        all_docs = []
        
        all_docs.extend(self.load_investment_theory_documents())
        all_docs.extend(self.load_policy_analysis_framework())
        all_docs.extend(self.load_industry_analysis_framework())
        all_docs.extend(self.load_valuation_methods())
        
        logger.info(f"总共加载{len(all_docs)}个知识库文档")
        return all_docs
