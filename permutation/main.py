
#function prints out every permutation of a string in alphabetical order
def permutation(str, prefix=""):
    str = sorted(str)
    
    if not len(str):
        #prints each permutation, followed by a comma, on a single line
        print(prefix + ", ", end='')
        
    else:
        for i in range(len(str)):
            permutation(str[:i] + str[i+1:], prefix + str[i])

#reads a file and creates a list of each line in the file
def read_file(file_name):
    r = open(file_name, "r")
    lines = []
    line = r.readline()
    while line:
        values = line.split()
        lines.append(values[0])
        line = r.readline()
    r.close()
    return lines

def main():
    a_list_of_words = read_file("words.txt")
    for word in a_list_of_words:
        permutation(word)
        print("\n")

if __name__ == "__main__":
    main()
         