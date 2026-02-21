age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert ages to set and compare length
age_set = set(age)
print(f"List length: {len(age)}, Set length: {len(age_set)}")
# The list is bigger because the set removed duplicate ages!

# 2. Differences:
# - String: Ordered text, immutable.
# - List: Ordered collection, mutable, allows duplicates.
# - Tuple: Ordered collection, immutable, allows duplicates.
# - Set: Unordered collection, mutable, NO duplicates, unique items only.

# 3. Unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split() # Splits into a list of words
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")