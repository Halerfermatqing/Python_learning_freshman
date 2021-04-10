path = input("请选这文件：")
#通过文件扩展名判断文件类型
p = path.rfind("\\")
file_name = path[p+1:]

if file_name.endswith('jpg') or file_name.endswith("png"):
    print("允许上传，验证是图片。")
else:
    print("不是图片格式，禁止上传！")