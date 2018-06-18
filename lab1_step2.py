# -*- coding: utf-8 -*-

import os
directory = '/home/greg/SRP1/Spec_Rozd_Program1'
all_files = os.listdir(directory)
list_files = filter(lambda x: x.endswith('.csv'), all_files)
print list_files

regions = {"01": " Вінницька ", "02": " Волинська ", "03": " Дніпропетровська ",
"04": " Донецька ", "05": " Житомирська ", "06": " Закарпатська ",
"07": " Запорізька ", "08": " Івано-Франківська ", "09": " Київська ",
"10": " Кіровоградська ", "11": " Луганська ", "12": " Львівська ",
"13": " Миколаївська ", "14": " Одеська ", "15": " Полтавська ",
"16": " Рівенська ", "17": " Сумська ", "18": " Тернопільська ",
"19": " Харківська ", "20": " Херсонська ", "21": " Хмельницька ",
"22": " Черкаська ", "23": " Чернівецька ", "24": " Чернігівська ",
"25": " Республіка Крим ", "26": " м.Київ ", "27": " м.Севастопіль "}


for fileName in list_files:
    file1 = open(fileName, 'rb')
    print fileName + ' open...'
    lines = file1.readlines()
    file1.close()
    index_kod_region = fileName.find('vhi_id_')
    kod_region = fileName[index_kod_region + 7:index_kod_region + 9]
    name_region = regions[kod_region]
    file2 = open('temp.tmp', 'ab')
    for line in lines:
        if line.find('<br>') != -1 or line.find('<pre>') != -1 or line.find('</pre>') != -1:
            line = line.replace(line, '')
            continue
        line = line[:8] + name_region + line[8:]
        line = line.replace(',', ' ')
        while line.find('  ') != -1:
            line = line.replace('  ', ' ')
        file2.writelines(line)
    file2.close()
    os.remove(fileName)
    os.rename('temp.tmp', fileName)
    print fileName + ' write...'