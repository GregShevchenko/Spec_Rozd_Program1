# -*- coding: utf-8 -*-
import timeit
import pandas as pd

# NEW TIMER ################################################
start = timeit.default_timer()
df = pd.read_csv('house1.txt', sep=';', low_memory=False)
stop = timeit.default_timer()
execution_time = stop - start
print(u"Чтение pandas (метод read_csv) 1 000 000 записей " + str(execution_time)) #It returns time in sec
#print(df.head(2))

df = df.dropna()
print df.size
print len(df)

# NEW TIMER ################################################
start = timeit.default_timer()
df1 = df[(df['Global_active_power'] > '5.0')]
stop = timeit.default_timer()
execution_time = stop - start
print(u"Выборка pandas (Global_active_power > 5) из 1 000 000 записей " + str(execution_time))
df1 = df1[['Date', 'Time', 'Global_active_power']]
print(df1.head(2))

# NEW TIMER ################################################
start = timeit.default_timer()
df2 = df[(df['Voltage'] > '235.0')]
stop = timeit.default_timer()
execution_time = stop - start
print(u"Выборка pandas (Voltage > 235) из 1 000 000 записей " + str(execution_time))
df2 = df2[['Date', 'Time', 'Voltage']]
print(df2.head(2))


# NEW TIMER ################################################
start = timeit.default_timer()
df3 = df[(df['Global_intensity'] >= '19.0') & (df['Global_intensity'] <= '20.0')
    & (df.Sub_metering_2.astype(float) > df.Sub_metering_3.astype(float))]
df3 = df3[['Date', 'Global_intensity', 'Sub_metering_2', 'Sub_metering_3']]#''Time''
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 3) Выборка pandas (Global_intensity >= 19 A and <= 20 A) из 1 000 000 записей " + str(execution_time))
print df3[:3]
print df3.size

# NEW TIMER ################################################
start = timeit.default_timer()
df4 = df.sample(n=500000)
print "sub1_mean " + str(df4.Sub_metering_1.astype(float).mean())
print "sub2_mean " + str(df4.Sub_metering_2.astype(float).mean())
print "sub3_mean " + str(df4.Sub_metering_3.astype(float).mean())
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 4) Выборка pandas 500 000 случайных записей из 1 000 000 записей " + str(execution_time))
print df4.head(2)
print df4.size
print len(df4)

# NEW TIMER ################################################
start = timeit.default_timer()
df5 = df4[(df4['Time'] >= '18:00:00')
    & ((df4.Sub_metering_1.astype(float) + df4.Sub_metering_2.astype(float) + df4.Sub_metering_3.astype(float)) > 6.0)
    & (df.Sub_metering_2.astype(float) > df.Sub_metering_1.astype(float))
    & (df.Sub_metering_2.astype(float) > df.Sub_metering_3.astype(float))]
size1 = len(df5)
list1 = [i * 3 for i in range(0,((size1/6)+1))]
list2 = [i * 4 for i in range(((size1/8)+1),((size1/4+1)))]
list1 = list1 + list2
df5 = df5.reset_index(drop=True)
df6 = df5.ix[list1]
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 5) Выборка pandas 500 000 случайных записей из 1 000 000 записей " + str(execution_time))
print df5.head(20)
print df6.head(20)
print df6.size
print len(df6)


