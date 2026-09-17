PLACEHOLDER = "[name]"

with open(
    "day-24-files-directories-paths/Input/Letters/starting_letter.txt", encoding="utf-8"
) as letter:
    letter_template = letter.read()

with open(
    "day-24-files-directories-paths/Input/Names/invited_names.txt", encoding="utf-8"
) as names_files:
    for name in names_files:
        stripped_name = name.strip()
        clean_letter = letter_template.replace(PLACEHOLDER, stripped_name)

        with open(
            f"day-24-files-directories-paths/Output/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w",
            encoding="utf-8",
        ) as completed_letter:
            completed_letter.write(clean_letter)
