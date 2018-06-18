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

#colums_name = 'Год Неделя Область SMN SMT VCI TCI VHI'

for fileName in list_files:
    file1 = open(fileName, 'rb')
    print fileName + ' open...'
    lines = file1.readlines()
    file1.close()
    index_kod_region = fileName.find('vhi_id_')
    kod_region = fileName[index_kod_region + 7:index_kod_region + 9]
    name_region = regions[kod_region]
    file2 = open('temp.tmp', 'ab')
#    line1 = 'Год Неделя Область SMN SMT VCI TCI VHI \n'
#    file2.writelines(line1)
    for line in lines:
    #    print line
        if line.find('<br>') != -1 or line.find('<pre>') != -1 or line.find('</pre>') != -1:
            line = line.replace(line, '')
    #        print line
            continue
        line = line[:8] + name_region + line[8:] #+ '\n'
        line = line.replace(',', ' ')
        while line.find('  ') != -1:
            line = line.replace('  ', ' ')
    #    print line
        file2.writelines(line)
#    text = text.replace('  ', name_region)
#lines = lines.insert(0, colums_name)
#file1 = open(fileName, 'wb')
#file1.writelines(lines)
    file2.close()
    os.remove(fileName)
    os.rename('temp.tmp', fileName)
    print fileName + ' write...'




#    line = file1.readline()
#    while line:
#        print (line),
#        line = file1.readline()
#    f.close()

#    index_kod_region1 = text.find('Province= ') + 10
#    index_kod_region2 = text.find(':')
#    kod_region = text[index_kod_region1: index_kod_region2]
#3) интересный момент, если нужно из строки убрать первые <n> символов
#s = s[n:]
#5) заменить часть строки
#s = s.replace( ‘camera’, ‘object’ )


#def ReplaceLineInFile(fileName, sourceText, replaceText):
#    file = open(fileName, 'r') #Opens the file in read-mode
#    text = file.read() #Reads the file and assigns the value to a variable
#    file.close() #Closes the file (read session)
#    file = open(fileName, 'w') #Opens the file again, this time in write-mode
#    file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
#    # and writes the whole output when done, wiping over the old contents of the file
#    file.close() #Closes the file (write session)
#    print 'All went well, the modifications are done'


#import pandas as pd
#df = pd.read_csv('vhi_id_1_20180527-013535.csv', index_col=False, header=1)
#print list(df.columns.values)
#print df[:1]

#df[(df['year']==2000) & (df['week']==18)]
#print df[:1]