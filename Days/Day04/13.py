def reverseSentence(sentence):
    words = sentence.split(' ')
    r_sentence = ''
    for word in words:
        r = word[::-1] # ''.join(list(reversed(word)))
        r_sentence = r_sentence + ' ' + r
    return(r_sentence.strip())

sentence = input()
print(reverseSentence(sentence))