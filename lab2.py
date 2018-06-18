# -*- coding: utf-8 -*-
from spyre import server
#from googlefinance.client import get_price_data
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
import glob
reload(sys)
sys.setdefaultencoding('utf-8')

#server.include_df_index = True


class RegionsData(server.App):
    title = u"Спеціальні розділи програмування 1"

    inputs = [{
        "type": 'dropdown',
        "label": u'Область',
        "options": [
            {"label": u"Вінницька", "value": "01"},
            {"label": u"Волинська", "value": "02"},
            {"label": u"Дніпропетровська", "value": "03"},
            {"label": u"Донецька", "value": "04"},
            {"label": u"Житомирська", "value": "05"},
            {"label": u"Закарпатська", "value": "06"},
            {"label": u"Запорізька", "value": "07"},
            {"label": u"Івано-Франківська", "value": "08"},
            {"label": u"Київська", "value": "09"},
            {"label": u"Кіровоградська", "value": "10"},
            {"label": u"Луганська", "value": "11"},
            {"label": u"Львівська", "value": "12"},
            {"label": u"Миколаївська", "value": "13"},
            {"label": u"Одеська", "value": "14"},
            {"label": u"Полтавська", "value": "15"},
            {"label": u"Рівенська", "value": "16"},
            {"label": u"Сумська", "value": "17"},
            {"label": u"Тернопільська", "value": "18"},
            {"label": u"Харківська", "value": "19"},
            {"label": u"Херсонська", "value": "20"},
            {"label": u"Хмельницька", "value": "21"},
            {"label": u"Черкаська", "value": "22"},
            {"label": u"Чернівецька", "value": "23"},
            {"label": u"Чернігівська", "value": "24"},
            {"label": u"Республіка Крим", "value": "25"},
            {"label": u"м.Київ", "value": "26"},
            {"label": u"м.Севастопіль", "value": "27"}
            ],
            "key": 'ticker',
            "action_id": "update_data"
            },
            {
            "type": 'dropdown',
            "label": u'Вибір індексу',
            "options": [
            {"label": "VHI", "value": "VHI"},
            {"label": "TCI", "value": "TCI"},
            {"label": "VCI", "value": "VCI"}
            ],
            "key": 'ticker_ind',
            "action_id": "update_data"
            },
            {
            "type": 'slider',
            "label": u'Початок діапазону тижнів',
            "min": 1, "max": 52, "value": 1,
            "key": 'ticker_week_start',
            "action_id": 'update_data'
            },
            {
            "type": 'slider',
            "label": u'Кінець діапазону тижнів',
            "min": 1, "max": 52, "value": 52,
            "key": 'ticker_week_finish',
            "action_id": 'update_data'
            },
            {
            "type": 'slider',
            "label": u'Початок діапазону років',
            "min": 1981, "max": 2018, "value": 1981,
            "key": 'ticker_year_start',
            "action_id": 'update_data'
            },
            {
            "type": 'slider',
            "label": u'Кінець діапазону років',
            "min": 1981, "max": 2018, "value": 2018,
            "key": 'ticker_year_finish',
            "action_id": 'update_data'
            }
            ]

    tabs = [u"Графік", u"Таблиця"]

    outputs = [{
        "type": "plot",
        "id": "plot",
        "control_id": "update_data",
        "tab": u"Графік"
    }, {
        "type": "table",
        "id": "table_id",
        "control_id": "update_data",
        "tab": u"Таблиця"
    }]

    controls = [{
        "type": "hidden",
        "label": "get stock data",
        "id": "update_data"
    }]

    def getData(self, params):
        name_file = glob.glob('vhi_id_' + params['ticker'] + '*''.csv')
        name_file = name_file.pop()
        df = pd.read_csv(name_file, sep=' ', names= [ 'Year', 'Week', 'Oblast', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI' ])
        df = df[['Year', 'Week','Oblast', 'SMN', 'SMT', params['ticker_ind']]]
        df = df[(df['Week']>=params['ticker_week_start']) & (df['Week']<=params['ticker_week_finish'])]
        df = df[(df['Year']>=params['ticker_year_start']) & (df['Year']<=params['ticker_year_finish'])]
#        #print df[(df['Year']==2018) & (df['Week']==18)]
#        df = df.drop(['Oblast'], axis='columns')
#        ticker = params['ticker']
#        xchng = "NASD"
#        param = {
#            'q': ticker,  # Stock symbol (ex: "AAPL")
#            'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
#            'x': xchng,  # Stock exchange symbol on which stock is traded (ex: "NASD")
#            'p': "3M"  # Period (Ex: "1Y" = 1 year)
#        }
#        df = get_price_data(param)
#        return df.drop('Volume', axis=1)
        return df


    def getPlot(self, params):
        df = self.getData(params)
        df = df[['Year', 'Week', params['ticker_ind']]]
#        df["DT"] = pd.to_datetime(df.Year.astype(str)+
#                          df.Week.astype(str) ,format='%Y%W')
        df["DT"] = pd.to_datetime(df.Year.astype(str) + df.Week.astype(str).add('-0') ,format='%Y%W-%w')
#        df = df.drop((['Oblast'], ['SMN'], ['SMT']), axis='columns')
#        df = df.pivot_table(['Year'], ['Week'])
#        df = df.pivot_table(params['ticker_ind'], index='Year', columns='Week')
#        print df

#        plt_obj = plot(df['Year'], df[params['ticker_ind']], "ro")
#        plt_obj.set_ylabel(params['ticker_ind'])
#        plt_obj.set_xlabel("Year")
#        plt_obj.set_title(params['ticker_ind'])
        fig, ax = plt.subplots()
        ax.set_title(params['ticker_ind'])
        ax.set_xlabel(u'Year')
        ax.set_ylabel(params['ticker_ind'])
        ticker_ind = str(params['ticker_ind'])
        ax.grid(True, linestyle='-', color='0.75')
        ax.plot(df['DT'], df[ticker_ind], "g-" )
        return ax



app = RegionsData()
app.launch()