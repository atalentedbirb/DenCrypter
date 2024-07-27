import os, daVinci
def file(fname, key, filename, directory):
    if directory == '':
        directory= 'SavedfilesDecrypt'
    print('DECRYPTING PROCESS AS BEGUN...')
    try:
        filename= filename+'.txt'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath= os.path.join(directory, filename)
        with open(fname, 'r') as f:
            sentence= f.readlines()
            for i in sentence:
                daVinci.generate_key(i, key) ##!!!!!
                decrypted= daVinci.decrypt_vigenere(i, key)
                with open(filepath, 'a') as g:
                    g.write(decrypted)
        print(f'Decryption successful, file located at: {filepath}')       
    except IOError:
        print("File could not be parsed")
