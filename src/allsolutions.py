from ortools.sat.python import cp_model
import os

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, schedule, deviation):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.schedule = schedule
        self.deviation = deviation
        self.solutions = []
        self.optimal_deviation = None

    def on_solution_callback(self):
        current_deviation = self.Value(self.deviation)
        if self.optimal_deviation is None or current_deviation < self.optimal_deviation:
            self.optimal_deviation = current_deviation
            self.solutions = [self.collect_solution()]
        elif current_deviation == self.optimal_deviation:
            self.solutions.append(self.collect_solution())

    def collect_solution(self):
        solution = {}
        for key in self.schedule:
            solution[key] = self.Value(self.schedule[key])
        return solution

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
    ppp = len(teachers) / periods
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

    prep_counts = [model.NewIntVar(0, len(teachers), f'prep_count_{p}') for p in range(periods)]

    for p in range(periods):
        model.Add(prep_counts[p] == sum(1 - schedule[(cls, p)] for cls in classes))

    deviation = model.NewIntVar(0, len(teachers) * periods, 'deviation')
    model.Add(deviation == sum(abs(prep_counts[p] - ppp) for p in range(periods)))
    model.Minimize(deviation)

    solver = cp_model.CpSolver()
    solution_collector = SolutionCollector(schedule, deviation)
    status = solver.SearchForAllSolutions(model, solution_collector)

    out = "out.txt"
    if not os.path.exists(out):
        with open(out, 'w') as file:
            file.write(f"Optimal solutions with deviation: {solution_collector.optimal_deviation}\n")
    else:
        with open(out, 'a') as file:
            file.write(f"Optimal solutions with deviation: {solution_collector.optimal_deviation}\n")

    for solution in solution_collector.solutions:
        output = []
        for teacher in teachers:
            for p in range(periods):
                assigned_classes = [cls for cls in cps if cps[cls][0] == teacher and solution[(cls, p)] == 1]
                if assigned_classes:
                    for cls in assigned_classes:
                        output.append(f'{cls} is scheduled in period {p} taught by {teacher.upper()}')
                else:
                    output.append(f'prep is scheduled in period {p} for {teacher.upper()}')
        with open(out, 'a') as file:
            file.write("\n".join(output) + "\n\n")

    print(f"Optimal solutions with deviation: {solution_collector.optimal_deviation}")
    for solution in solution_collector.solutions:
        for teacher in teachers:
            for p in range(periods):
                assigned_classes = [cls for cls in cps if cps[cls][0] == teacher and solution[(cls, p)] == 1]
                if assigned_classes:
                    for cls in assigned_classes:
                        print(f'{cls} is scheduled in period {p} taught by {teacher.upper()}')
                else:
                    print(f'prep is scheduled in period {p} for {teacher.upper()}')
        print()

if __name__ == '__main__':
    main()