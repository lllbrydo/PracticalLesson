class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)
        print(f"cтудента {student_name} додано в список")

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"студента {student_name} видаленл")
        else:
            print(f"студента {student_name} не знайдено")

    def show_students(self):
        if self.students:
            print("список студентів")
            for student in self.students:
                print(student)
        else:
            print("студентів немає.")

    def info(self):
        return (
                f"вчитель {self.name}"
                f" предмет: {self.subject}"
                f" стаж роботи {self.experience} "
                )


teacher = Teacher("Олена",
                  "Математика",
                  10
                  )

teacher.add_student("назар")
teacher.show_students()
teacher.remove_student("назар")
teacher.show_students()
print(teacher.info())
