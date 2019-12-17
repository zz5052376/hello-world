import os
import re

path = r'E:\xinhaoye\study\网易云uc缓存\res_xieyang'

for root, dir, files in os.walk(path):
    for file in files:
        if '.html' in file:
            file_path = os.path.join(root, file)
            # print(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                a = f.read()
            ttt = re.findall('(<title><title>(.+_iseetest官网)</title></title>)', a)[0]
            ppp = '<title>'+ttt[1]+'</title>'+'\n<link href="./css/style.css" rel="stylesheet" type="text/css">\n<link rel="stylesheet" href="./css/smoothproducts.css">\n<link rel="stylesheet" href="./css/zxkf.css">\n<link rel="stylesheet" href="./css/font-awesome.css">\n'
            a = a.replace(ttt[0], ppp)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(a)




