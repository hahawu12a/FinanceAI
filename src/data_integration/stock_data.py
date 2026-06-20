"""Stock data integration module"""
import tushare as ts
import pandas as pd
from datetime import datetime, timedelta
import logging
from config.settings import TUSHARE_API_TOKEN

logger = logging.getLogger(__name__)


class StockDataIntegrator:
    """获取和处理股票数据"""
    
    def __init__(self, api_token: str = None):
        self.api_token = api_token or TUSHARE_API_TOKEN
        try:
            self.pro = ts.pro_api(self.api_token)
            self.logger = logging.getLogger(__name__)
        except Exception as e:
            logger.error(f"Tushare API初始化失败: {e}")
            self.pro = None
    
    def get_stock_basic_info(self):
        """获取A股基础信息"""
        if not self.pro:
            logger.error("Tushare API未初始化")
            return None
        
        try:
            df = self.pro.stock_basic(
                exchange='',
                list_status='L',  # L上市 D退市 P暂停上市
                fields='ts_code,symbol,name,area,industry,market,list_date'
            )
            logger.info(f"成功获取{len(df)}只股票基础信息")
            return df
        except Exception as e:
            logger.error(f"获取股票基础信息失败: {e}")
            return None
    
    def get_stock_daily(self, ts_code: str, start_date: str = None, end_date: str = None):
        """获取日线行情数据"""
        if not self.pro:
            logger.error("Tushare API未初始化")
            return None
        
        try:
            if end_date is None:
                end_date = datetime.now().strftime('%Y%m%d')
            if start_date is None:
                start_date = (datetime.now() - timedelta(days=250)).strftime('%Y%m%d')
            
            df = self.pro.daily(
                ts_code=ts_code,
                start_date=start_date,
                end_date=end_date,
                fields='ts_code,trade_date,open,high,low,close,vol,amount'
            )
            logger.info(f"成功获取{ts_code}的日线数据: {len(df)}行")
            return df
        except Exception as e:
            logger.error(f"获取股票日线数据失败: {e}")
            return None
    
    def get_stock_financial_report(self, ts_code: str):
        """获取财务报表数据"""
        if not self.pro:
            logger.error("Tushare API未初始化")
            return None
        
        try:
            df = self.pro.query('fina_indicator', ts_code=ts_code,
                               fields='ts_code,ann_date,roe,debt_to_assets,current_ratio')
            logger.info(f"成功获取{ts_code}的财务数据")
            return df
        except Exception as e:
            logger.error(f"获取财务报表失败: {e}")
            return None
    
    def calculate_technical_indicators(self, ts_code: str, end_date: str = None):
        """计算技术指标"""
        if end_date is None:
            end_date = datetime.now().strftime('%Y%m%d')
        
        start_date = (datetime.now() - timedelta(days=250)).strftime('%Y%m%d')
        df = self.get_stock_daily(ts_code, start_date, end_date)
        
        if df is None or len(df) == 0:
            logger.warning(f"无法计算{ts_code}的技术指标")
            return None
        
        try:
            df = df.sort_values('trade_date')
            
            # 计算移动平均线
            df['ma_5'] = df['close'].rolling(5).mean()
            df['ma_20'] = df['close'].rolling(20).mean()
            df['ma_60'] = df['close'].rolling(60).mean()
            
            # 计算RSI
            df['rsi'] = self._calculate_rsi(df['close'], 14)
            
            logger.info(f"成功计算{ts_code}的技术指标")
            return df
        except Exception as e:
            logger.error(f"计算技术指标失败: {e}")
            return None
    
    @staticmethod
    def _calculate_rsi(prices, period=14):
        """计算相对强弱指标"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
