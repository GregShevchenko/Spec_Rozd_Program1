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
    i = 0
    try:
        name_region = regions[kod]
    except (TypeError, ValueError, KeyError):
        i = 1
name_file = glob.glob('vhi_id_' + kod + '*''.csv')
name_file = name_file.pop()
df = pd.read_csv(name_file, sep=' ', names= [ 'Year', 'Week', 'Oblast', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI' ])
region = df['Oblast']
region = (region[1])
df = df[['Year', 'VHI']]
print df.columns.values
df = df[(df['VHI'] <= 35) & (df['VHI'] > 15)]
df = df.groupby(['Year'])['VHI'].mean().reset_index()
print df

fig, ax = plt.subplots()
ax.set_title(u'VHI > 15 но < 35 ' + region)
ax.set_xlabel(u'Year')
ax.set_ylabel('VHI')
ax.plot(df['Year'], df['VHI'], "ro" )
ax.grid(True, linestyle='-', color='0.75')
#fig.savefig("test.png")
plt.show()

