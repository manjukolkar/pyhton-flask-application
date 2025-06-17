from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
data_store = []  # Temporary in-memory storage

@app.route('/')
def index():
    return render_template('index.html', data=data_store)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']
    data_store.append({'name': name, 'message': message})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
