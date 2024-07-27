import os, daVinci
def file(fname, key, filename, directory):
    if directory =='':
        directory= 'SavedfilesEncrypt'
    print('ENCRYPTION HAS BEGUN...')
    try:
        filename= filename+'.txt'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath= os.path.join(directory, filename)
        with open(fname, 'r') as f:
            sentence= f.readlines()
            for i in sentence:
                daVinci.generate_key(i, key) ##!!!!!
                encrypted= daVinci.encrypt_vigenere(i, key)
                with open(filepath, 'a') as g:
                    g.write(encrypted)
        print(f'Encryption sucessful, file located at: {filepath}')       
    except IOError:
        print("File could not be parsed")

        