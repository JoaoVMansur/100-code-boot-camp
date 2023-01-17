PLACEHOLDER = "[name]"


with open("day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    nomes = names.readlines()

with open("day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()
    for name in nomes:
        striped_name =  name.strip()
        new_letter = letter.replace(PLACEHOLDER, striped_name)
        with open(f"day 24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{striped_name}.txt",mode="w" ) as final_letter:

            final_letter.write(new_letter)

