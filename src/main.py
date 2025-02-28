from ortools.sat.python import cp_model
import os, json, ast

def main():
    model = cp_model.CpModel()
    periods = 8
    cps = json.load(open("./src/data/classesin.json", "r")) if os.path.isfile("./src/data/classesin.json") else json.load(open("./data/classesin.json", "r"))
    cps = {ast.literal_eval(k): v for k, v in cps.items()}
    teachers = list(set(teacher for _, teacher in cps))
    ppp = len(teachers) / periods
    schedule = {}

    for (cls, teacher) in cps:
        for p in range(periods):
            schedule[(cls, teacher, p)] = model.NewBoolVar(f'schedule_{cls}_{teacher}_{p}')

    for (cls, teacher) in cps:
        model.Add(sum(schedule[(cls, teacher, p)] for p in range(periods)) == cps[(cls, teacher)][1])

    for teacher in teachers:
        for p in range(periods):
            model.Add(sum(schedule[(cls, teacher, p)] for (cls, t) in cps if t == teacher) <= 1)

    prep = {}
    for teacher in teachers:
        for p in range(periods):
            prep[(teacher, p)] = model.NewBoolVar(f'prep_{teacher}_{p}')
            model.Add(prep[(teacher, p)] == 1 - sum(schedule[(cls, teacher, p)] for (cls, t) in cps if t == teacher))

    prep_count = [model.NewIntVar(0, len(teachers), f'prep_count_{p}') for p in range(periods)]
    for p in range(periods):
        model.Add(prep_count[p] == sum(prep[(teacher, p)] for teacher in teachers))

    deviation = [model.NewIntVar(0, len(teachers), f'deviation_{p}') for p in range(periods)]
    for p in range(periods):
        model.Add(deviation[p] >= prep_count[p] - int(ppp))
        model.Add(deviation[p] >= int(ppp) - prep_count[p])

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
                assigned_classes = [cls for (cls, t) in cps if t == teacher and solver.Value(schedule[(cls, teacher, p)]) == 1]
                if assigned_classes:
                    for cls in assigned_classes:
                        output.append(f'{cls} is scheduled in period {p+1} taught by {teacher.upper()}')
                        outputjson["classes"].append([cls, p+1, teacher.upper()])
                else:
                    output.append(f'prep is scheduled in period {p} for {teacher.upper()}')
                    outputjson["classes"].append(["Prep", p+1, teacher.upper()])

    td = sum(abs(solver.Value(prep_count[p]) - ppp) for p in range(periods))

    with open(out, 'w') as file:
        file.write(f"Solution suboptimality: {td}")
        for line in output:
            file.write(f"\n{line}")

    with open(outjson, 'w') as file:
        json.dump(outputjson, file, indent=4)

if __name__ == '__main__':
    main()
