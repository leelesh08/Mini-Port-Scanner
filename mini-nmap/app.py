import sqlite3
from db import init_db
from flask import Flask, render_template, request
from scanner import scan_ports
from db import init_db,save_scan_to_db, get_scan_history

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        target = request.form['target']
        start_port = int(request.form['start_port'])
        end_port = int(request.form['end_port'])
        results = scan_ports(target, start_port, end_port)
        save_scan_to_db(target, results)
    history = get_scan_history()
    return render_template('index.html', results=results, history=history)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
