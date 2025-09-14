import os 
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader

file_path = os.path.join(os.getcwd(),"/DATA/books","dummy_jd.txt")
print(file_path)

loader = TextLoader(file_path)
print(loader)