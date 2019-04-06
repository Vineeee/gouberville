import os
import os.path
import ctypes

def import_gouberville_paragraphe(f_in, f_out):
    
    #f= open(f_out,"w+")
    fread = open(f_in, 'r')
    mytext = fread.read()
    fread.close()

    mytext.replace(". Le jeudi", ".\nLe jeudi")
    mytext.replace(". Le vendredi", ".\nLe vendredi")

    fwrite = open(f_out, 'w')
    fwrite.write(mytext)
    fwrite.close()
 
if __name__ == '__main__':
    texte_gouberville = "/home/dev/workspaceConda/gouberville/data/gouberville.txt"
    texte_gouberville2 = "/home/dev/workspaceConda/gouberville/data/gouberville2.txt"
    import_gouberville_paragraphe(texte_gouberville, texte_gouberville2)
    