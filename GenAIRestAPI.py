import os
from flask import Flask, request
from flask_restful import Resource, Api
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# set GOOGLE_API_KEY to env
os.environ['GOOGLE_API_KEY'] = 'xxxxxx'

# set system proxy if needed
os.environ['http_proxy'] = 'http://127.0.0.1:7897'
os.environ['https_proxy'] = 'http://127.0.0.1:7897'

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

app = Flask(__name__)
api = Api(app)

class GenAIRestAPI(Resource):
    def get(self):
        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "You are a helpful assistant! Your name is Bob.",
                },
                {
                    "type": "text",
                    "text": request.form['data'],
                },
            ]
        )

        result = llm.invoke([message])
        return {'data': result.content}

api.add_resource(GenAIRestAPI, '/chatBot')

if __name__ == '__main__':
    app.run(debug=True)


