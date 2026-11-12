"""estimate of doing this question : 1 hour
"""
word_to_count = {}
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    try:
        word_to_count[word] +=1
    except KeyError:
        word_to_count[word] = 1

print(word_to_count)

max_length = max(len(word) for word in words)

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")