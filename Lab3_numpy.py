# -*- coding: utf-8 -*-
import timeit
import numpy as np

# NEW TIMER ################################################
start = timeit.default_timer()
data = np.genfromtxt('house1.txt', dtype='S10,S8,f8,f8,f8,f8,f8,f8,f8', names=True, delimiter=';', )
stop = timeit.default_timer()
execution_time = stop - start
print(u"Чтение numpy метод genfromtxt 1 000 000 записей " + str(execution_time)) #It returns time in sec
print data.size

# NEW TIMER ################################################
start = timeit.default_timer()
data1 = data[data['Global_active_power'] > 5.0]
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 1) Выборка numpy (Global_active_power > 5) из 1 000 000 записей " + str(execution_time))
print data1[0:3]
print data1.size

# NEW TIMER ################################################
start = timeit.default_timer()
data2 = data[data['Voltage'] > 235.0]
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 2) Выборка numpy (Voltage > 235) из 1 000 000 записей " + str(execution_time))
print data2[0:3]
print data2.size

# NEW TIMER ################################################
start = timeit.default_timer()
data3 = data[(data['Global_intensity'] >= 19.0) & (data['Global_intensity'] <= 20.0) & (data['Sub_metering_2'] > data['Sub_metering_3'])]
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 3) Выборка numpy (Global_intensity >= 19 A and <= 20 A) из 1 000 000 записей " + str(execution_time))
print data3[0:3]
print data3.size

# NEW TIMER ################################################
start = timeit.default_timer()
mask = np.random.choice([False, True], len(data), p=[0.45, 0.55])
data4 = data[mask]
data4 = data4[np.logical_not(np.isnan(data4['Sub_metering_1']))]
data4 = data4[np.logical_not(np.isnan(data4['Sub_metering_2']))]
data4 = data4[np.logical_not(np.isnan(data4['Sub_metering_3']))]
data4 = data4[:500000]
stop = timeit.default_timer()
execution_time = stop - start
print(u"Выборка numpy 500 000 случайных записей из 1 000 000 записей " + str(execution_time))
print data4[0:3]
print data4.size

# NEW TIMER ################################################
start = timeit.default_timer()
sub1_mean = np.mean(data4['Sub_metering_1'],axis=0)
sub2_mean = np.mean(data4['Sub_metering_2'],axis=0)
sub3_mean = np.mean(data4['Sub_metering_3'],axis=0)
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 4) Выборка numpy из 500 000 записей " + str(execution_time))
print ("sub1_mean " + str(sub1_mean))
print ("sub2_mean " + str(sub2_mean))
print ("sub3_mean " + str(sub3_mean))
print data4.size


# NEW TIMER ################################################
start = timeit.default_timer()
data5 = data4[(data4['Time'] >= '18:00:00') & ((data4['Sub_metering_1'] + data4['Sub_metering_2'] + data4['Sub_metering_3']) > 6.0) & (data4['Sub_metering_2'] > data4['Sub_metering_1']) & (data4['Sub_metering_2'] > data4['Sub_metering_3'])]
size1 = data5.size
list1 = [i * 3 for i in range(0,((size1/6)+1))]
list2 = [i * 4 for i in range(((size1/8)+1),((size1/4+1)))]
list1 =list1 + list2
data6 = data5[list1]
stop = timeit.default_timer()
execution_time = stop - start
print(u"(Задание 5)Выборка numpy из 500 000 записей " + str(execution_time))
print data5.size
print data6.size





