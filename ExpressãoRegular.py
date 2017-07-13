import re


texto = ''';background-image:url(/az/hprichbg/rb/GrusJaponensis_PT-BR8754475029_1920x1080.jpg);
}.hp_sw_logo{float:left;text-indent:-20em;_padding-'''.split(';')

link_re = re.compile(r'rb/.*\.jpg')
ret = []
for linha in texto:    
    ret+=link_re.findall(linha)
    print(linha)
print(ret)
