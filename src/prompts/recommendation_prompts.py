"""Recommendation prompts"""

class RecommendationPrompts:
    
    @staticmethod
    def generate_recommendation_prompt(user_profile: dict) -> str:
        return f"""
Based on user profile, generate investment recommendations:

Risk Level: {user_profile.get('risk_level', 'N/A')}
Amount: {user_profile.get('investment_amount', 'N/A')}
Time Horizon: {user_profile.get('time_horizon', 'N/A')}
Industry Preference: {user_profile.get('industry_preference', [])}

Provide:
1. Specific stock/fund recommendations with codes
2. Allocation percentages
3. Expected returns
4. Risk assessment
5. Implementation plan
"""
