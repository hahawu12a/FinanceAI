from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="FinanceAI",
    version="0.1.0",
    author="hahawu12a",
    description="AI-powered financial investment advisor system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hahawu12a/FinanceAI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "langchain>=0.0.300",
        "openai>=0.27.0",
        "tushare>=1.2.95",
        "pandas>=1.5.0",
        "numpy>=1.23.0",
    ],
)
