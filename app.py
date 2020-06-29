from flask import Flask, request, jsonify
from functions.send_sms import send_sms
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

@app.route("/send-sms", methods=["POST"])
def sms():
    try:
        req = request.json
        result = send_sms(req)
        return jsonify(result)
    except Exception as err:
        return {"statusCode":400, "message":str(err)},400


if __name__ == "__main__":
    app.run(debug=True)
