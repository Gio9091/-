import json

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def __str__(self):
        return f"სახელი: {self.name}, სიის ნომერი: {self.roll_number}, შეფასება: {self.grade}"

    def to_dict(self):

        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):

        return Student(data["name"], data["roll_number"], data["grade"])

class StudentManagementSystem:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                students_data = json.load(file)
                if isinstance(students_data, list):
                    return [Student.from_dict(student) for student in students_data]
                else:
                    print("ფაილში არასწორი მონაცემები.")
                    return []
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"შეცდომა ფაილის ჩატვირთული: {e}")
            return []

    def save_students(self):

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add_student(self):
        name = input("შეიყვანეთ სტუდენტის სახელი: ")

        while True:
            try:
                roll_number = int(input("შეიყვანეთ სიის ნომერი: "))
                if roll_number <= 0:
                    print("სიის ნომერი უნდა იყოს დადებითი.")
                    continue
                break
            except ValueError:
                print("გთხოვთ, შეიყვანოთ ვალიდური ნომერი.")

        while True:
            grade = input("შეიყვანეთ შეფასება (A, B, C, D, F): ").upper()
            if grade in ['A', 'B', 'C', 'D', 'F']:
                break
            else:
                print("არასწორი შეფასება. გთხოვთ, შეიყვანოთ ვალიდური შეფასება.")

        student = Student(name, roll_number, grade)
        self.students.append(student)
        self.save_students()
        print("სტუდენტი წარმატებით დაემატა.")

    def view_all_students(self):
        if len(self.students) == 0:
            print("არ არსებობს სტუდენტები.")
        else:
            for student in self.students:
                print(student)

    def search_student_by_roll_number(self):
        try:
            roll_number = int(input("შეიყვანეთ სიის ნომერი, რომლის მიხედვითაც გსურთ მოძებნათ სტუდენტი: "))
            student = next((s for s in self.students if s.roll_number == roll_number), None)
            if student:
                print(student)
            else:
                print("სტუდენტი არ მოიძებნა.")
        except ValueError:
            print("გთხოვთ, შეიყვანოთ ვალიდური ნომერი.")

    def update_grade(self):
        try:
            roll_number = int(input("შეიყვანეთ სიის ნომერი სტუდენტის შეფასების განახლებისთვის: "))
            student = next((s for s in self.students if s.roll_number == roll_number), None)
            if student:
                while True:
                    new_grade = input("შეიყვანეთ ახალი შეფასება (A, B, C, D, F): ").upper()
                    if new_grade in ['A', 'B', 'C', 'D', 'F']:
                        student.grade = new_grade
                        self.save_students()
                        print("შეფასება წარმატებით განახლდა.")
                        break
                    else:
                        print("არასწორი შეფასება. გთხოვთ, შეიყვანოთ ვალიდური შეფასება.")
            else:
                print("სტუდენტი არ მოიძებნა.")
        except ValueError:
            print("გთხოვთ, შეიყვანოთ ვალიდური ნომერი.")

    def show_menu(self):
        while True:
            print("\nსტუდენტების მართვის სისტემა")
            print("1. ახალი სტუდენტის დამატება")
            print("2. ყველა სტუდენტის ნახვა")
            print("3. სტუდენტის მოძებნა სიის ნომრით")
            print("4. სტუდენტის შეფასების განახლება")
            print("5. გასვლა")
            choice = input("აირჩიეთ ოპცია: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student_by_roll_number()
            elif choice == '4':
                self.update_grade()
            elif choice == '5':
                print("პროგრამა დაიხურა.")
                break
            else:
                print("არასწორი ოპცია. გთხოვთ, სცადეთ ისევ.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.show_menu()
