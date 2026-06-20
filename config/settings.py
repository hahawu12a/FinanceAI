"""Global settings and configuration"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')

# Tushare Configuration
TUSHARE_API_TOKEN = os.getenv('TUSHARE_API_TOKEN')

# Milvus Configuration
MILVUS_HOST = os.getenv('MILVUS_HOST', 'localhost')
MILVUS_PORT = int(os.getenv('MILVUS_PORT', '19530'))

# Pinecone Configuration (Optional)
PINCONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINCONE_ENVIRONMENT = os.getenv('PINECONE_ENVIRONMENT')

# Debug Configuration
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Data Paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
KNOWLEDGE_BASE_DIR = os.path.join(DATA_DIR, 'knowledge_base')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Ensure directories exist
for directory in [DATA_DIR, KNOWLEDGE_BASE_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR]:
    os.makedirs(directory, exist_ok=True)

# Embedding Configuration
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'openai')
EMBEDDING_DIMENSION = int(os.getenv('EMBEDDING_DIMENSION', '1536'))

# Vector Store Configuration
VECTOR_STORE_TYPE = os.getenv('VECTOR_STORE_TYPE', 'milvus')
KNOWLEDGE_BASE_INDEX = os.getenv('KNOWLEDGE_BASE_INDEX', 'finance_knowledge')

# LLM Configuration
LLM_TEMPERATURE = float(os.getenv('LLM_TEMPERATURE', '0.3'))
LLM_MAX_TOKENS = int(os.getenv('LLM_MAX_TOKENS', '2000'))

# Analysis Configuration
ANALYSIS_LOOKBACK_DAYS = int(os.getenv('ANALYSIS_LOOKBACK_DAYS', '250'))
TECHNICAL_INDICATORS_PERIODS = {
    'short': 5,
    'medium': 20,
    'long': 60
}
