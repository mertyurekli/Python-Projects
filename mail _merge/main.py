with open("Input/Names/invited_names.txt", "r") as file:
    invited_list = file.readlines()

with open("Input/Letters/starting_letter.txt", "r") as file:
    letter_contents = file.read()

for name in invited_list:
    stripped_name = name.strip()
    new_letter = letter_contents.replace("[name]", f"{stripped_name}")
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as file:
        file.write(new_letter)
