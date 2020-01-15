sentence = input('Enter a sentence: ')

split_sentence = sentence.split()

i = 0
while i < len(split_sentence):
    if i == 0:
        split_sentence[i] = split_sentence[i].lower()
        i += 1
    else:
        split_sentence[i] = split_sentence[i].capitalize()
        i += 1

s = ''

s = s.join(split_sentence)

print(s)