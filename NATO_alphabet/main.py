import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

word = input("Enter the Word: ")
output_list = [phonetic_dict[letter.upper()] for letter in word]
print(output_list)

