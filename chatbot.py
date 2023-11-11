import os
import sys
import constant
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = constant.APIKEY

PERSIST = False
PERSIST_DIRECTORY = "persist"
DATA_DIRECTORY = "data/"

query = sys.argv[1] if len(sys.argv) > 1 else None


def load_or_create_index():
    if PERSIST and os.path.exists(PERSIST_DIRECTORY):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=OpenAIEmbeddings())
        return VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        loader = DirectoryLoader(DATA_DIRECTORY)
        creator = VectorstoreIndexCreator(
            vectorstore_kwargs={"persist_directory": PERSIST_DIRECTORY}) if PERSIST else VectorstoreIndexCreator()
        return creator.from_loaders([loader])


index = load_or_create_index()

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)


def chat():
    chat_history = []

    while True:
        global query
        query = query or input("Enter your prompt: ")
        if query in ['q', 'quit']:
            sys.exit()

        result = chain({"question": query, "chat_history": chat_history})
        print(result['answer'])

        chat_history.append((query, result['answer']))
        query = None


if __name__ == "__main__":
    while True:
        chat()
