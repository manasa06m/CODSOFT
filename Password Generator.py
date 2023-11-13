import random
import string

def gen_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return

        password = gen_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()