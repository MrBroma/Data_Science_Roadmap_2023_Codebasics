# Master Yoda speaks a sentence in a different order. Let's say
# you want to convert a sentence to Yoda’s speech.
# Write a function named master_yoda which will take a string as input
# and return the output after reversing the words of the sentence.

def reverse(sentence):
    # creating a list of words
    words = sentence.split()

    # suppress ponctuation
    terminate = ""
    if words[-1][-1] == "." or words[-1][-1] == "?":
        terminate = words[-1][-1]
        last_word = words[-1]
        last_word_without = last_word.replace(terminate, '')
        words[-1] = last_word_without

    # reverse the order in the list
    words.reverse()

    # creating the new sentence
    yoda_sentence = " ".join(words) + terminate
    return yoda_sentence


new_sentence = reverse("I am learning Python.")

print(new_sentence)

