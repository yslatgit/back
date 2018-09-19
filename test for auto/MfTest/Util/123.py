import os

result = os.popen("adb shell pm list package -3")
app_3 = result.readlines()
list = []
for i in app_3:
    list.append(i)

for i in list:
    print i