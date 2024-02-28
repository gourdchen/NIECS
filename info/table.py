import pandas as pd
import numpy as np

def match_table(core_table,sub_table,sub_table_name,upper_bound = 180,lower_bound = 180,on='record_id',left_date='date_of_diagnosis',right_date='scan_date'):
    '''
    find the closest record from sub_table for each row of core_table that satified the condition
    can be used in match MRI scan vist and Clinical visit.
    upper_bound : core table after sub table days Days
    lower_bound : core table before sub table days Days

    '''
    infotable = core_table.copy()
    upper_bound = pd.Timedelta("%ddays" % upper_bound)
    lower_bound = pd.Timedelta("%ddays" % lower_bound)

    for index,row in sub_table.iterrows():
        mask = (infotable[on] == row[on]) & ((infotable[left_date] < row[right_date] + upper_bound) & (infotable[left_date] > row[right_date] - lower_bound))   
        if(np.sum(mask) == 0):
            print(row[on],row[right_date])
        if(np.sum(mask) == 1):
            for name in row.index:
                infotable.loc[mask, sub_table_name + "_" + name] = row[name]
        elif(np.sum(mask) > 1):
            rows = infotable.loc[mask].copy()
            rows['delta'] = np.abs(infotable.loc[mask,left_date] - row[right_date])
            rows = rows.sort_values('delta')
            for name in row.index:
                infotable.loc[rows.index[0], sub_table_name + "_" + name] = row[name]
    return infotable