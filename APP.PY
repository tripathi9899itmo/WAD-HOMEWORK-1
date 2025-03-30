from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def PROFILE():
    return render_template('PROFILE.html')

if __name__ == '__main__':
    app.run(debug=True)