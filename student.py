class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, gpa: {self.gpa}'

def main():
    alice = Student('Alice', 'aa1234aa', '4.0')
    bob = Student('Bob', 'bb1234bb', '1.3')

    print(alice.name)
    print(bob.college_id)
    print(bob.gpa)

    print(alice)
    print(bob)

main()