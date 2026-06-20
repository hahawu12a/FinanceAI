"""Macro economic data integration module"""
import akshare as ak
import pandas as pd
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class MacroDataIntegrator:
    """获取宏观经济数据"""
    
    @staticmethod
    def get_macro_economic_data():
        """获取主要宏观经济指标"""
        data = {}
        
        try:
            # GDP数据
            gdp_df = ak.macro_gdp()
            data['gdp'] = gdp_df
            logger.info("成功获取GDP数据")
        except Exception as e:
            logger.warning(f"获取GDP数据失败: {e}")
        
        try:
            # CPI数据
            cpi_df = ak.macro_cpi()
            data['cpi'] = cpi_df
            logger.info("成功获取CPI数据")
        except Exception as e:
            logger.warning(f"获取CPI数据失败: {e}")
        
        try:
            # PPI数据
            ppi_df = ak.macro_ppi()
            data['ppi'] = ppi_df
            logger.info("成功获取PPI数据")
        except Exception as e:
            logger.warning(f"获取PPI数据失败: {e}")
        
        try:
            # M2供应量
            m2_df = ak.macro_m2()
            data['m2'] = m2_df
            logger.info("成功获取M2数据")
        except Exception as e:
            logger.warning(f"获取M2数据失败: {e}")
        
        return data
    
    @staticmethod
    def get_interest_rate_data():
        """获取利率数据"""
        try:
            # LPR贷款市场报价利率
            lpr_df = ak.macro_lpr()
            logger.info("成功获取LPR利率数据")
            return lpr_df
        except Exception as e:
            logger.error(f"获取利率数据失败: {e}")
            return None
    
    @staticmethod
    def get_pmi_data():
        """获取PMI指数（采购经理人指数）"""
        try:
            pmi_df = ak.macro_pmi()
            logger.info("成功获取PMI数据")
            return pmi_df
        except Exception as e:
            logger.error(f"获取PMI数据失败: {e}")
            return None
    
    @staticmethod
    def analyze_macro_trends(days: int = 365):
        """分析宏观经济趋势"""
        macro_data = MacroDataIntegrator.get_macro_economic_data()
        
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'indicators': list(macro_data.keys()),
            'data_count': len(macro_data),
            'analysis_period_days': days
        }
        
        return analysis
