import os
from langchain_google_vertexai import ChatVertexAI

# set GOOGLE_APPLICATION_CREDENTIALS (json file) to env
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/EndlessGrief/Downloads/credentials.json'

# set system proxy if needed
# os.environ['http_proxy'] = 'http://127.0.0.1:7897'
# os.environ['https_proxy'] = 'http://127.0.0.1:7897'

# config
chat = ChatVertexAI(
    model="gemini-1.5-flash-001",  # used model 
    temperature=1,                 # Temperature controls the randomness in token selection (higher will be more random)
    max_tokens=2048,               # Output token limit
    max_retries=6,                 # retry times when network not good
    stop=None
)

messages = [
    (
        "system",
        "You are a business analyst, you need to write an email to your customer.",
    ),
    (
        "human", 
        "Write an email because i want to know new progress of the project."
    ),
]

ai_msg = chat.invoke(messages)
ai_msg
