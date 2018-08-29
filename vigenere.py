# Connor Hanlon hanlo047@umn.edu

# I understand this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work none it was
# obtained from any source other than material presented as part of the
# course.


def main():
    """
    Encrypts or decrypts an input file using an encryption keyword, and writes
    the new message to a given output file.
    """
    import sys
    filexistance(sys.argv[2])
    if len(sys.argv[4]) < 3:
        raise SystemExit("Encryption Key requires three or more characters")
    abet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
    messagein = readmessagein(sys.argv[2])
    keyword = sys.argv[4]
    vigtable = constructvigenere(keyword, abet)
    if sys.argv[1] == '-e':
        outmessage, typemess = encryptmess(abet, vigtable, messagein), "encoded: "
    if sys.argv[1] == '-d':
        outmessage, typemess =  decryptmess(abet, vigtable, messagein), "decoded: "
    messageout(sys.argv[3], outmessage)
    print()
    print(typemess + outmessage)
    print()
    for emt in vigtable:
        print(emt)

def filexistance(somefile):
    """
    Determines whether the input file exists, and if file does not exist the
    system exit exception is thrown with the appropriate message.
    """
    try:
        xfiles3 = open(somefile, 'r')
        xfiles3.close()
    except:
        raise SystemExit('Input file does not exist')


def messageout(sysargument2, outmessage):
    """
    Writes the encoded or decrypted message to the output file.
    """
    xfiles2 = open(sysargument2, 'w')
    xfiles2.write(outmessage)
    xfiles2.close()

def readmessagein(sysargument):
    """
    Opens the input file and returns the contents of the input file.
    """
    xfiles = open(sysargument, 'r')
    mess = xfiles.read()
    xfiles.close()
    return mess

def constructvigenere(keyword, abet):
    """
    Constructs a sparse version of the Vigenere table using a list of shifted
    alphabets using the encryption keyword.
    """
    vigeneretable = []
    for letter in keyword:
        x = 0
        for symbol in abet:
            if letter == symbol:
                vigeneretable.append(abet[x:] + abet[:x])
            x += 1
    return vigeneretable

def encryptmess(abet, vigtable, messagein):
    """
    Ecrypts the contents of the input message read by the messagein function using
    the constructed Vigenere table.
    """
    encodedmessage = ''
    location = []
    for inputletters in messagein:
        x = 0
        for letters in abet:
            if letters == inputletters:
                location.append(x)
            x += 1
    y, z = 0, 0
    while y < len(location):
        locator = location[y]
        if z >= len(vigtable):
            z = 0
        encodedmessage = encodedmessage + vigtable[z][locator]
        y += 1
        z += 1
    return encodedmessage

def decryptmess(abet, vigtable, messagein):
    """
    Decrypts the contents of the input message read by the messagein function using
    the constructed Vigenere table.
    """
    decryptedmessage = ''
    location = []
    element = 0
    for letter in messagein:
        x = 0
        if element >= len(vigtable):
            element = 0
        for place in vigtable[element]:
            if letter == vigtable[element][x]:
                location.append(x)
            x += 1
        element += 1
    for number in location:
        decryptedmessage = decryptedmessage + abet[number]
    return decryptedmessage


main()
