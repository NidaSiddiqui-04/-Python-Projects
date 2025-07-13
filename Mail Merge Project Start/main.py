#TODO: Create a letter using st
# with open("/Users/nidas/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/ for_letter.txt ",mode="w") as new:
#     new.write("something")
with open("C:/Users/nidas/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letters=letter.read()


with open("C:/Users/nidas/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name=names.readlines()


for each_name in name:
    stripped_name=each_name.strip()
    personalized_letter=letters.replace("[name]",stripped_name)
    with open (f"C:/Users/nidas/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for {stripped_name}.docs",mode="w") as output:
        output.write(personalized_letter)

# print(stripped_name)
# #Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        # Define fi
