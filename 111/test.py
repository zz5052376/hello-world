import requests
import re
import time
import os


# base_path_1 = 'http://www.iseetest.com/news/list_4_1.html'
base_path_1 = 'http://www.iseetest.com/news/list_4_'
base_path_2 = 'http://www.iseetest.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',

}

num = 1
for i in range(1, 16):
    time.sleep(5)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    path_1 = base_path_1+str(i)+'.html'
    print(path_1)
    res = requests.get(path_1, headers=headers)
    a = res.text
    a_li = re.findall('<h4><a href="(/news/.+?)"', a)
    print(a_li)
    for tmp in a_li:
        path_2 = base_path_2+tmp
        b = tmp.split('/')[-1]
        html_name = 'res/' + b
        if os.path.exists(html_name):
            continue
        print(path_2)
        res_2 = requests.get(path_2)
        res_2.encoding = 'utf-8'
        a_2 = res_2.text
        a_2_li = re.findall('(<div class="body">[\d\D]*?)<div class="paging">', a_2)
        title = re.findall('<title>(.+?)_iseetest官网</title>', a_2)[0]

        for tmp2 in a_2_li:
            # html_name = 'res/'+str(num)+'.html'
            # html_name = 'res/'+str(title)+'_'+ b
            html_name = 'res/'+ b
            print(html_name)
            with open(html_name, 'w', encoding='utf-8') as f:
                f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>'+title+'</title>\n</head>\n<body>\n')
                f.write('<p>'+title+'</p>')
                f.write(tmp2,)
                f.write('</body>\n</html>')
                num += 1
        time.sleep(2)


