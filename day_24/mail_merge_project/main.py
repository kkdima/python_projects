# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def main():
    with open("day_24/mail_merge_project/Letters/starting_letter.txt") as file:
        starting_letter = file.read()
    with open("day_24/mail_merge_project/Names/invited_names.txt") as file:
        names = file.readlines()
    for name in names:
        name = name.strip()
        letter = starting_letter.replace("[name]", name)
        with open(f"day_24/mail_merge_project/Letters/letter_for_{name}.docx", "w") as file:
            file.write(letter)


main()
