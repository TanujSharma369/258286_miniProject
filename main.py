"""
defining rules to encode the data
each character will be paired to some random character
"""


def encodingRule():
    # making pairs of each alphabet in a dictionary
    encoded_characters = {

        # Defining codes for Lowercase Alphabets
        'a': 'w', 'b': 'x', 'c': 'v', 'd': 'y',
        'e': 'z', 'f': 'u',
        'g': 't', 'h': 'r', 'i': 's', 'j': 'q',
        'k': 'm', 'l': 'p',
        'm': 'k', 'n': 'o', 'o': 'n', 'p': 'l',
        'q': 'j', 'r': 'h',
        's': 'i', 't': 'g', 'u': 'f', 'v': 'c',
        'w': 'a', 'x': 'b',
        'y': 'd', 'z': 'e',

        # Defining codes for Uppercase Alphabets
        'A': 'W', 'B': 'X', 'C': 'V', 'D': 'Y',
        'E': 'Z', 'F': 'U',
        'G': 'T', 'H': 'R', 'I': 'S', 'J': 'Q',
        'K': 'M', 'L': 'P',
        'M': 'K', 'N': 'O', 'O': 'N', 'P': 'L',
        'Q': 'J', 'R': 'H',
        'S': 'I', 'T': 'G', 'U': 'F', 'V': 'C',
        'W': 'A', 'X': 'B',
        'Y': 'D', 'Z': 'E',

        # Defining codes for digits
        '1': '5', '2': '4', '3': '3', '4': '2',
        '5': '1', '6': '7',
        '7': '6', '8': '9', '9': '8', '0': '0',

        # Defining codes for special characters
        '`': '/', '/': '`', '!': '~', '~': '!',
        '@': '#', '#': '@',
        '(': '[', ')': ']', '[': '(', ']': ')',
        '+': '-', '-': '+', '.': '^', '^': '.'
    }
    # returning encoding rules in a dictionary
    return encoded_characters


"""
encoding the data entered by the user 
encoded data will be returned in the form of string
"""


def encode(data_to_encode):
    # creating an object of encodingRule()

    encoding_rules = encodingRule()

    # declaring an empty string which will contain encoded data
    encoded_data = ""

    # encoding the data
    for character in range(0, len(data_to_encode)):
        if data_to_encode[character] in encoding_rules.keys():
            encoded_data += encoding_rules[data_to_encode[character]]
        else:
            encoded_data += data_to_encode[character]
    # returning the encoded data
    return encoded_data


if __name__ == "__main__":
    print("***************Welcome to encoder***************")
    print("You can encode \n1.your message\n2.URLs\n3.Email ID\n")
    data = input("Input your data to encode: ")
    encoded_result = encode(data)
    print("Encoded data: " + encoded_result)
    decoded_result = encode(encoded_result)
    print("Decoded data: " + decoded_result)



