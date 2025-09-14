import os
# from langchain.document_loaders import DirectoryLoader        Not working 
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
DATA_PATH = "DATA/books"


def load_documents(DATA_PATH = "DATA/books"):
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"the directory {DATA_PATH} does not exist .Please create it and ")

    loader = DirectoryLoader(path=DATA_PATH,glob="*.txt",loader_cls=TextLoader)
    documents = loader.load()
    return documents


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 300,
    length_function = len,
    add_start_index = True
)   

def read_file(name):
    # print(os.getcwd())
    print(f'reading file: {name}')
    with open(name,"r",  encoding="utf-8") as f:
        lines = f.readlines()
        # print("".join(lines))
        return lines

