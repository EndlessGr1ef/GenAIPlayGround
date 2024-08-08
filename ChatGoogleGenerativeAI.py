import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# set GOOGLE_API_KEY to env
os.environ['GOOGLE_API_KEY'] = 'xxxxxxxxxxxxxxxxxxxx'

# set system proxy if needed
# os.environ['http_proxy'] = 'http://127.0.0.1:7897'
# os.environ['https_proxy'] = 'http://127.0.0.1:7897'

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Tell me the full content in this image the same like the image.",
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": "/Users/EndlessGrief/Documents/GitHub/GenAIPlayGround/image.png"},
    ]
)

# The value of image_url can be any of the following:
# A public image URL
# A gcs file (e.g., "gcs://path/to/file.png")
# A local file path
# A base64 encoded image (e.g., data:image/png;base64,abcd124)
# A PIL image

llm.invoke([message])