'''Objective : To identify and fix errors in a Python program that manipulates strings.'''

'''There's a small mistake in the for loop range. It should be range(len(s)-1, -1, -1) instead of range(len(s) - 1, 0, -1) to include the first character in the reversed string. 
Here's the corrected code:'''

def reverse_string(s):

    reversed = ""
    for i in range(len(s) - 1, 0, -1):
        reversed += s[i]
    return reversed

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()

