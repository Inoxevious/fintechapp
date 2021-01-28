import csv
from companies import models

# opfile  =  '/home/greats/Documents/projects/dreatol/webapp/fintechapp/clean_applications.csv'

def get_data(csv_file):
    opfile = csv_file
    header  =  []
    lbfile  =  open(opfile, "rt")
    reader  =  csv.reader(lbfile)
    rownum  =  0
    for row in reader:
        if rownum  ==  0:
            header.append(row)
            rownum += 1
        else:
            the_row  =  models.LoanApplication(SK_ID_CURR = row[0],TARGET = row[1],NAME_CONTRACT_TYPE = row[2],CODE_GENDER = row[3],FLAG_OWN_CAR = row[4],FLAG_OWN_REALTY = row[5],
                        CNT_CHILDREN = row[6],AMT_INCOME_TOTAL = row[7],AMT_CREDIT = row[8],AMT_ANNUITY = row[9],AMT_GOODS_PRICE = row[10],NAME_TYPE_SUITE = row[11],NAME_INCOME_TYPE = row[12],NAME_EDUCATION_TYPE = row[13],NAME_FAMILY_STATUS = row[14],NAME_HOUSING_TYPE = row[15],
                        REGION_POPULATION_RELATIVE = row[16],DAYS_BIRTH = row[17],DAYS_EMPLOYED = row[18],DAYS_REGISTRATION = row[19],DAYS_ID_PUBLISH = row[20],OWN_CAR_AGE = row[21],FLAG_MOBIL = row[22],FLAG_EMP_PHONE = row[23],FLAG_WORK_PHONE = row[24],FLAG_CONT_MOBILE = row[25],
                        FLAG_PHONE = row[26],FLAG_EMAIL = row[27],OCCUPATION_TYPE = row[28],CNT_FAM_MEMBERS = row[29],REGION_RATING_CLIENT = row[30],REGION_RATING_CLIENT_W_CITY = row[31],WEEKDAY_APPR_PROCESS_START = row[32],HOUR_APPR_PROCESS_START = row[33],REG_REGION_NOT_LIVE_REGION = row[34],REG_REGION_NOT_WORK_REGION = row[35],
                        LIVE_REGION_NOT_WORK_REGION = row[36],REG_CITY_NOT_LIVE_CITY = row[37],REG_CITY_NOT_WORK_CITY = row[38],LIVE_CITY_NOT_WORK_CITY = row[39],ORGANIZATION_TYPE = row[40],EXT_SOURCE_1 = row[41],EXT_SOURCE_2 = row[42],EXT_SOURCE_3 = row[43],APARTMENTS_AVG = row[44],BASEMENTAREA_AVG = row[45],
                        YEARS_BEGINEXPLUATATION_AVG = row[46],YEARS_BUILD_AVG = row[47],COMMONAREA_AVG = row[48],ELEVATORS_AVG = row[49],ENTRANCES_AVG = row[50],FLOORSMAX_AVG = row[51],FLOORSMIN_AVG = row[52],LANDAREA_AVG = row[53],LIVINGAPARTMENTS_AVG = row[54],LIVINGAREA_AVG = row[55],
                        NONLIVINGAPARTMENTS_AVG = row[56],NONLIVINGAREA_AVG = row[57],APARTMENTS_MODE = row[58],BASEMENTAREA_MODE = row[59],YEARS_BEGINEXPLUATATION_MODE = row[60],YEARS_BUILD_MODE = row[61],COMMONAREA_MODE = row[62],ELEVATORS_MODE = row[63],ENTRANCES_MODE = row[64],FLOORSMAX_MODE = row[65],
                        FLOORSMIN_MODE = row[66],LANDAREA_MODE = row[67],LIVINGAPARTMENTS_MODE = row[68],LIVINGAREA_MODE = row[69],NONLIVINGAPARTMENTS_MODE = row[70],NONLIVINGAREA_MODE = row[71],APARTMENTS_MEDI = row[72],BASEMENTAREA_MEDI = row[73],YEARS_BEGINEXPLUATATION_MEDI = row[74],YEARS_BUILD_MEDI = row[75],
                        COMMONAREA_MEDI = row[76],ELEVATORS_MEDI = row[77],ENTRANCES_MEDI = row[78],FLOORSMAX_MEDI = row[79],FLOORSMIN_MEDI = row[80],LANDAREA_MEDI = row[81],LIVINGAPARTMENTS_MEDI = row[82],LIVINGAREA_MEDI = row[83],NONLIVINGAPARTMENTS_MEDI = row[84],NONLIVINGAREA_MEDI = row[85],
                        FONDKAPREMONT_MODE = row[86],HOUSETYPE_MODE = row[87],TOTALAREA_MODE = row[88],WALLSMATERIAL_MODE = row[89],EMERGENCYSTATE_MODE = row[90],OBS_30_CNT_SOCIAL_CIRCLE = row[91],DEF_30_CNT_SOCIAL_CIRCLE = row[92],OBS_60_CNT_SOCIAL_CIRCLE = row[93],DEF_60_CNT_SOCIAL_CIRCLE = row[94],DAYS_LAST_PHONE_CHANGE = row[95],
                        FLAG_DOCUMENT_2 = row[96],
            )
            the_row.save()

