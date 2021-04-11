import csv

filename = "D:\BaiduNetdiskDownload\Python编程 从入门到实践\《Python编程》源代码文件\chapter_16\sitka_weather_07_2014"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)