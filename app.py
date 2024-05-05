import json
import secrets
from datetime import datetime

from flask import Flask, redirect, url_for

from timer import CheckInTimer

app = Flask(__name__)

check_in_timers = {}

@app.route('/')
def hello_geek():
    return 'Hello from Flask'

@app.route('/timeout/')
def timeout_new():
    timeout_id = secrets.token_urlsafe(10)
    check_in_timers[timeout_id] = CheckInTimer(300)
    return redirect(url_for('timeout_check', timeout_id=timeout_id))

@app.route('/timeout/<timeout_id>')
def timeout_check(timeout_id):
    return (json.dumps(check_in_timers[timeout_id].check_in()), {'Content-Type': 'application/json'})

@app.route('/timeout/<timeout_id>/reset')
def reset(timeout_id):
    check_in_timers[timeout_id] = CheckInTimer(300) # reset the old timer with a new timer
    return redirect(url_for('timeout_check', timeout_id=timeout_id))

if __name__ == "__main__":
    app.run(debug=True)
