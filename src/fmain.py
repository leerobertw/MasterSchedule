from flask import Flask, render_template, flash, redirect, url_for, request
from schedule import schedulegrab
from clist import L
import json
from collections import Counter

schedule = schedulegrab()['classes']
app = Flask(__name__)
app.secret_key = "LonePeakMasterSchedulee"
app.jinja_env.filters["fromjson"] = json.loads

@app.route('/')
def index():
    return render_template('index.html')

def get_valid(classes):
    all_combinations = L()
    for class_name, periods in classes.items():
        if class_name and periods:
            all_combinations.p(periods)
    all_combinations.c()
    valid_combinations = [comb for comb in all_combinations if len(set(comb)) == len(comb)]
    return valid_combinations, len(valid_combinations)>0

@app.route('/check_schedule', methods=['POST'])
def check_schedule():
    form_data = request.form.to_dict()
    classnames = [form_data[f'class{i}'] for i in range(1, 9)]
    classes = {form_data[f'class{i}']: [] for i in range(1, 9)}
    for classs, _ in classes.items():
        classes[classs] = list(set([classss[1] for classss in schedule if classss[0] == classs]))
    valid_combinations, valid = get_valid(classes)
    if not valid:
        period_conflicts = {}
        for class_name, periods in classes.items():
            for period in periods:
                if period in period_conflicts:
                    period_conflicts[period].append(class_name)
                else:
                    period_conflicts[period] = [class_name]
        conflicting_classes = {k: v for k, v in sorted(period_conflicts.items()) if len(v) > 1}
        removable_classes = []
        for class_name in list(classes.keys()):
            temp_classes = {k: v for k, v in classes.items() if k != class_name}
            _, temp_valid = get_valid(temp_classes)
            if temp_valid:
                removable_classes.append(class_name)
        msg = {
            "status": "You can't take those classes next year!",
            "conflicts": removable_classes
        }
        flash(json.dumps(msg))
    else:
        mapped_class_combinations = [dict(sorted({valid_combination[i]: classnames[i] for i in range(len(classnames))}.items())) for valid_combination in valid_combinations]
        msg = {"status": "You can take those classes next year!", "result": mapped_class_combinations}
        flash(json.dumps(msg))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)