# Kendra Ludwig (kel334@nau.edu)


alphabet = "ABCDEFGHIJKLMNOPRSTVWXYZ_"
print("Welcome to the Playfair Cipher Machine!")
print("Would you like to:")
print("\t(e)ncrypt")
print("\tor")
print("\t(d)ecrypt")
selection = input()
key = input("\nPlease enter your key: ")
key = key.upper()


# make grid
# start with key chars
grid = ["", "", "", "", ""]
processedChars = ""
for char in key:
    if (char not in processedChars):
        if (len(grid[0]) <= 4):
            grid[0] += char
        elif (len(grid[1]) <= 4):
            grid[1] += char
        elif (len(grid[2]) <= 4):
            grid[2] += char
        elif (len(grid[3]) <= 4):
            grid[3] += char
        else:
            grid[4] += char

    processedChars += char

# continue with alphabet
for char in alphabet:
    if (char not in processedChars):
        if (len(grid[0]) <= 4):
            grid[0] += char
        elif (len(grid[1]) <= 4):
            grid[1] += char
        elif (len(grid[2]) <= 4):
            grid[2] += char
        elif (len(grid[3]) <= 4):
            grid[3] += char
        else:
            grid[4] += char

if (userChoice == 1):  # encrypt message
    msgToEncrypt = input("Please enter a message to encrypt: ")
    msgToEncrypt = msgToEncrypt.upper()

    # group letters into digrams
    digramList = []
    tempDigram = ""
    counter = 0
    for char in msgToEncrypt:
        # change SPACE TO '_'
        if (char == ' '):
            char = '_'

        # add letter to tempDigram
        tempDigram += char

        if (counter % 2 == 1):
            # counter is odd, add tempDigram
            # to fullMsg and clear tempDigram
            digramList.append(tempDigram)
            tempDigram = ""

        counter += 1

    # remove duplicates in digrams
    for digram in digramList:
        processedChars = ""
        digramIndex = digramList.index(digram)
        for char in digram:
            charIndex = digram.find(char)
            if (char in processedChars):
                # if letter is a duplicate
                newDigram = digram[:charIndex] + "X" + digram[(charIndex + 1):]
                digramList[digramIndex] = newDigram

            processedChars += char

    # locate row of first and second parts of each digram
    newDigramList = []
    for digram in digramList:
        char1Row = -1
        char1Col = -1
        char2Row = -1
        char2Col = -1
        rowNum = -1
        for char in digram:
            for row in grid:
                rowNum += 1
                for item in row:
                    if (item == char):
                        if (char1Row == -1):
                            char1Row = rowNum
                            char1Col = grid[rowNum].find(char)
                        else:
                            char2Row = rowNum
                            char2Col = grid[rowNum].find(char)
            rowNum = -1

        # modify char-rows without changing original values
        newChar1Row = char1Row
        newChar1Col = char1Col
        newChar2Row = char2Row
        newChar2Col = char2Col

        if (char1Row == char2Row):  # if both chars have same row
            # move 1 column over
            newChar1Col += 1
            newChar2Col += 1

            # go back to start of column if overflow
            if (newChar1Col > 4):
                newChar1Col = 0
            if (newChar2Col > 4):
                newChar2Col = 0

        elif (char1Col == char2Col):  # if both chars have the same column
            # move 1 row down
            newChar1Row += 1
            newChar2Row += 1

            # go to top of grid if overflow
            if (newChar1Row > 4):
                newChar1Row = 0
            if (newChar2Row > 4):
                newChar2Row = 0
        else:
            # cut across diagonal
            newChar1Row = char2Row
            newChar1Col = char2Col
            newChar2Row = char1Row
            newChar2Col = char1Col

            # find char in specific location on grid
            newChar1 = grid[newChar1Row][newChar1Col]
            newChar2 = grid[newChar2Row][newChar2Col]
            newDigramList.append(newChar1 + newChar2)

        # print final encrypted message
        output = ""
        for digram in newDigramList:
            output += (digram + " ")
        print("\nHere is your encrypted message: \n" + output)

else:  # decrypt message
    msgToDecrypt = input("\nPlease enter a message to decrypt: ")
    msgToDecrypt = msgToDecrypt.upper()

    # spit string into digrams
    digramList = msgToDecrypt.split(' ')

    # find locations and replace with decrypted digrams
    newDigramList = []
    for digram in digramList:
        char1Row = -1
        char1Col = -1
        char2Row = -1
        char2Col = -1
        rowNum = -1
        for char in digram:
            for row in grid:
                rowNum += 1
                for item in row:
                    if (item == char):
                        if (char1Row == -1):
                            char1Row = rowNum
                            char1Col = grid[rowNum].find(char)
                        else:
                            char2Row = rowNum
                            char2Col = grid[rowNum].find(char)
            rowNum = -1

        # modify char-rows without changing original values
        newChar1Row = char1Row
        newChar1Col = char1Col
        newChar2Row = char2Row
        newChar2Col = char2Col

        if (char1Row == char2Row):  # if both chars have same row
            # move 1 column over
            newChar1Col -= 1
            newChar2Col -= 1

            # go back to start of column if overflow
            if (newChar1Col < 0):
                newChar1Col = 4
            if (newChar2Col < 0):
                newChar2Col = 4

        elif (char1Col == char2Col):  # if both chars have same column
            # move 1 row down
            newChar1Row -= 1
            newChar2Row -= 1

            # go to top of grid if overflow
            if (newChar1Row < 0):
                newChar1Row = 4
            if (newChar2Row < 0):
                newChar2Row = 4

        else:
            # cut across diagonal
            newChar1Row = char2Row
            newChar1Col = char2Col
            newChar2Row = char1Row
            newChar2Col = char1Col

        # find char in specific location on grid
        newChar1 = grid[newChar1Row][newChar1Col]
        newChar2 = grid[newChar2Row][newChar2Col]
        newDigramList.append(newChar1 + newChar2)

    # display new decrypted message
    output = ""
    for digram in newDigramList:
        output += digram
    output = output.replace("_", " ")

    print("\nHere in your decrypted message:\n" + output)
