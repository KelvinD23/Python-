SIZE_ALPHABET = 26
def decode_caesar(encoded_message, key):
    """
    Using the value contained in key, decrypts all alphabetic characters in encoded_message, including all non-alpha
    characters in decoded-message left not decrypted.

    :param encoded_message: String encrypted by the Caesar cipher.
    :param key: Integer used for decryption.
    :return: Decrypted string.
    """

    # WRITE YOUR CODE HERE!

    mod_str = " "

    for char in encoded_message:
        if char.isalpha():
            current_ord = ord(char) - key

            if not (char.isupper() and ord("A") <= current_ord <= ord("Z") or (char.islower() and ord("a") <= current_ord <= ord("z"))):
                current_ord += SIZE_ALPHABET

            char = chr(current_ord)
        mod_str += char
    return mod_str


def main():
    """
    Just some sample behavior.
    """
    decryption_key = 3

    try:
        file = open("calling_america_lyrics.txt", 'r')
    except FileNotFoundError:
        print("ERROR: File not found!")
    else:
        for line in file:
            line = line.strip()
            decryption = decode_caesar(line, decryption_key)
            print(decryption)

        file.close()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
