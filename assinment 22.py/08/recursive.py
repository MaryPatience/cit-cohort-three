#sample_words = "green-red-yellow-black-white" 

def wat(s: str):
    words = s.split("-")
    words.sort()
    new_item = "-".join(words)

    return new_item

print(wat(sample_words))
