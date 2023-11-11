'''Objective: To identify and fix errors in a Python program that validates user input.'''

''' 
'age' is initially assigned as a string. When you use input(), the user's input is always a string. Therefore, we need to convert age to an integer before comparing it with 18.
The comparison age >= 18 would cause a TypeError because age is a string, not an integer. To fix this, we should convert age to an integer before performing the comparison.
'''
def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18: #Fixed comparison and conversion
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
