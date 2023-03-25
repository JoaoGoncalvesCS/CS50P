#Getting input from user
filename = input("File name: ").lower().strip()

#Checking for image extensions
if ".gif" in filename:
    print("image/gif")

elif ".jpg" in filename:
    print("image/jpeg")

elif ".jpeg" in filename:
    print("image/jpeg")

elif ".png" in filename:
    print("image/png")

#Checking for pdf file extensions

elif ".pdf" in filename:
    print("application/pdf")

#Checking for txt file extensions

elif ".txt" in filename:
    print("text/plain")

#Checking for zip file extensions

elif ".zip" in filename:
    print("application/zip")

#Checking for no file extensions

else:
    print("application/octet-stream")