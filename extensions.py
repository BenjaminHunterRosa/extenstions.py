image = input("image link: ")
if ".jpeg" in image.strip():
   print("image/jpeg")
elif ".jpg" in image.strip():
   print("image/jpg")
elif ".png" in image.strip():
   print("image/png")
elif ".gif" in image.strip():
   print("image/gif")
elif ".pdf" in image.strip():
   print("application/pdf")
elif ".txt" in image.strip():
   print("application/txt")
elif ".zip" in image.strip():
   print("application/zip")
else:
   print("application/octet-stream")
