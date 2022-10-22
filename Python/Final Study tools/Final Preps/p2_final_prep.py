def file_find(direc, string):
    """Find recursively all files under directory direc with names that
    include substring string."""

    def filename_search(filename, string):
        """Search for string in file name."""
        if filename.find(string) >= 0:
            print("Found", filename)

    files = []
    subdirs = []
    for f in os.listdir(direc):
        name = os.path.join(direc, f)
        if os.path.isfile(name):
            files.append(name)
        if os.path.isdir(name):
            subdirs.append(name)
    for f in files:
        filename_search(f, string)
    for d in subdirs:
        file_find(d, string)  # <--- recursive call

# THis coould be done easier with the os.walk() function:
#    for dir_name, dirs, files in os.walk(direc):
#        print(dir_name, dirs, files)
# file_find(".", '.py')