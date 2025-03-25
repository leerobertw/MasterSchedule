from ortools.sat.python import cp_model
import os, json, ast

def schedule():
    model = cp_model.CpModel()
    periods = 8
    cps_raw = json.load(open("./src/data/classesin.json", "r")) if os.path.isfile("./src/data/classesin.json") else json.load(open("./data/classesin.json", "r"))
    cps_raw = {ast.literal_eval(k): v for k, v in cps_raw.items()}
    teachings = {}
    teacher_unavail = {}
    for key, val in cps_raw.items():
        cls, teacher = key
        if cls == "RESERVED":
            teacher_unavail[teacher] = [p - 1 for p in val[2]]
        else:
            teachings[key] = val
    teachers = list(set(teacher for _, teacher in teachings))
    schedule = {}
    for teacher in set(t for _, t in teachings):
        required_teaching = sum(teachings[(cls, t)][1] for (cls, t) in teachings if t == teacher)
        reserved_periods = len(teacher_unavail.get(teacher, []))
        available_periods = periods - reserved_periods
        if required_teaching > available_periods:
            print(f"Infeasible: {teacher} needs {required_teaching} periods to teach, but only has {available_periods} free periods.")
    for (cls, teacher) in teachings:
        for p in range(periods):
            if teacher in teacher_unavail and p in teacher_unavail[teacher]:
                continue
            schedule[(cls, teacher, p)] = model.NewBoolVar(f'schedule_{cls}_{teacher}_{p}')
    for (cls, teacher) in teachings:
        available_periods = [p for p in range(periods) if teacher not in teacher_unavail or p not in teacher_unavail[teacher]]
        model.Add(sum(schedule[(cls, teacher, p)] for p in available_periods) == teachings[(cls, teacher)][1])
    for teacher in teachers:
        for p in range(periods):
            if teacher in teacher_unavail and p in teacher_unavail[teacher]:
                continue
            relevant = [schedule[(cls, teacher, p)] for (cls, t) in teachings if t == teacher and (cls, teacher, p) in schedule]
            model.Add(sum(relevant) <= 1)
    prep = {}
    for teacher in teachers:
        for p in range(periods):
            if teacher in teacher_unavail and p in teacher_unavail[teacher]:
                prep[(teacher, p)] = model.NewIntVar(0, 0, f'prep_{teacher}_{p}')
            else:
                relevant = [schedule[(cls, teacher, p)] for (cls, t) in teachings if t == teacher and (cls, teacher, p) in schedule]
                prep[(teacher, p)] = model.NewBoolVar(f'prep_{teacher}_{p}')
                model.Add(prep[(teacher, p)] == 1 - sum(relevant))
    prep_count = [model.NewIntVar(0, len(teachers), f'prep_count_{p}') for p in range(periods)]
    for p in range(periods):
        available = [prep[(teacher, p)] for teacher in teachers if teacher not in teacher_unavail or p not in teacher_unavail[teacher]]
        model.Add(prep_count[p] == sum(available))
    available_teachers = {}
    for p in range(periods):
        available_teachers[p] = sum(1 for teacher in teachers if teacher not in teacher_unavail or p not in teacher_unavail[teacher])
    total_available = sum(available_teachers[p] for p in range(periods))
    total_teaching = sum(teachings[(cls, teacher)][1] for (cls, teacher) in teachings)
    total_prep_needed = total_available - total_teaching
    deviation = [model.NewIntVar(0, total_available, f'deviation_{p}') for p in range(periods)]
    for p in range(periods):
        target = int(round(available_teachers[p] * total_prep_needed / total_available))
        model.Add(deviation[p] >= prep_count[p] - target)
        model.Add(deviation[p] >= target - prep_count[p])
    model.Minimize(sum(deviation))
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    out = "./data/out.txt" if os.path.isfile("./data/out.txt") else "./src/data/out.txt"
    outjson = "./data/classesout.json" if os.path.isfile("./data/classesout.json") else "./src/data/classesout.json"
    output = []
    outputjson = {"classes":[]}
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for teacher in teachers:
            for p in range(periods):
                if teacher in teacher_unavail and p in teacher_unavail[teacher]:
                    output.append(f'{teacher.upper()} is not available in period {p+1}')
                    outputjson["classes"].append(["Not available", p+1, teacher.upper()])
                    continue
                assigned_classes = [cls for (cls, t) in teachings if t == teacher and (cls, teacher, p) in schedule and solver.Value(schedule[(cls, teacher, p)]) == 1]
                if assigned_classes:
                    for cls in assigned_classes:
                        output.append(f'{cls} is scheduled in period {p+1} taught by {teacher.upper()}')
                        outputjson["classes"].append([cls, p+1, teacher.upper()])
                else:
                    output.append(f'prep is scheduled in period {p+1} for {teacher.upper()}')
                    outputjson["classes"].append(["Prep", p+1, teacher.upper()])
    td = sum(abs(solver.Value(prep_count[p]) - int(round(available_teachers[p] * total_prep_needed / total_available))) for p in range(periods))
    with open(out, 'w') as file:
        file.write(f"Solution suboptimality: {td}")
        for line in output:
            file.write(f"\n{line}")
    with open(outjson, 'w') as file:
        json.dump(outputjson, file, indent=4)
    
    return outputjson

def schedulegrab():
    return json.load(open("./data/classesout.json", "r") if os.path.isfile("./data/classesout.json") else open("./src/data/classesout.json", "r"))