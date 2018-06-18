# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
import glob
reload(sys)
sys.setdefaultencoding('utf-8')
regions = {"01": " Вінницька ", "02": " Волинська ", "03": " Дніпропетровська ",
"04": " Донецька ", "05": " Житомирська ", "06": " Закарпатська ",
"07": " Запорізька ", "08": " Івано-Франківська ", "09": " Київська ",
"10": " Кіровоградська ", "11": " Луганська ", "12": " Львівська ",
"13": " Миколаївська ", "14": " Одеська ", "15": " Полтавська ",
"16": " Рівенська ", "17": " Сумська ", "18": " Тернопільська ",
"19": " Харківська ", "20": " Херсонська ", "21": " Хмельницька ",
"22": " Черкаська ", "23": " Чернівецька ", "24": " Чернігівська ",
"25": " Республіка Крим ", "26": " м.Київ ", "27": " м.Севастопіль "}
i = 1
while i != 0:
    print 'Введите код региона (01-27):'
    kod = raw_input()
#    print kod
#    if kod.isdigit() and kod < 10 and kod > 0:
#        kod = '0' + str(kod)
#    else:
#        continue
    i = 0
    try:
        name_region = regions[kod]
    except (TypeError, ValueError, KeyError):
        i = 1
print name_region
#df = pd.read_csv('vhi_id_01_20180530-013120.csv', index_col=False, header=1, sep=' ')
#print list(df.columns.values)
#print df[:1]
#mask_file = 'vhi_id_' + kod + '*' + '.csv'
#print mask_file
name_file = glob.glob('vhi_id_' + kod + '*''.csv')
name_file = name_file.pop()
print name_file
df = pd.read_csv(name_file, sep=' ', names= [ 'Year', 'Week', 'Oblast', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI' ])
#print(df.head())
#print df[(df['Year']==2018) & (df['Week']==18)]
region = df['Oblast']
region = (region[1])
#print region
df = df[['Year', 'Week', 'VHI']]
df = df[(df['Year']==2018)]
df1 = df.sort_values('VHI')
df1_min = df1.head(1)
df1_max = df1.tail(1)
vhi_min = 'Min = ' + str(df['VHI'].min())
vhi_max = 'Max = ' + str(df['VHI'].max())
#print 'Минимальное значение VHI ' + vhi_min
#print 'Максимальное значение VHI ' + vhi_max
fig, ax = plt.subplots()
ax.set_title(u'Значение индекса VHI за 2018 год в ' + region)
ax.set_xlabel(u'Недели')
ax.set_ylabel('VHI')
ax.plot(df.Week, df.VHI, color='green')
ax.grid(True, linestyle='-', color='0.75')
ax.plot(df1_min.Week, df1_min.VHI, "ro")
ax.text(df1_min.Week, df1_min.VHI, '   ' + vhi_min) #ax.text (х, у, текст)
ax.plot(df1_max.Week, df1_max.VHI, "ro")
ax.text(df1_max.Week, df1_max.VHI, '   ' + vhi_max) #ax.text (х, у, текст)
#ax.text(1, df1_min.VHI, vhi_min + '   ' + vhi_max) #ax.text (х, у, текст)

#fig.savefig("test.png")
plt.show()

