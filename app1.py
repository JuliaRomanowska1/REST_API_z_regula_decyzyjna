from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})
    
@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})
    
@app.route('/hello')
def say_hello():
    name = request.args.get("name", "")
    if name:
        resp = f"Hello {name}!"
    else:
        resp = "Hello!"
    return resp
   
if __name__ == '__main__':
    app.run()
