from flask import Flask, render_template, request, redirect, url_for
from schedule import schedule
from clist import L

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
    all_combinations = L()
    for class_name, periods in classes.items():
        if class_name and periods:
            all_combinations.p(periods)
    for combination in all_combinations:
        combination = L(combination)
        combination.c()
    for combination in all_combinations:
        combination[0].append(combination.pop(1))
        combination = combination[0]
    valid_combinations = all_combinations
    for combination in all_combinations:
        for x in combination:
            if combination.count(x) > 1:
                valid_combinations.remove(combination)
    mapped_combinations = []
    for combination in valid_combinations:
        mapped_classes = []
        for period in combination:
            for class_name, periods in classes.items():
                if period in periods:
                    mapped_classes.append(class_name)
                    break
        mapped_combinations.append((combination, mapped_classes))
    print("Valid Combinations with Classes:")
    for combo, class_names in mapped_combinations:
        print(f"Combination: {combo} -> Classes: {class_names}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)