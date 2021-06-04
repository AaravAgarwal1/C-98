def countWords():
    fileName=input("Enter the file name: ")
    file= open(fileName,"r")
    numofWords=0
    for line in file:
        words=line.split()
        numofWords+=len(words)
        
    print(f"Number of words in this paragraph: {numofWords}")

countWords()