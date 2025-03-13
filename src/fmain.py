from flask import Flask, render_template, request, redirect, url_for
from schedule import schedule

schedule = schedule()['classes']
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_schedule', methods=['POST'])
def check_schedule():
    form_data = request.form.to_dict()
    classes = {form_data[f'class{i}']: [] for i in range(1, 9)}
    
    for classs, _ in classes.items():
        classes[classs] = list(set([classss[1] for classss in schedule if classss[0] == classs]))

    occupied_periods = set()
    conflicts = []
    print(classes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)