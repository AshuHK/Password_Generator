import random
import string


def shuffle_string(rand_str):
    char_list = list(rand_str)
    random.shuffle(char_list)
    return "".join(char_list)


def generate_password(size=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    chars = shuffle_string(chars)

    new_password = ""
    while len(new_password) < size:
        new_password += chars[random.randint(0, len(chars) - 1)]

    new_password = shuffle_string(new_password)

    return new_password


def main():
    try:
        size = int(input("Enter the size of the password: "))
        new_password = generate_password(size)
    except ValueError:
        new_password = generate_password()

    print("Your new password is: {}".format(new_password))


if __name__ == "__main__":
    main()
