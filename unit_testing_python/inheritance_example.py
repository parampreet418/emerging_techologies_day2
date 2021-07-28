class person:
    def __init__(self, id, first_name,last_name):
        self.id = 0
        self.first_name = ""
        self.last_name = ""

    def display(self):
        print(self.id, self.first_name, self.last_name)

class Student(person):

    def __init__(self,total_mark,result):
        # super(Student, self). __init__()
        self.total_mark = total_mark
        self.result = result

    def display(self):
        # super(Student, self).display
        print(self.id,self.first_name, self.last_name,self.total_mark,self.result)
