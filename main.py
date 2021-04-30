# defining rules to encode and decode string
def encodingRule():
    # making pairs of each alphabet
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


def encode(data_to_encode):
    encoding_rules = encodingRule()
    encoded_data = ""

    for character in range(0, len(data_to_encode)):
        if data_to_encode[character] in encoding_rules.keys():
            encoded_data += encoding_rules[data_to_encode[character]]
        else:
            encoded_data += data_to_encode[character]

    return encoded_data


if __name__ == "__main__":
    data = input("Input your message to encode: ")
    print(encode(data))

