import os 
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()


def main():
    print("Main Function")
    #1 load  the file
    #2 chunk the file
    #3 Embedding & Storing in Vector DB

if __name__ == "__main__":
    main()