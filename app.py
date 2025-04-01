from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/programming')
def programming():
    return render_template('programming.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

if __name__ == '__main__':
    app.run(debug=True)