import os
import shutil

maplePath = "C:/Nexon/Maple/"
screenshotPath = maplePath + "screenshot/"
fileList = os.listdir(maplePath)

screenshot = [file for file in fileList if file.endswith(".jpg")]
screenshotPng = [file for file in fileList if file.endswith(".png")]
screenshot.extend(screenshotPng)

for img in screenshot:
    shutil.move(maplePath + img, screenshotPath + img)
