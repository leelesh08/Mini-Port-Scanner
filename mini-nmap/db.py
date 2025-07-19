import sqlite3

def init_db():
    conn = sqlite3.connect('scan_history.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            host TEXT NOT NULL,
            ports TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_scan_to_db(target, ports):
    conn = sqlite3.connect('scan_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO scans (host, ports) VALUES (?, ?)", (target, str(ports)))
    conn.commit()
    conn.close()

def get_scan_history():
    conn = sqlite3.connect('scan_history.db')
    c = conn.cursor()
    c.execute("SELECT host, ports, timestamp FROM scans ORDER BY timestamp DESC LIMIT 10")
    history = c.fetchall()
    conn.close()
    return history
