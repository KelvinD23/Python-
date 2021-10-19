from copy import deepcopy, copy
from random import random


def corrupter(some_object):
    """
    Using award-winning, record-breaking algorithms jointly developed by Google, Amazon, Apple, and Sebastian, returns
    either a deep or shallow copy of some_object.

    This is just a sample corrupter function you can use to test your code! In theory, we can use any algorithm to
    return either a deep or shallow copy.

    :param some_object: Any Python object.
    :return: A deep or shallow copy of some_object.
    """
    if round(random()):
        return deepcopy(some_object)

    return copy(some_object)


def is_impostor(information, corrupter_function):
    """
    Returns true if function corrupter creates a deep copy of information.
    Students can also check this by modifying information's "Members" key-value pair, since changing its values would
    reflect in a shallow copy, but not a deep copy.

    This problem is actually pretty simple, but the students have to really know what deep/shallow copying entails in
    order to do it.

    :param information: A dictionary of a band's information.
    :param corrupter_function: A function that returns either a deep or shallow copy of the object passed onto it.
    :return: True or False
    """

    # WRITE YOUR CODE HERE!
    corr_res = corrupter_function(information)

    new_alb_name = "Some new album"
    information["Albums"].append(new_alb_name)

    if new_alb_name in corr_res["Albums"]:
        return False
    return True



def main():
    """
    Just some sample behavior. Feel free to try your own!
    """

    the_1975 = {
        "Band Name": "The 1975",
        "Members": {
            "Guitarist": "Adam Hann",
            "Bass Player": "Ross MacDonald",
            "Drummer": "George Daniel",
            "Singer": "Matty Healy"
        },
        "Albums": ["The 1975", "I like it when you sleep for you are so beautiful yet so unaware of it",
                   "A Brief Inquiry Into Online Relationships", "Notes on a Conditional Form"]
    }

    if is_impostor(the_1975, corrupter):
        print("is_impostor returned a deep copy!")
    else:
        print("is_impostor returned a shallow copy!")

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
