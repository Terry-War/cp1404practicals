"""CP1404 Practical 5 - Word Occurrences
Estimate: ~ 20 mins
Started at 18:30
finished at 17:00
"""
# text = "this is a collection of words of nice words this is a fun thing it is"  # used for testing

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1
words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
