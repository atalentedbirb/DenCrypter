import filekryptosencrypt
import daVinci
import filekryptosdecrypt
print('SUPER_DUPER_ENCRYPTER'.center(100,'='))
directory= input('Choose your working directory: ')

while True:
    c1= input('Enter what you wanna do: \n[FILE encrypt (F)/WORD encrypt(W)]\n[FILE decrypt (FD)/WORD decrypt(WD)]\nHelp and Info(H)\nEnter your choice: ')
    if c1.lower()=='f':
        print('FILE_ENCODER'.center(100, "="))
        filename= input('Enter file location: ')
        key= input('Enter a key:')
        newfile= input('Output File Name: ')
        filekryptosencrypt.file(filename,key, newfile, directory)
    elif c1.lower()=='w':
        print('WORD_ENCODER'.center(100, '='))
        text= input('Enter text to encode: ').strip()
        key= input('Enter a key:')
        daVinci.generate_key(text, key)
        mytext= daVinci.encrypt_vigenere(text, key)
        print(f'The encrypted word is: {mytext}')
    elif c1.lower()=='fd':
        print('FILE_DECODER'.center(100, '='))
        text= input('Enter file location: ')
        key= input('Enter the key:')
        newfile= input('Output File Name:')
        filekryptosdecrypt.file(text,key, newfile, directory)
    elif c1.lower()=='wd':
        print('WORD_DECODER'.center(100, '='))
        text= input('Enter text to decode: ').strip()
        key= input('Enter a key:')
        daVinci.generate_key(text, key)
        yourtext= daVinci.decrypt_vigenere(text, key)
        print(f'The decrypted word is: {yourtext}')
    elif c1.lower()=='h':
        print("HELP/INFO BOOTH".center(100,'='))
        print('You can drag and drop files directly into your terminal. File cannot be parsed could be not having a directory to save to.')
        print('File contents are case sensitive. A whitespace can ruin the process.')
        print('Most of this is self explanatory. KEYS are whitespace and case sensitive.')
        print('For bugs and features you can tag me in Twitter, @unrelatedbentok :3')
        print('Version --1.0.2')
        print('Made in Atlanta, GA. Inspired by Lemmino.')
        print("---".center(100, '-'))
    else:
        print('Wrong/Missing Characters, try again')
        continue
    endloop= input('Want to Exit?(Y/N)')
    if endloop.upper() == 'Y':
        break
    elif endloop.upper()== 'N':
        continue
    else:
        print('Wrong Character, try again')