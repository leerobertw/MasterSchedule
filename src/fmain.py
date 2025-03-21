from flask import Flask, render_template, flash, redirect, url_for, request
from schedule import schedule
from clist import L
import json

schedule = schedule()['classes']
app = Flask(__name__)
app.secret_key = "LonePeakMasterSchedulee"
app.jinja_env.filters["fromjson"] = json.loads

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_schedule', methods=['POST'])
def check_schedule():
    form_data = request.form.to_dict()
    classnames = [form_data[f'class{i}'] for i in range(1, 9)]
    classes = {form_data[f'class{i}']: [] for i in range(1, 9)}
    for classs, _ in classes.items():
        classes[classs] = list(set([classss[1] for classss in schedule if classss[0] == classs]))
    all_combinations = L()
    for class_name, periods in classes.items():
        if class_name and periods:
            all_combinations.p(periods)
    all_combinations.c()
    valid_combinations = [comb for comb in all_combinations if len(set(comb)) == len(comb)]
    mapped_class_combinations = [dict(sorted({valid_combination[i]:classnames[i] for i in range(len(classnames))}.items())) for valid_combination in valid_combinations]
    if len(valid_combinations) <= 0:
        msg = "You can't take those classes next year!"
        flash(json.dumps({"status":msg}))
    else:
        msg = "You can take those classes next year!"
        flash(json.dumps({"status":msg,"result":mapped_class_combinations}))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)