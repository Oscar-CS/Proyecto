import hashFile
import argparse

def main():
    # Creamos el objeto ArgumentParser
    parser = argparse.ArgumentParser() 

    # Creamos los flags para los argumentos
    parser.add_argument("-path", dest="path", help="")
    parser.add_argument("-hsh", dest="hashAlg")

    params = parser.parse_args()
    filePath = params.path
    hashAlgorithm = params.hashAlg
    
    hashFile.hash(filePath, hashAlgorithm)
           
if __name__ == '__main__':
    main = main()
    