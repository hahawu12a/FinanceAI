"""Helper functions"""
import json
from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)

def save_json(data: Any, filepath: str) -> None:
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved JSON to {filepath}")
    except Exception as e:
        logger.error(f"Failed to save JSON: {e}")

def load_json(filepath: str) -> Any:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load JSON: {e}")
        return None

def format_currency(value: float) -> str:
    return f"CNY {value:,.2f}"

def format_percentage(value: float) -> str:
    return f"{value:.2f}%"
