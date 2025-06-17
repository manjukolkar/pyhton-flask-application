from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS submissions (name TEXT, email TEXT, message TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('INSERT INTO submissions (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
        conn.close()
        return redirect('/records')
    return render_template('form.html')

@app.route('/records')
def records():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM submissions')
    data = c.fetchall()
    conn.close()
    return render_template('records.html', submissions=data)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000)
