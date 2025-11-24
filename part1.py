import datetime
class person:
    def __init__(self, name, surname, birthyear,gender):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear
        self.gender =gender

    def calculate_age(self):
        return 2025 - self.birthyear
    
class student(person):
    def __init__(self, name, surname, birthyear, gender,school, id, field_of_study,  academic_year, parent_name, parent_number, start_year, size):
        super().__init__(name, surname, birthyear,gender)
        self.school = school
        self.id = id
        self.field_of_study = field_of_study
        self.academic_year = academic_year      
        self.parent_name = parent_name
        self.parent_number = parent_number
        self.start_year = start_year
        self.size = size
        
    def enter_information(self):
        while True:
            name = input("enter your name: ").strip()
            if name:
                self.name = name
                break
            print("Name cannot be empty. Please try again.")

        while True:
            surname = input("enter your surname: ").strip()
            if surname:
                self.surname = surname
                break
            print("Surname cannot be empty. Please try again.")

        while True:
            val = input("birthyear(YYYY): ").strip()
            try:
                self.birthyear = int(val)
            except ValueError:
                print("Invalid year format. Use YYYY.")
                continue
            if self.valide_birthyear():
                break

        while True:
            school = input("enter your school name: ").strip()
            if school:
                self.school = school
                break
            print("School name cannot be empty. Please try again.")

        while True:
            self.id = input("enter your ID number: ").strip()
            if self.valide_id_number():
                break

        while True:
            fos = input("enter your field of study: ").strip()
            if fos:
                self.field_of_study = fos
                break
            print("Field of study cannot be empty. Please try again.")

        while True:
            g = input("your gender (male or female): ").strip().lower()
            self.gender = g
            if self.valide_gender():
                break

        while True:
            val = input("enter your academic year(YYYY): ").strip()
            try:
                self.academic_year = int(val)
            except ValueError:
                print("Invalid year format. Use YYYY.")
                continue
            if self.valide_academic_year():
                break

        while True:
            pn = input("enter one parent name: ").strip()
            if pn:
                self.parent_name = pn
                break
            print("Parent name cannot be empty. Please try again.")

        while True:
            self.parent_number = input("enter parent phone number: ").strip()
            if self.validate_parent_number():
                break

        while True:
            val = input("enter your start year(YYYY): ").strip()
            try:
                self.start_year = int(val)
            except ValueError:
                print("Invalid year format. Use YYYY.")
                continue
            if self.valide_start_year():
                break

        while True:
            val = input("enter your size (meters, e.g. 1.75): ").strip()
            try:
                self.size = float(val)
            except ValueError:
                print("Invalid size. Use a number like 1.75.")
                continue
            if self.valide_size():
                break

        print("thank you for your information!")

    def calculate_finish_year(self):
        return self.start_year + 3

    def display_information(self):
        print("--------------------------------------------------")
        print(f"***{self.school} Student Card***")
        print("--------------------------------------------------")
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname} ")
        print(f"Age: {self.calculate_age()} years ")
        print(f"size: {self.size} m")
        print(f"Field of Study: {self.field_of_study} ")
        print(f"ID Number: {self.id}")
        print(f"Gender: {self.gender} ")
        print(f"Academic Year: {self.academic_year} ")
        print(f"Parent Name: {self.parent_name} ")
        print(f"Parent Phone Number: {self.parent_number} ")
        print(f"Delivrement Year: {self.academic_year} ")
        print(f"Expiration Year: {self.academic_year + 1} ")
        print(f"Start Year: {self.start_year} ")
        print(f"Finiss Year: {self.calculate_finish_year()} ")
        print("--------------------------------------------------")

    def validate_parent_number(self):
        if len(str(self.parent_number)) == 8:
            return True
        else:
            print("enter a valid parent phone number please")
            return False
        
    def valide_birthyear(self):
        if self.birthyear <= 2007:
            return True
        else:
            print("you must be at least 16 years old to be a student")
            return False
        
    def valide_id_number(self):
        if len(str(self.id)) >= 5:
            return True
        else:
            print("invalid id number")
            return False
        
    def valide_start_year(self):
        if self.start_year <= self.academic_year:
            return True
        else:
            print("enter a valid start year")
            return False
        
    def valide_gender(self):
        if self.gender in ["male", "female"]:
            return True
        else:
            print("gender must be either 'male' or 'female'")
            return False
        
    def valide_size(self):
        if 0.5 <= self.size <= 2.5:
            return True
        else:
            print("you are entering an invalid size")
            return False
        
    def valide_academic_year(self):
        current_year = datetime.datetime.now().year
        if self.academic_year == current_year:
            return True
        else:
            print(f"enter a valid academic year (should be {current_year})")
            return False
        
    def convert_name_to_uppercase(self):
        self.name = self.name.upper()
        print(f"Name: {self.name}")
        return self.name
    
    def convert_first_letter_surname_to_uppercase(self):
        if self.surname:
            self.surname = self.surname[0].upper() + self.surname[1:]
            print(f"Surname: {self.surname}")
        return self.surname
    
    def convert_first_letter_parent_name_to_uppercase(self):
        if self.parent_name:
            self.parent_name = self.parent_name[0].upper() + self.parent_name[1:]
            print(f"Parent Name: {self.parent_name}")
        return self.parent_name
    
    def convert_school_name_to_uppercase(self):
        self.school = self.school.upper()
        print(f"School Name: {self.school}")
        return self.school 
        
    def validate_all(self):
        return True
    
def main():
    print("---------------------------------------")
    print("welcome to our aplication")
    print("please enter your information below")
    print("---------------------------------------")

    args = ["", "", 0, "", "", "", "", 0, "", 0, 0, 0.0]
    student1 = student(*args)

    student1.enter_information()
    student1.convert_name_to_uppercase()
    student1.convert_first_letter_surname_to_uppercase()
    student1.convert_first_letter_parent_name_to_uppercase()
    student1.convert_school_name_to_uppercase()
    student1.display_information()

if __name__ == "__main__":
    main()




