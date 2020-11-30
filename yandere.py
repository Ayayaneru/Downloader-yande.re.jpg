import requests
import time
import re
from os import mkdir,listdir

start = time.time()
url = input('Please input yande.re/pool URL to download jpgs.\n')
folder_name = re.match(r'.+/(.+)',url).group(1)

def download(url_jpg):
    jpg_name = re.sub(r'%20',' ',re.match(r'.+/(.+)',url_jpg).group(1))
    for file in listdir(folder_name):
        # 跳过已有文件
        if file == jpg_name:
            print('[pass]')
            return
    try:
        jpg = requests.get(url_jpg)
    except:
        main()    
    jpg_path = folder_name + '/' + jpg_name
    with open(jpg_path,'wb') as f:
        f.write(jpg.content)

def main():
    try:
        mkdir(folder_name)
    except:
        pass

    pool = str(requests.get(url).content)
    jpg_count = 0
    for jpg_url in re.findall(r'"jpeg_url":"(.+?)"',pool):
        # time.sleep(1)
        jpg_count+=1
        print('Downloading',jpg_count)
        download(jpg_url)

    end = time.time()
    print('Download jpgs amount to',jpg_count,' [cost',int(end-start),'s]')

main()
