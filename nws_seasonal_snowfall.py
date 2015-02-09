import requests
climo_stations = [['BOX', 'BOS', 'BDL', 'ORH', 'PVD'], ['OKX', 'NYC', 'LGA', 'JFK', 'ISP', 'BDR', 'EWR'], ['GYX', 'PWM',
    'CON', 'GYX', 'MHT'], ['CAR', 'BGR', 'CAR'], ['BTV', 'BTV'], ['ALY', 'ALB'], ['PHI', 'ABE', 'ACY', 'PHL', 'ILG'],
    ['BGM', 'BGM', 'AVP', 'SYR'], ['BUF', 'BUF', 'ROC'], ['CTP', 'MDT', 'IPT'], ['PIT', 'PIT'], ['LWX', 'DCA', 'BWI',
    'IAD'], ['CLE', 'CLE', 'TOL', 'MFD', 'CAK', 'YNG', 'ERI'], ['RLX', 'BKW', 'CRW', 'EKN', 'HTS'], ['AKQ', 'RIC', 'ORF'
    , 'SBY', 'ECG', 'WAL'], ['ILN', 'CVG', 'DAY', 'CMH'], ['DTX', 'DTW', 'FNT', 'MBS'], ['APX', 'APN', 'HTL', 'ANJ'],
    ['IWX', 'FWA', 'SBN'], ['MQT', 'MQT'], ['MKX', 'MKE', 'MSN', 'GRB', 'AUW', 'LSE', 'RFD'], ['LOT', 'ORD', 'RFD',
    'DPA', 'LOT'], ['DVN', 'DVN', 'DBQ', 'MLI'], ['MPX', 'MSP', 'STC', 'EAU', 'MPX', 'RST', 'DLH', 'INL', 'FAR', 'FSD'],
    ['DLH', 'FGF'], ['DMX', 'DSM', 'ALO', 'MCW'], ['LSX', 'STL', 'COU'], ['OAX', 'OMA', 'LNK', 'OFK', 'OAX'], ['ABR',
    'ABR', 'PIR', 'ATY', 'MBG', '8D3', 'UNR', 'RAP', 'HON'], ['BIS', 'BIS'], ['MHX', 'HSE', 'EWN'], ['RAH', 'RDU', 'GSO'
    ], ['ILM', 'ILM'], ['CHS', 'CHS', 'SAV'], ['CAE', 'CAE', 'AGS'], ['GSP', 'AVL', 'CLT', 'GSP'], ['RNK', 'RNK', 'ROA',
    'LYH', 'DAN', 'BLF', 'LWB'], ['BOU', 'DEN'], ['GJT', 'GJT'], ['PUB', 'ALS', 'COS', 'PUB'], ['ILX', 'PIA', 'SPI',
    'ILX'], ['IND', 'IND'], ['DDC', 'DGC', 'P28'], ['GLD', 'GLD'], ['TOP', 'TOP', 'CNK'], ['ICT', 'ICT'], ['JKL', 'JKL']
    , ['LMK', 'SDF', 'LEX', 'BWG'], ['PAH', 'PAH', 'EVV'], ['GRR', 'GRR', 'LAN', 'MKG'], ['EAX', 'MCI'], ['SGF', 'SGF']
    , ['GID', 'GRI', 'HSI'], ['LBF', 'LBF', 'VTN'], ['FGF', 'GFK'], ['FSD', 'SUX', 'MHE'], ['GRB', 'RHI'], ['CYS', 'CYS'
    , 'BFF'], ['RIW', 'CPR', 'LND', 'RIW'], ['AFC', 'ANC', 'BET', 'CDB', 'AKN', 'ADQ', 'SNP'], ['AFG', 'FAI', 'BRW',
    'OTZ', 'OME', 'MCG', 'JNU', 'YAK', 'ANN'], ['GUM', 'GUM'], ['HNL', 'HNL', 'LIH', 'OGG', 'ITO'], ['BMX', 'ANB', 'BHM'
    , 'MGM', 'TCL', 'EET', 'TOI'], ['HUN', 'HSV', 'MSL'], ['MOB', 'MOB', 'PNS'], ['LZK', 'LIT', 'LZK', 'HRO', 'PBF'],
    ['JAX', 'GNV', 'JAX', 'AMG', 'SSI'], ['KEY', 'EYW', 'MTH'], ['MLB', 'DAB', 'MCO', 'MLB', 'VRB'], ['MFL', 'MIA',
    'FLL', 'PBI', 'APF'], ['FFC', 'ATL', 'AHN', 'CSG', 'MCN', 'VPC', 'PDK', 'FTY', 'GVL', 'FFC', 'RMG'], ['LCH', 'LCH',
    'BPT', 'LFT', 'AEX', 'ARA'], ['LIX', 'BTR', 'NEW'], ['SHV', 'SHV', 'MLU', 'TXK', 'ELD', 'DEQ', 'TYR', 'GGG', 'LFK'],
    ['JAN', 'JAN', 'MEI'], ['ABQ', 'ABQ', 'CAO', 'ROW'], ['OUN', 'OKC', 'SPS'], ['TSA', 'TUL', 'FSM', 'FYV'], ['SJU',
    'SJU', 'IST', 'ISX'], ['MEG', 'MEM', 'MKL', 'JBR', 'TUP', 'MEG'], ['MRX', 'CHA', 'TYS', 'TRI'], ['OHX', 'BNA'], [
    'AMA', 'AMA', 'BGD', 'DHT', 'GUY'], ['EWX', 'AUS', 'ATT', 'DRT', 'SAT'], ['BRO', 'BRO', 'HRL', 'MFE'], ['CRP', 'CRP'
    , 'VCT'], ['FWD', 'DFW', 'ACT'], ['EPZ', 'ELP'], ['HGX', 'HOU', 'GLS', 'CLL'], ['LUB', 'LBB', 'CDS'], ['MAF', 'MAF']
    , ['SJT', 'ABI', 'SJT'], ['FGZ', 'FLG'], ['PSR', 'PHX'], ['EKA', 'EKA', 'CEC', 'RDD', 'UKI'], ['LOX', 'BUR', 'CMA',
    'CQT', 'LAX', 'LGB', 'PMD', 'PRB', 'SBA', 'SMX', 'WJF'], ['STO', 'RDD', 'SAC', 'SCK', 'MOD'], ['SGX', 'CZZ', 'FUL',
    'SNA', 'OKB', 'ONT', 'PSP', 'RAL', 'RNM', 'SAN', 'TRM'], ['MTR', 'SFO', 'OAK', 'SJC'], ['HNX', 'FAT', 'BFL', 'MAE',
    'MCE', 'HJO'], ['BOI', 'BOI'], ['PIH', 'PIH'], ['BYZ', 'BIL'], ['GGW', 'GGW'], ['TFX', 'BZN', 'GTF', 'HVR', 'HLN'],
    ['MSO', 'MSO', 'GPI'], ['LKN', 'EKO', 'ELY', 'WMC'], ['VEF', 'LAS', 'BIH'], ['REV', 'RNO'], ['MFR', 'MFR'], ['PDT',
    'PDT', 'YKM'], ['PQR', 'EUG', 'HIO', 'MFR'], ['SLC', 'SLC'], ['SEW', 'SEA', 'SEW'], ['OTX', 'GEG', 'LWS', 'OTX']]
snowfall_file = open("2014-15 Seasonal Snowfall Totals.txt", "w")
for nws_office in climo_stations:
    for climo_station in nws_office[1:]:
        url = 'http://www.nws.noaa.gov/data/' + nws_office[0] + "/CLI" + climo_station
        data = requests.get(url)

        # dump resulting text to file
        with open("CLI" + climo_station + ".txt", "w") as out_f:
            out_f.write(data.text)

        print(climo_station + ": ", end='')
        snowfall_file.write(climo_station + ": ")
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