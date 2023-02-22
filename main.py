import pandas as pd

data = pd.read_csv('Morse Code Alphabet.csv', header=None)
data.columns = ['letter', 'morse']
letters = data['letter'].str.lower().tolist()
morse = data['morse'].tolist()

# create dictionary
morse_dict = {}

for letter in letters:
    position = letters.index(letter)
    translation = morse[position]
    morse_dict[letter] = translation


def encrypt(user_input):
    characters = list(user_input)
    coded_text = []
    for character in characters:
        morse_character = morse_dict[character]
        coded_text.append(morse_character)
    coded_text_str = ' '.join(coded_text)
    print(coded_text_str)


repeat = True

while repeat:
    text = input('Text to convert to Morse Code: ').lower()

    try:
        encrypt(text)
    except KeyError:
        print('Invalid characters, please review and try again.')
