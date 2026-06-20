"""Analysis prompts templates"""

class AnalysisPrompts:
    
    @staticmethod
    def policy_analysis_prompt(policy_text: str) -> str:
        return f"""
Analyze the following policy:

{policy_text}

Provide analysis on:
1. Policy background
2. Core measures
3. Positive and negative industries
4. Market reaction prediction
5. Investment recommendations
6. Risk factors
"""
    
    @staticmethod
    def stock_analysis_prompt(stock_data: dict) -> str:
        return f"""
Analyze the following company:

Code: {stock_data.get('code', 'N/A')}
Name: {stock_data.get('name', 'N/A')}
Industry: {stock_data.get('industry', 'N/A')}
Price: {stock_data.get('current_price', 'N/A')}

Provide comprehensive analysis including:
1. Fundamental analysis
2. Valuation analysis
3. Technical analysis
4. Risk assessment
"""
    
    @staticmethod
    def fund_analysis_prompt(fund_data: dict) -> str:
        return f"""
Analyze the following fund:

Code: {fund_data.get('code', 'N/A')}
Name: {fund_data.get('name', 'N/A')}
Type: {fund_data.get('type', 'N/A')}

Provide analysis on:
1. Fund manager assessment
2. Strategy analysis
3. Historical performance
4. Fee level
5. Peer comparison
"""
