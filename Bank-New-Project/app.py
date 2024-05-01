from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database connection function
def db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='l3n0v0ph0n3$$$$',  
            database='newschema'
        )
        return conn
    except mysql.connector.Error as error:
        print("Failed to connect to the database:", error)
        return None
    
def index():
    return render_template('index.html')

@app.route('/accounts', methods=['GET', 'POST'])
def manage_accounts():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("INSERT INTO accounts (customer_name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    return render_template('accounts.html', accounts=accounts)

@app.route('/transactions', methods=['GET', 'POST'])
def manage_transactions():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        account_id = request.form['account_id']
        transaction_type = request.form['type']
        amount = request.form['amount']
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, %s, %s)",
                       (account_id, transaction_type, amount))
        conn.commit()
    return render_template('transactions.html')

if __name__ == '__main__':
    app.run(debug=True)
