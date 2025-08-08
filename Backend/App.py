from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # if using templates, or return open('frontend/index.html').read()

@app.route('/test-db')
def test_db():
    try:
        connection = pymysql.connect(
            host='your-db-endpoint',
            user='admin',
            password='your-password',
            database='your-database'
        )
        return "Connected to RDS!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
