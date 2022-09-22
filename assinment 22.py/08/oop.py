class Man:
    def __init__(self, height, finance, color, tribe, name):
        self.height=height
        self.finance=finance
        self.color=color
        self.tribe = tribe
        self.name = name
Paul = Man("tall", "rich", "brown", "muganda", "Paul")
John = Man("tall", "poor", "brown", "mukiga", "John")
Chris = Man("short", "rich", "dark", "mufumbira", "Chris")
Mark = Man("tall", "rich", "dark", "acholi", "Mark")
men=[Paul, John, Chris, Mark]

#print(Paul.height)

for i in range(len(men)):
    print(f" {men[i].name} is a {men[i].height} {men[i].finance} {men[i].color} {men[i].tribe} man.")
    #print(men[i].height)