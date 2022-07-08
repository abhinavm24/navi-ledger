from sys import argv
from ledger.interface import Interface

def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    # Interface().cmdloop()
    PATH = argv[1] #retrieving path of text file

    #reading the text file
    FILE = open(PATH, "r")
    INPUT_LINES = FILE.readlines()

    for line in INPUT_LINES:
        Interface().onecmd(line) #calling function to route input as required
    
if __name__ == "__main__":
    main()