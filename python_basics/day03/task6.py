# Given a list of words
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length

def create_word_length_dictionary(words):
    word_length_dict = {word: len(word) for word in words}
    return word_length_dict

# Example usage
words = ["apple", "banana", "kiwi", "cherry", "mango"]
word_length_dict = create_word_length_dictionary(words)
print(word_length_dict)