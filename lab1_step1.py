# -*- coding: utf-8 -*-
import  urllib2
import time
regions_sopostovlenie = {"1": "22", "2": "24", "3": "23",
"4": "25", "5": "03", "6": "04",
"7": "08", "8": "19", "9": "20",
"10": "21", "11": "09", "12": "26",
"13": "10", "14": "11", "15": "12",
"16": "13", "17": "14", "18": "15",
"19": "16", "20": "27", "21": "17",
"22": "18", "23": "6", "24": "01",
"25": "02", "26": "07", "27": "05"}
i = 1
while i <= 27:
    old_kod_oblasti = str(i)
    print i
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+ old_kod_oblasti + "&year1=1981&year2=2018&type=Mean"
    try: vhi_url = urllib2.urlopen(url)
    except urllib2.URLError as e:
        print e.reason
        continue
    timelabel = time.strftime("%Y%m%d-%H%M%S")
    print (timelabel)
    new_kod_oblasti = regions_sopostovlenie[old_kod_oblasti]
    filename = 'vhi_id_' + new_kod_oblasti + '_' + timelabel + '.csv'
    out = open(filename, 'wb')
    out.write(vhi_url.read())
    out.close()
    print ("VHI is downloaded... %s" % (filename))
    i = i + 1
