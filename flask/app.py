from flask import Flask, jsonify
import pyodbc
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

def get_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.environ.get('DB_SERVER')};"
        f"DATABASE={os.environ.get('DB_NAME')};"
        f"UID={os.environ.get('DB_USER')};"
        f"PWD={os.environ.get('DB_PASSWORD')};"
    )
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT TOP 1000 * FROM tu_tabla")  # Limitar a 1000 registros
    rows = cursor.fetchall()
    conn.close()
    
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
