import sqlite3

class Logger:
    def __init__(self):
        self.conn = sqlite3.connect('threats.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS threats(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                severity TEXT,
                category TEXT,
                source TEXT,
                confidence REAL,
                timestamp REAL
            )
        ''')
        self.conn.commit()

    def log_threat(self, threat):
        self.cursor.execute('''
            INSERT INTO threats(
                name,
                severity,
                category,
                source,
                confidence,
                timestamp
                )
            VALUES(?,?,?,?,?,?)
            
            ''', (
            threat['name'],
            threat['severity'],
            threat['category'],
            threat['source'],
            threat['confidence'],
            threat['timestamp']
            ))
        self.conn.commit()
        