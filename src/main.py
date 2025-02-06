from ortools.sat.python import cp_model
import os

def main():
    model = cp_model.CpModel()
    classes = ['science', 'math', 'english', 'astronomy']
    teachers = ['x', 'y', 'z']
    periods = 3
    cps = {
        'science': ('x', 2),
        'math': ('y', 2),
        'english': ('z', 1),
        'astronomy': ('z', 1)
    }
    schedule = {}
    ppp = len(teachers)/periods
    for cls in classes:
        for p in range(periods):
            schedule[(cls, p)] = model.NewBoolVar(f'schedule_{cls}_{p}')

    for cls in cps:
        model.Add(sum(schedule[(cls, p)] for p in range(periods)) == cps[cls][1])
    for teacher in teachers:
        for p in range(periods):
            tcip = [
                schedule[(cls, p)] for cls in cps if cps[cls][0] == teacher
            ]
            model.Add(sum(tcip) <= 1)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    out = "out.txt"
    output = []
    unformatted = []

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for teacher in teachers:
            for p in range(periods):
                assigned_classes = [cls for cls in cps if cps[cls][0] == teacher and solver.Value(schedule[(cls, p)]) == 1]
                if assigned_classes:
                    for cls in assigned_classes:
                        output.append(f'{cls} is scheduled in period {p} taught by {teacher.upper()}')
                        unformatted.append((cls, p, teacher.upper()))
                else:
                    output.append(f'prep is scheduled in period {p} for {teacher.upper()}')
                    unformatted.append(('prep', p, teacher.upper()))
    
    ppps = {}
    for i in range(periods):
        ppps[i] = 0
    for unformat in unformatted:
        if unformat[0] == "prep":
            ppps[unformat[1]] += 1
    td = 0
    for i in ppps:
        td += abs(ppps[i]-ppp)

    if not os.path.exists(out):
        with open(out, 'w') as file:
            file.write(f"Solution suboptimality: {td}\n")
            file.write("\n".join(output))
    else:
        with open(out, 'a') as file:
            file.write(f"Solution suboptimality: {td}\n")
            file.write("\n".join(output))

    for line in output:
        print(line)
    print(f"Solution suboptimality: {td}")

if __name__ == '__main__':
    main()
