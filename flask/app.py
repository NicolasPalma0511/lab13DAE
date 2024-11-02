from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Conexión a SQL Server
def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=ec2-34-234-75-73.compute-1.amazonaws.com;"
        "DATABASE=movielens;"
        "UID=SA;"
        "PWD=YourStrong@Passw0rd;"
    )
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Consulta de la base de datos
    cursor.execute("SELECT * FROM ratings")  # Limitar a 1000 registros
    rows = cursor.fetchall()
    conn.close()
    
    # Convertir los datos a formato JSON
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
