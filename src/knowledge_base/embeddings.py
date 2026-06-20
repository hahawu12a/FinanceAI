"""Embeddings management module"""
from typing import Optional
import os
import logging

logger = logging.getLogger(__name__)


class EmbeddingManager:
    """管理文本嵌入"""
    
    def __init__(self, model_type: str = 'openai', model_name: Optional[str] = None):
        """
        初始化嵌入模型
        model_type: 'openai' 或 'huggingface' 或 'local'
        """
        self.model_type = model_type
        self.embeddings = None
        
        try:
            if model_type == 'openai':
                from langchain.embeddings import OpenAIEmbeddings
                self.embeddings = OpenAIEmbeddings(
                    openai_api_key=os.getenv('OPENAI_API_KEY'),
                    model='text-embedding-3-small'
                )
                logger.info("OpenAI Embedding模型初始化成功")
            elif model_type == 'huggingface':
                from langchain.embeddings import HuggingFaceEmbeddings
                model_name = model_name or 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
                self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
                logger.info(f"HuggingFace Embedding模型({model_name})初始化成功")
            else:
                # 本地模型
                from langchain.embeddings import HuggingFaceEmbeddings
                self.embeddings = HuggingFaceEmbeddings(
                    model_name='sentence-transformers/all-MiniLM-L6-v2'
                )
                logger.info("本地Embedding模型初始化成功")
        except Exception as e:
            logger.error(f"Embedding模型初始化失败: {e}")
            raise
    
    def embed_text(self, text: str):
        """嵌入单个文本"""
        if not self.embeddings:
            raise ValueError("Embeddings not initialized")
        return self.embeddings.embed_query(text)
    
    def embed_documents(self, documents: list):
        """嵌入文档列表"""
        if not self.embeddings:
            raise ValueError("Embeddings not initialized")
        return self.embeddings.embed_documents(documents)
