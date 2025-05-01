from flask import Flask, render_template, flash, redirect, url_for, request
from schedule import schedulegrab
from clist import L
import json

schedule = schedulegrab()["classes"]
app = Flask(__name__)
app.secret_key = "LonePeakMasterSchedulee"
app.jinja_env.filters["fromjson"] = json.loads


@app.route("/")
def index():
    return render_template("index.html")


def get_valid(classes):
    all_combinations = L()
    for class_name, periods in classes.items():
        if class_name and periods:
            all_combinations.p(periods)
    all_combinations.c()
    valid_combinations = [
        comb for comb in all_combinations if len(set(comb)) == len(comb)
    ]
    return valid_combinations, len(valid_combinations) > 0


@app.route("/check_schedule", methods=["POST"])
def check_schedule():
    try:
        form_data = request.form.to_dict()
        classnames = [form_data[f"class{i}"] for i in range(1, 9)]
        class_mapping = {
            form_data[f"class{i}"].lower(): form_data[f"class{i}"] for i in range(1, 9)
        }
        classes = {class_name: [] for class_name in class_mapping}
        for classs in classes:
            for classss in schedule:
                if classss[0].lower() == classs:
                    classes[classs] = list(set(classes[classs] + [classss[1]]))
                    class_mapping[classs] = classss[0]
        valid_combinations, valid = get_valid(classes)
        if not valid:
            period_conflicts = {}
            for class_name, periods in classes.items():
                for period in periods:
                    if period in period_conflicts:
                        period_conflicts[period].append(class_name)
                    else:
                        period_conflicts[period] = [class_name]
            conflicting_classes = []
            for class_name in list(classes.keys()):
                temp_classes = {k: v for k, v in classes.items() if k != class_name}
                _, temp_valid = get_valid(temp_classes)
                if temp_valid:
                    conflicting_classes.append(
                        {
                            "class_name": class_mapping[class_name],
                            "available_periods": ",".join(map(str, classes[class_name])),
                        }
                    )
            msg = {
                "status": "You can't take those classes next year!",
                "conflicts": conflicting_classes,
            }
            flash(json.dumps(msg))
        else:
            mapped_class_combinations = []
            for valid_combination in valid_combinations:
                sorted_schedule = dict(
                    sorted(
                        {
                            valid_combination[i]: class_mapping[classnames[i].lower()]
                            for i in range(len(classnames))
                        }.items()
                    )
                )
                mapped_class_combinations.append(sorted_schedule)
            # currently the teacher mapping sets the teacher to the last teacher found but it is supposed to be a list of all teachers
            mapped_with_teachers = mapped_class_combinations.copy()
            for mapp in mapped_with_teachers:
                for period, class_name in mapp.items():
                    teachers = []
                    for class_info in schedule:
                        if class_info[0].lower() == class_name.lower() and int(period) == class_info[1]:
                            teachers.append(class_info[2] if class_info[2] else "No Teacher Found")
                    mapp[period] = {
                        "class_name": class_name,
                        "teachers": teachers if teachers else ["No Teacher Found"],
                    }
            msg = {
                "status": "You can take those classes next year!",
                "result": mapped_with_teachers,
            }
            flash(json.dumps(msg))
        return redirect(url_for("index"))
    except Exception as e:
        return render_template("error.html", error=e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
