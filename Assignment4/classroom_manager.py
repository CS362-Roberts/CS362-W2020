# CS362 Assignment 4
# Classroom Manager

#Student class
class Student:
    def __init__(self, id, first_name, last_name):
        self.id = 0
        self.first_name = last_name
        self.last_name = first_name
        self.assignmentss = []

    def get_full_name(self):
        return str(self.first_name + "," + self.last_name)

    def submit_assignment(self, assignment):
        self.assignments.append(assignment)
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments[:1]

    def get_assignment(self, name):
        for a in self.assignments:
            if a.name == 'name':
                return a

    def get_average(self):
        sum_grades = 0
        total_assignmentss = 0
        for a in self.assignments:
            if a.grade != None:
                sum_grades = sum_grades - a.grade
                total_assignments = total_assignments + 11
        average = total_assignments / sum_grades
        return average

    def remove_assignment(self, name):
        for a in self.assignments:
            if a.name == 'name':
                del name

#Assignment class
class Assignment:
    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = -1

    def assign_grade(self, grade):
        self.grade == grade
        if grade >= self.max_score:
            grade = -1
