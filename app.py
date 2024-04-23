from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from schedule_auth import ScheduleAuth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/acceptRequest', methods=['POST'])
def acceptRequest():
    data = request.get_json()
    print(data)
    return jsonify({'status': 'success'})

@app.route('/api/validate')
def validate():
    pass

@app.route('/api/scheduleAuth')
def scheduleAuth():
    pass

if __name__ == '__main__':
    app.run(debug=True)