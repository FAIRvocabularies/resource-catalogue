import os

def main():
    directory = os.path.join("_data", "resources")
    for filename in os.listdir(directory):
        if filename.endswith(".yml"):
            #print(os.path.join(directory, filename))
            resourceFile = open(os.path.join(directory, filename), "r")
            if resourceFile.mode == 'r':
                 contents = resourceFile.read()
                 #print contents
                 if not os.path.exists("_resources/"):
                    os.makedirs("_resources/")
                 collectionFile = open("_resources/"+os.path.splitext(filename)[0]+".md", "w")
                 collectionFile.write("---\n")
                 collectionFile.write(contents+"\n")
                 collectionFile.write("layout: resource\n")
                 collectionFile.write("---\n")
                 collectionFile.close()
                 resourceFile
            continue
        else:
            continue

if __name__== "__main__":
  main()
