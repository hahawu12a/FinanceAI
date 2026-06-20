"""Fund data integration module"""
import akshare as ak
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class FundDataIntegrator:
    """获取和处理基金数据"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def get_fund_basic_info(self):
        """获取基金基本信息"""
        try:
            fund_df = ak.fund_info_sina()
            logger.info(f"成功获取{len(fund_df)}只基金基本信息")
            return fund_df
        except Exception as e:
            logger.error(f"获取基金基本信息失败: {e}")
            return None
    
    def get_fund_daily_value(self, fund_code: str):
        """获取基金净值历史"""
        try:
            fund_value_df = ak.fund_sina_daily(symbol=fund_code)
            logger.info(f"成功获取基金{fund_code}的净值数据: {len(fund_value_df)}行")
            return fund_value_df
        except Exception as e:
            logger.error(f"获取基金{fund_code}数据失败: {e}")
            return None
    
    def get_fund_portfolio(self, fund_code: str):
        """获取基金持仓信息"""
        try:
            portfolio_df = ak.fund_portfolio_hold_sina(symbol=fund_code)
            logger.info(f"成��获取基金{fund_code}的持仓数据")
            return portfolio_df
        except Exception as e:
            logger.error(f"获取基金持仓失败: {e}")
            return None
    
    def get_fund_performance(self, fund_code: str):
        """获取基金业绩数据"""
        try:
            perf_df = ak.fund_performance_sina(symbol=fund_code)
            logger.info(f"成功获取基金{fund_code}的业绩数据")
            return perf_df
        except Exception as e:
            logger.error(f"获取基金业绩失败: {e}")
            return None
    
    def filter_funds_by_criteria(self, criteria: dict):
        """按条件筛选基金
        criteria: {
            'fund_type': '混合型',
            'return_1y': (0.1, 1),
            'risk_level': 'medium',
        }
        """
        funds = self.get_fund_basic_info()
        
        if funds is None:
            return None
        
        # 按类型筛选
        if 'fund_type' in criteria:
            funds = funds[funds['type'] == criteria['fund_type']]
        
        logger.info(f"筛选基金完成: {len(funds)}只")
        return funds
