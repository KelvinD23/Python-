def binary_to_decimal(binary_list):
    """
    Converts a binary number, represented by the values inside binary_list, to its decimal equivalent.

    :param binary_list: A list of ones and zeroes.
    :return: An integer.
    """

    # WRITE YOUR CODE HERE!
    binary_list.reverse()
    num = 0
    for i in range(0, len(binary_list)):

        if binary_list[i] == 1:
            num += 2 ** i

    return num





def main():
    """
    Just some sample behavior. Feel free to try your own!
    """

    binary = [1, 0, 0, 1, 1, 1]
    print(binary_to_decimal(binary))

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
