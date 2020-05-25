import random
import string


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


def generate_password(size=16):
    """
    Generates a new password with a given size

    :param size: Integer for the size of the new password
    :return: String to represent the new password
    """

    # generate a basic pool of characters and shuffle it
    chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
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


if __name__ == "__main__":
    main()
