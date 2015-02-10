import requests
from climostations import climo_stations
snowfall_file = open("2014-15 Seasonal Snowfall Totals.csv", "w")
for nws_office in climo_stations:
    for climo_station in nws_office[1:]:
        url = 'http://www.nws.noaa.gov/data/' + nws_office[0] + "/CLI" + climo_station
        data = requests.get(url)

        # dump resulting text to file
        with open("CLI" + climo_station + ".txt", "w") as out_f:
            out_f.write(data.text)

        print(climo_station + ": ", end='')
        snowfall_file.write(climo_station + ",")
        fp = open("CLI" + climo_station + ".txt")
        for i, line in enumerate(fp):
            if 32 < i < 46 and (line[2:13] in ['SINCE JUL 1', 'SINCE SEP 1']) or (line[1:12] in ['SINCE JUL 1',
                'SINCE SEP 1']):
                char_num = 17
                while line[char_num] == ' ':  # Check where seasonal snowfall starts
                    char_num += 1
                while line[char_num] not in [' ', '\n']:
                    print(line[char_num], end='')
                    snowfall_file.write(line[char_num])
                    char_num += 1
                snowfall_file.write("\n")
                print()
                break
        fp.close()
snowfall_file.close()