# Student Management System (Terminal-based)
# Author: Nitin Gupta

students = []

def show_menu():
    print("\n===== STUDENT MANAGEMENT MENU =====")
    print("1. View all students")
    print("2. Add student")
    print("3. Search student by enrollment no")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

def view_students():
    if not students:
        print("\nNo students found.")
        return
    print("\nList of Students:")
    print("{:<5} {:<20} {:<15} {:<10}".format('No', 'Name', 'Enrollment', 'Year'))
    for i, s in enumerate(students, start=1):
        print("{:<5} {:<20} {:<15} {:<10}".format(i, s['name'], s['enroll'], s['year']))

def add_student():
    name = input('Enter student name: ').strip()
    enroll = input('Enter enrollment number: ').strip()
    year = input('Enter year/semester: ').strip()
    students.append({'name': name, 'enroll': enroll, 'year': year})
    print('✅ Student added successfully!')

def find_by_enroll(enroll):
    for idx, s in enumerate(students):
        if s['enroll'] == enroll:
            return idx, s
    return None, None

def search_student():
    enroll = input('Enter enrollment number to search: ').strip()
    idx, s = find_by_enroll(enroll)
    if s:
        print('\nStudent found:')
        print('Name:', s['name'])
        print('Enrollment:', s['enroll'])
        print('Year:', s['year'])
    else:
        print('⚠️ No student with that enrollment number.')

def update_student():
    enroll = input('Enter enrollment number to update: ').strip()
    idx, s = find_by_enroll(enroll)
    if s:
        print('Current data:', s)
        name = input('Enter new name (leave blank to keep): ').strip()
        year = input('Enter new year (leave blank to keep): ').strip()
        if name:
            students[idx]['name'] = name
        if year:
            students[idx]['year'] = year
        print('✅ Student updated successfully!')
    else:
        print('⚠️ No student with that enrollment number.')

def delete_student():
    enroll = input('Enter enrollment number to delete: ').strip()
    idx, s = find_by_enroll(enroll)
    if s:
        confirm = input(f"Are you sure you want to delete {s['name']}? (y/n): ").lower()
        if confirm == 'y':
            students.pop(idx)
            print('🗑️ Student deleted successfully!')
        else:
            print('Deletion cancelled.')
    else:
        print('⚠️ No student with that enrollment number.')

def main():
    while True:
        show_menu()
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            view_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print('👋 Exiting Student Management System.')
            break
        else:
            print('⚠️ Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
