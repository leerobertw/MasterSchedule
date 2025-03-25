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
        period_conflicts = {}
        valid_periods = {class_name: set() for class_name in classes}
        for valid_combination in all_combinations:
            for i, class_name in enumerate(classnames):
                valid_periods[class_name].add(valid_combination[i])
        conflicts = {period: [class_name for class_name, periods in valid_periods.items() if period in periods] for period in [item for item, count in Counter([item for value in valid_periods.values() for item in value]).items() if count > 1]}
        print(conflicts)
        """
        for class_name, periods in classes.items():
            conflicting_periods = [p for p in periods if p not in valid_periods[class_name]]
            print(f"Class {class_name} has conflicting periods:", conflicting_periods)
            for period in conflicting_periods:
                if period in period_conflicts:
                    period_conflicts[period].append(class_name)
                else:
                    period_conflicts[period] = [class_name]
        print("Final period conflicts:", period_conflicts)
        conflicting_classes = {p: c for p, c in period_conflicts.items() if len(c) > 1}
        print("Filtered conflicting classes (only periods with multiple conflicts):", conflicting_classes)
        msg = {"status": "You can't take those classes next year!", "conflicts": conflicting_classes}
        flash(json.dumps(msg))"
        """
    else:
        msg = "You can take those classes next year!"
        flash(json.dumps({"status":msg,"result":mapped_class_combinations}))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)