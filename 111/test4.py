import requests
import re
import time
import os


base_path_1 = 'http://www.iseetest.com/products/list_2_'
base_path_2 = 'http://www.iseetest.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host':'www.iseetest.com',
}
k = 0
k_li = []
for i in range(1, 22):
    path_1 = base_path_1 + str(i) + '.html'
    print('-------------------------------------------')
    print(path_1)

    res = requests.get(path_1, headers=headers)
    a = res.text
    # print(a)
    a_li = re.findall('<a href="(.+?)" class="mask" target="_blank">', a)
    for tmp in a_li:
        k += 1
        path_2 = base_path_2 + tmp
        b = tmp.split('/')[-1]
        html_name = 'res_xieyang/' +str(k)+'_'+ b

        k_li.append(html_name)
        if os.path.exists(html_name):
            continue
        print(path_2)

        res_2 = requests.get(path_2)
        res_2.encoding = 'utf-8'
        a_2 = res_2.text
        a_2_li = re.findall('(<div id="news" class="scrol-page">[\d\D]*?)<div class="footer">', a_2)

        title = re.findall(r'<title>.+?_iseetest官网</title>', a_2)[0]

        for tmp2 in a_2_li:
            # print(tmp2)

            with open(html_name, 'w', encoding='utf-8') as f:
                f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>'+title+'</title>\n</head>\n<body>\n')
                f.write('<p>'+title+'</p>')
                f.write(tmp2,)
                f.write('</body>\n</html>')
        time.sleep(2)
    time.sleep(5)

print(k)
print(len(k_li))
print(len(set(k_li)))