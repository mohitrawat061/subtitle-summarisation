from flask import Flask, jsonify, render_template
from flask import request

from summarizer import *

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html", name="hey")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['link']
      result = result.split("=", 1)[1]
      summary_and_subs = generate_summary(result, 2)
      return render_template("result.html", result=summary_and_subs)


@app.route('/sendSubtitles', methods=['POST'])
def sendSubtitles():
    try:
        data = request.get_json()
        return jsonify({'status': 'OK', 'data': data["data"]})
    except Exception:
        return jsonify({'status': 'FAILED'})

@app.route('/getSummary', methods=['GET'])
def getSummary():
    return "Summarized data"

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8081, debug=True)