# importing packages
import sys

from pytube import YouTube
import os

# url input from user
yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
# extract only audio
video = yt.streams.filter(only_audio=True).first()

instructions = "Enter 1 to download to external drive \n" \
               "Enter 2 to download to C: drive\n" \
               "Enter 3 to download to both\n" \
               "Enter 4 to input path"
print(instructions)
user_input = input()
while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4':
    user_input = input(f"INPUT ERROR!\n{instructions}")
isDownloadBoth = False
if user_input == '1':
    destination = r'D:\Music'
elif user_input == '2':
    destination = r'C:\Users\javal\Music'
elif user_input == '3':
    destination = r'D:\Music'
    destination2 = r'C:\Users\javal\Music'
    isDownloadBoth = True
elif user_input == '4':
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
else:
    print("FATAL ERROR. BAD DATA. EXITING SCRIPT")
    sys.exit()

# download the file
out_file = video.download(output_path=destination)
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
if isDownloadBoth:
    out_file = video.download(output_path=destination2)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
