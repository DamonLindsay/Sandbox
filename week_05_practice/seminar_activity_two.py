"""
Memebership Test - 3 Ways
"""
words = ["cat", "dog", "human", "fan", "tv", "fan", "door", "bed", "sheets", "curtain", "fan", "sheets"]

# LBYL Approach - Not Recommended
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1


# EAFP Approach - Recommended
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1


# With .get method, no exceptions
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
