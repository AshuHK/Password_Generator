import random
import string

# for getting the password onto the clipboard
import pyperclip


def shuffle_string(some_str):
    """
    Shuffles the given string and return it

    :param some_str: String of characters to be shuffled in a random order
    :return: String of the same characters in a random order
    """

    # turn the string into a list of strings
    char_list = list(some_str)

    # shuffle the list using random
    random.shuffle(char_list)

    # combine the list and return the string
    return "".join(char_list)


def update_file(password):
    """
    Updates (or creates) passwords.txt with the newest password

    :param password: String for the new password
    """
    file_obj = open("passwords.txt", "a")
    file_obj.write("{}\n".format(password))
    file_obj.close()


def get_data(password):
    """
    Gets data on the newst password and returns it into a tuple of integers

    :param password: String for the new password

    :return: Tuple of integers for the number of uppercase, lowercase, numbers, and punctuation characters in the password
    """
    lower = upper = digits = special = 0

    for i in range(len(password)):

        # if the character is lowercase
        if password[i].islower():
            lower += 1

        # if the character is uppercase
        elif password[i].isupper():
            upper += 1

        # if the character is a number
        elif password[i].isdigit():
            digits += 1

        # if the character is punctuation
        else:
            special += 1

    return (lower, upper, digits, special)


def generate_password(size=16):
    """
    Generates a new password with a given size

    :param size: Integer for the size of the new password
    :return: String to represent the new password
    """

    # generate a basic pool of characters and shuffle it
    chars = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.punctuation
        + string.digits
    )

    chars = shuffle_string(chars)

    # build the new password
    new_password = ""
    while len(new_password) < size:
        new_password += chars[random.randint(0, len(chars) - 1)]

    # shuffs the new password
    new_password = shuffle_string(new_password)

    return new_password


def main():
    try:
        size = int(input("\nEnter the size of the password: "))
        new_password = generate_password(size)
    except ValueError:
        new_password = generate_password()

    print("Your new password is: {}\n".format(new_password))

    lower, upper, digits, special = get_data(new_password)

    print("--------- Password Data ---------")
    print("Number of lowercase characters: {}".format(lower))
    print("Number of uppercase characters: {}".format(upper))
    print("Number of decimal numbers     : {}".format(digits))
    print("Number of special characters  : {}\n".format(special))

    pyperclip.copy(new_password)

    update_file(new_password)

    print("Updated passwords.txt")
    print("Copied onto your clipboard :)\n")


if __name__ == "__main__":
    main()
