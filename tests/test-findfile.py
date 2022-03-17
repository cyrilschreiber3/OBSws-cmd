import os
from datetime import datetime, timedelta
today = datetime.now()
today_formatted = today.strftime("%Y-%m-%d %H-%M-%S")
tomorrow = today + timedelta(days=1)
tomorrow_formatted = tomorrow.strftime("%Y-%m-%d %H-%M-%S")
fileName2 = f"Replay {today_formatted}"
# print(today)
name = "Replay 2022-03-15"
list = []
for file in os.listdir(r"C:\Users\swisscom\Videos"):
    if file.startswith(name):
        list.append(os.path.join(r"C:\Users\swisscom\Videos", file))
        oldFileNameDate = datetime.strptime(file, 'Replay %Y-%m-%d %H-%M-%S.mp4')
        print(oldFileNameDate)
        newFileNameDate = oldFileNameDate.strftime("Squadron 42 - Star Citizen %Y.%m.%d %H.%M.%S.00.OBS.mp4")
        print(newFileNameDate)
        newFilePath = "D:\\Vidéos\\Squadron 42 - Star Citizen\\" + newFileNameDate
        print(newFilePath)

for id, file in enumerate(list):
    print(id, file)
    print(len(list))
