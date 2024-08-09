from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# MySQL bağlantı ayarları
db_config = {
    'user': os.getenv('DATABASE_USER'),
    'password': os.getenv('DATABASE_PASSWORD'),
    'host': os.getenv('DATABASE_HOST'),
    'database': os.getenv('DATABASE_NAME')
}

@app.route('/')
def home():
    try:
        # MySQL veritabanına bağlanma
        mysql_connection = mysql.connector.connect(**db_config)
        cursor = mysql_connection.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()[0]

        return f"Ulaş'ın E-ticaret Sitesine Hoş Geldiniz! Bağlanılan Veritabanı: {db_name}."
    except mysql.connector.Error as err:
        return f"Bağlantı hatası: {err}"
    finally:
        if 'mysql_connection' in locals() and mysql_connection.is_connected():
            cursor.close()
            mysql_connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
