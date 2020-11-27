import os
for filename in os.listdir(os.path.dirname(__file__)):
    if filename.isupper() == False:
        os.rename(filename, filename.upper())


exit()
