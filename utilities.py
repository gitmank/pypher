def to_caesar(plaintext, shift):
    ans = ""
    # iterate over the string
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # if character is space, add space
        if ch==" ":
            ans+=" "
        # rotate character 'shift' times
        elif (ch.isupper()):
            ans += chr((ord(ch) + shift-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + shift-97) % 26 + 97)
    
    return ans

def from_caesar(ciphertext, shift):
    ans = ""
    # iterate over the string
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        # if character is space, add space
        if ch==" ":
            ans+=" "
        # rotate character negative 'shift' times
        elif (ch.isupper()):
            ans += chr((ord(ch) - shift-65) % 26 + 65)
        else:
            ans += chr((ord(ch) - shift-97) % 26 + 97)
    
    return ans
    
def to_vigenere(plaintext, key):
    ans = ""
    # iterate over the string
    for i in range(len(plaintext)):
        ch = plaintext[i]
        # if character is space, add space
        if ch==" ":
            ans+=" "
        # encode by adding key[i] to plaintext[i]
        # example: B + L = M, T + M = F
        elif (ch.isupper()):
            ans += chr((ord(ch) + ord(key[i%len(key)])-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + ord(key[i%len(key)])-97) % 26 + 97)
    
    return ans

def from_vigenere(ciphertext, key):
    ans = ""
    # iterate over the string
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        # if character is space, add space
        if ch==" ":
            ans+=" "
        # decode by subtracting key[i] from ciphertext[i]
        # example: M - L = B, F - M = T
        elif (ch.isupper()):
            ans += chr((ord(ch) - ord(key[i%len(key)])-65) % 26 + 65)
        else:
            ans += chr((ord(ch) - ord(key[i%len(key)])-97) % 26 + 97)
    
    return ans

def generatePlayfairMatrix(key):
    # remove spaces and make uppercase
    key = "".join(key.upper().split(' '))
    # remove duplicate letters from key
    key = "".join(dict.fromkeys(key))
    key = [*key]
    # add remaining letters to key
    for i in range(65, 91):
        if chr(i) not in key:
            key.append(chr(i))
    # remove J from key
    key = "".join(key)
    key = key.replace("J", "")

    # generate 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append([*key[i:i+5]])

    return matrix

def generatePlayfairPairs(text):
    # remove spaces and make uppercase
    text = "".join(text.upper().split(' '))
    # remove J from text
    text = text.replace("J", "I")
    digrams = []
    for i in range(0, len(text)+1, 2):
        if(i+1 > len(text)):
            break
        if (i+1 == len(text)):
            text += "X"
        elif (text[i] == text[i+1]):
            text = text[:i+1] + "X" + text[i+1:]
        digrams.append(text[i:i+2])

    return digrams

def encodePlayfairPair(pair, matrix):
    # get coordinates of each letter in pair
    x1, y1 = getCoordinatesOfMatrixElement(pair[0], matrix)
    x2, y2 = getCoordinatesOfMatrixElement(pair[1], matrix)

    # if letters are in same row, shift right
    if (x1 == x2):
        return matrix[x1][(y1+1)%5] + matrix[x2][(y2+1)%5]
    # if letters are in same column, shift down
    elif (y1 == y2):
        return matrix[(x1+1)%5][y1] + matrix[(x2+1)%5][y2]
    # if letters are in different rows and columns, swap columns
    else:
        return matrix[x1][y2] + matrix[x2][y1]

def decodePlayfairPair(pair, matrix):
    # get coordinates of each letter in pair
    x1, y1 = getCoordinatesOfMatrixElement(pair[0], matrix)
    x2, y2 = getCoordinatesOfMatrixElement(pair[1], matrix)

    # if letters are in same row, shift left
    if (x1 == x2):
        return matrix[x1][(y1-1)%5] + matrix[x2][(y2-1)%5]
    # if letters are in same column, shift up
    elif (y1 == y2):
        return matrix[(x1-1)%5][y1] + matrix[(x2-1)%5][y2]
    # if letters are in different rows and columns, swap columns
    else:
        return matrix[x1][y2] + matrix[x2][y1]

def getCoordinatesOfMatrixElement(letter, matrix):
    for i in range(5):
        for j in range(5):
            if (matrix[i][j] == letter):
                return (i, j)

def to_playfair(plaintext, key):
    matrix = generatePlayfairMatrix(key)
    pairs = generatePlayfairPairs(plaintext)
    for i in range(len(pairs)):
        pairs[i] = encodePlayfairPair(pairs[i], matrix)
    return("".join(pairs))

def from_playfair(ciphertext, key):
    matrix = generatePlayfairMatrix(key)
    pairs = generatePlayfairPairs(ciphertext)
    for i in range(len(pairs)):
        pairs[i] = decodePlayfairPair(pairs[i], matrix)
    return("".join(pairs))
