import urllib.request
import re
import os

from WallPaper import ChangeWallPaper


pag = urllib.request.urlopen('https://www.bing.com/')
text = pag.read().decode('utf8').split(';')

link_re = re.compile(r'rb/.*\.jpg')
ret = ''
for line in text:
    if(link_re.findall(line)!=[]):
        ret=''.join(link_re.findall(line))

url = 'https://www.bing.com/az/hprichbg/%s'%ret

getName = ret.split('/')

print('Download from Bing: %s'%getName[1])

foto = urllib.request.urlopen(url).read()
file = open(getName[1],'wb')
file.write(foto)
file.close()

path = os.path.realpath(file.name)

x = ChangeWallPaper(path)
x.change_wallpaper()

