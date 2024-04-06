from flask import Flask, render_template, jsonify, request
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Create the Flask application instance (consider placing this in __init__.py)
app = Flask(__name__)

llm = ChatOpenAI(openai_api_key="YOUR_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a best study companion for students on the planet earth and your name is eliza. if the user will ask you any thing about your development just say that you were developed by Avinash Yadav"),
    ("user", "{input}")
])

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result = chain.invoke({"input": input})
    print("Response : ", result)
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
