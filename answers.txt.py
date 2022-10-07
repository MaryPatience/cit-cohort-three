print("\tQuestions \n1. How old is Uganda? \n2. Who is the president of Uganda? \n3. Who is the president of America?")
with open('answers.txt', 'w') as f:
    f.write("\tSolutions \n1. 60 years old. \n2. Yoweri Kaguta Museveni \n3. Joe Biden")
with open("answers.txt") as f:
    contents = f.read()
    print(contents)