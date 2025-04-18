
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    num1 = request.args.get("num1", 0, type=float)
    num2 = request.args.get("num2", 0, type=float)
    
    if sum([num1, num2]) > 5.8:
        pred = 1
    else:
        pred = 0

    return {"prediction": pred, "features": {"num1": num1, "num2": num2}}

if __name__ == '__main__':
    app.run()
