from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# After running this code without errors, you may navigate to http://localhost:8080 or http://127.0.0.1:8080, to see findex.html rendered.
