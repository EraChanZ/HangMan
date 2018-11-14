import random
words = []
wwords = open('words.txt','r')
new_words = [i.strip() for i in list(open('newwords.txt','r'))]
def make_word(w):
    k = 0
    final = ''
    for l in w:
        if l == '\t':
            final = w[:k]
            break
        k += 1
    return final
for w in wwords:
    words.append(make_word(w.split(' ')[3]).lower())
words = words + new_words
print(words)
variants = []
wwords.close()
def find_letter(var,free,used):
    answer = ''
    flag = False
    for v in var:
        for f in free:
            if v[f] not in used:
                answer = v[f]
                flag = True
                break
        if flag:
            break
    if answer == '':
        return 'I lost'
    else:
        return answer
def find_free_pos(word):
    pos = []
    k = 0
    for ww in word:
        if ww == '.':
            pos.append(k)
        k += 1
    return pos
def compare(f,s):
    k = 0
    answ = True
    for i in f:
        if i == '.':
            pass
        else:
            if i != s[k]:
                answ = False
        k += 1
    return answ
def del_var(word, variants,useless):
    final_arr = []
    for v in variants:
        if compare(word,v):
            flag = True
            for u in useless:
                if u in v:
                    flag = False
                    break
            if flag:
                final_arr.append(v)
    return final_arr
long = int(input('How long is your word? :'))
guess = ['.' for i in range(long)]
for wo in words:
    if len(wo) == len(guess):
        variants.append(wo)
used_letters = []
tryes = 0
response = ''
no_letters = []
while '.' in guess:
    variants = del_var(guess, variants,no_letters)
    print(variants)
    if len(variants) == 1:
        smth = input('Is this word "{}" ? (y/n) :'.format(variants[0]))
        if smth == 'y':
            response = 'I won, loooooser!'
            break
        else:
            response = 'I lost... I have no more words'
            break
    positions = find_free_pos(guess)
    letter = find_letter(variants,positions,used_letters)
    if letter == 'I lost':
        response = 'You won! I have no more words'
        break
    a = input('Is {} in your word? (y/n) :'.format(letter))
    if a == 'n':
        tryes += 1
        used_letters.append(letter)
        no_letters.append(letter)
        continue
    elif a == 'y':
        b = [int(i) for i in input('Write all positions of this letter :').split(' ')]
        for ps in b:
            guess[ps-1] = letter
        print(''.join(guess))
        used_letters.append(letter)
if response == '':
    print('I won, loooooser!')
    print('your word :'+''.join(guess))
    print('tryes :'+str(tryes))
elif response == 'I won, loooooser!':
    print('I won, loooooser!')
    print('your word :' + variants[0])
    print('tryes :' + str(tryes))
elif response == 'You won! I have no more words' or response == 'I lost... I have no more words':
    print(response)
    inp = input('Would you like to add your word to my dictionary ? (y/n)')
    if inp == 'y':
        file = open('newwords.txt','a')
        file.write(input('Write your word here :') + '\n')
        file.close()