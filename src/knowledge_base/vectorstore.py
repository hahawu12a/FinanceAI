"""Vector store management module"""
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)


class VectorStoreManager:
    """管理向量存储"""
    
    def __init__(self, store_type: str = 'milvus', connection_args: Optional[Dict] = None):
        """
        初始化向量存储
        store_type: 'milvus' 或 'pinecone'
        """
        self.store_type = store_type
        self.connection_args = connection_args or {}
        self.vectorstore = None
        logger.info(f"VectorStoreManager初始化: {store_type}")
    
    def create_knowledge_base(self, embeddings, index_name: str = 'finance_knowledge'):
        """创建知识库"""
        try:
            if self.store_type == 'milvus':
                from langchain.vectorstores import Milvus
                connection_args = self.connection_args or {
                    'host': 'localhost',
                    'port': 19530
                }
                self.vectorstore = Milvus(
                    embedding_function=embeddings,
                    connection_args=connection_args,
                    collection_name=index_name
                )
                logger.info(f"Milvus知识库创建成功: {index_name}")
            elif self.store_type == 'pinecone':
                logger.info("Pinecone向量存储待配置")
            else:
                logger.warning(f"未知的向量存储类型: {self.store_type}")
        except Exception as e:
            logger.error(f"知识库创建失败: {e}")
            logger.info("将继续使用基本功能...")
        
        return self.vectorstore
    
    def add_documents(self, documents: List[Dict]):
        """添加文档到向量存储"""
        if not self.vectorstore:
            logger.warning("向量存储未初始化，跳过文档导入")
            return
        
        try:
            texts = [doc['content'] for doc in documents]
            metadatas = [doc.get('metadata', {}) for doc in documents]
            
            self.vectorstore.add_texts(texts, metadatas=metadatas)
            logger.info(f"成功导入{len(documents)}个文档到知识库")
        except Exception as e:
            logger.error(f"添加文档失败: {e}")
    
    def search_similar(self, query: str, k: int = 5):
        """相似度搜索"""
        if not self.vectorstore:
            logger.warning("向量存储未初始化")
            return []
        
        try:
            results = self.vectorstore.similarity_search(query, k=k)
            logger.info(f"相似度搜索完成: 返回{len(results)}个结果")
            return results
        except Exception as e:
            logger.error(f"相似度搜索失败: {e}")
            return []
