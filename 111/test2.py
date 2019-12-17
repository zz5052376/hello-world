import os
import re
import requests


def down_load(path, go_path):
    pass
    res = requests.get(path)
    a = res.content
    with open(go_path, 'wb') as f:
        f.write(a)


# http://www.iseetest.com/uploads/allimg/190318/1-1Z31Q04QT63.jpg
# http://www.iseetest.com/uploads/allimg/190318/14L15RVU540-45510.jpg
# /uploads/allimg/190318/1-1Z31Q04QT63.jpg

base_path = r'E:\xinhaoye\study\网易云uc缓存\res_xieyang'

li = os.listdir(base_path)
for tmp in li:
    if '.html' in tmp and 'local' not in tmp:
        html_path = os.path.join(base_path, tmp)
        print(html_path)
        with open(html_path, 'r', encoding='utf-8') as f:
            a = f.read()
            # pic_li = re.findall('<img alt=".*?" src="(.+?)" /></center>',a)
            jpg_li = re.findall('src="(.+?\.jpg)"',a)
            png_li = re.findall('src="(.+?\.png)"',a)
            print(jpg_li)
            for jpg_path in jpg_li:
                jpg_name = jpg_path.split('/')[-1]
                go_path = 'res_xieyang/imgs/'+jpg_name
                print(jpg_path)
                print(jpg_name)
                a = a.replace(jpg_path, './imgs/'+jpg_name)
                if 'http' not in jpg_path:
                    jpg_path = 'http://www.iseetest.com'+jpg_path

                if not os.path.exists(go_path):
                    down_load(jpg_path, go_path)
            print(png_li)
            for png_path in png_li:
                png_name = png_path.split('/')[-1]
                go_path = 'res_xieyang/imgs/' + png_name
                print(png_path)
                print(png_name)
                a = a.replace(png_path, './imgs/'+png_name)
                if 'http' not in png_path:
                    png_path = 'http://www.iseetest.com'+png_path

                if not os.path.exists(go_path):
                    down_load(png_path, go_path)

            with open(html_path[:-5]+'_local_pic'+'.html', 'w', encoding='utf-8') as f2:
                f2.write(a)




