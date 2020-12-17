plaintext = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
encrytedtext = list('DEFGHIJKLMNOPQRSTUVWXYZABC')

def message(text , plain , encryp)
    dictionary = dict(zip(plain , encryp))
    for char in text:
        try:
            newmessage += dictionary[char]
        except:
            newmessage += ' '


