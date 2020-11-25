#!/usr/bin/env python
import os
import sys
import json
import pandas as pd
from IPython.display import display


sys.path.insert(0, 'src/data')
from Loading_Data import load_data


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'.

    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        # make the data target
#         battery_query = data_cfg['battery_query']
#         process_query = data_cfg['process_query']
        cp2_query = data_cfg['cp2_query']
        battery_information = load_data(cp2_query)
        display(battery_information)
#         return battery_information

    if 'analysis' in targets:
        ## Data Preprocessing Part
        def show_original(x):
            return x

        try:
            battery_information
        except:
            battery_information = pd.read_csv('./src/data/battery_use_data.csv')

        table = pd.pivot_table(battery_information, values='VALUE', columns=['INPUT_DESCRIPTION'],
                            index=['MEASUREMENT_TIME'], aggfunc=show_original)

        with open('config/inputs.json') as fh:
             input_cfg = json.load(fh)
         # make the data target
        battery_tag = input_cfg['tag']
        battery1 = input_cfg['battery1']
        battery2 = input_cfg['battery2']

        table[battery_tag] = table[battery_tag].fillna(method = 'ffill')
        display(table)
        ## Data Exploration Part
        print('----------Battery Tag 4------------------')
        display(table.loc[table[battery_tag] == battery1].nunique())
        print('----------Battery Tag 5------------------')
        display(table.loc[table[battery_tag] == battery2].nunique())

    if 'test' in targets:
        def show_original(x):
            return x

        try:
            battery_information
        except:
            battery_information = pd.read_csv('./test/testdata/battery_use_data.csv')

        table = pd.pivot_table(battery_information, values='VALUE', columns=['INPUT_DESCRIPTION'],
                            index=['MEASUREMENT_TIME'], aggfunc=show_original)

        with open('config/inputs.json') as fh:
             input_cfg = json.load(fh)
         # make the data target
        battery_tag = input_cfg['tag']
        battery1 = input_cfg['battery1']
        battery2 = input_cfg['battery2']

        table[battery_tag] = table[battery_tag].fillna(method = 'ffill')
        display(table)
        ## Data Exploration Part
        print('----------Battery Tag 4------------------')
        display(table.loc[table[battery_tag] == battery1].nunique())
        print('----------Battery Tag 5------------------')
        display(table.loc[table[battery_tag] == battery2].nunique())
#         print(">>>>>>>>>>>>> Start Analyzing Data <<<<<<<<<<<<<<<")
#         print('------------- Battery Data -------------------')
#         battery_info = load_data(battery_query)
#         display(battery_info)

#         print('------------- Process Data -------------------')
#         process_info = load_data(process_query)
#         display(process_info)

#         with open('config/inputs.json') as fh:
#             input_cfg = json.load(fh)
#         # make the data target
#         measurement_time = input_cfg['input_1']
#         estimated_remaining_time = input_cfg['input_2']
#         number_of_exEfiles = input_cfg['input_3']

#         battery_info[measurement_time] = pd.to_datetime(battery_info[measurement_time]).apply(lambda x: x.strftime("%Y-%m-%d %H:%M"))
#         process_info[measurement_time] = pd.to_datetime(process_info[measurement_time]).apply(lambda x: x.strftime("%Y-%m-%d %H:%M"))
#         a = battery_info.groupby(measurement_time)[estimated_remaining_time].mean().to_frame()
#         b = process_info.groupby(measurement_time)[number_of_exEfiles].sum().to_frame()
#         c=a.merge(b, on = measurement_time, how = 'inner').sort_values(by = number_of_exEfiles, ascending = False)
#         data = pd.DataFrame(c.groupby(number_of_exEfiles)[estimated_remaining_time].mean())
#         print('---------------Combined Battery and Process Data----------------')
#         display(data)
#         print(">>>>>>>>>>>>>>>>>>>>>>> End Analyzing Data <<<<<<<<<<<<<<<<<<<")



if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
