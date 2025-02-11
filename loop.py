import os


def save_grade(grade):
    with open('grades.txt', 'a') as file:
        file.write(f"{grade}\n")


def view_grades():
    if not os.path.exists('grades.txt'):
        print("No grades found.")
        return
    
    with open('grades.txt', 'r') as file:
        grades = file.readlines()
    
    if not grades:
        print("No grades found.")
    else:
        print("\n--- Grades ---")
        for idx, grade in enumerate(grades, 1):
            print(f"{idx}. {grade.strip()}")
        print("---------------")


def main():
    while True:
        print("\nMenu:")
        print("1. Input a grade")
        print("2. View stored grades")
        print("3. Exit")
        
        choice = input("Please choose an option (1/2/3): ").strip()
        
        if choice == '1':
            grade = input("Enter the grade: ").strip()
            save_grade(grade)
            print(f"Grade {grade} has been saved.")
        
        elif choice == '2':
            view_grades()
        
        elif choice == '3': 
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
