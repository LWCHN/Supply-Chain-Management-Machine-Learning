
## 1. Data Cleaning
## Import the relevant libraries

import warnings; warnings.simplefilter('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import my_helper_functions as mhf
import pandas_profiling as prof
##conda install -c anaconda pandas-profiling
##conda instll xlrd
## conda install -c anaconda openpyxl
import missingno as msno


##解决办法：安装旧版本pip install xlrd==1.2.0
## pandas 0.20.3


ct_df = pd.read_csv("./Data/Source/country_code_to_continent_map.csv")
CONTINENT_DICT = {x:y for x,y in zip(ct_df.country,ct_df.continent)}



##Load the data files
# Data Source: https://data.pepfar.net/additionalData, downloaded as excel file
full = pd.ExcelFile('./Data/Source/SCMS Data 20151023.xlsx')#,engine='openpyxl')
#full = pd.read_excel('./Data/Source/SCMS Data 20151023.xlsx')
##原因：xlrd更新到了2.0.1版本，只支持.xls文件，不支持.xlsx。解决办法：安装旧版本pip install xlrd==1.2.0.
print("Sheetnames: ",full.sheet_names)
parsed_data = mhf.parse_raw_data(full)
for df in parsed_data:
    print(df.name," shape:",df.shape )

# View ref top rows
summary, purpose, ref, data = parsed_data
data.head(3)


#Check Duplicates
data.duplicated().sum()


# Rename the columns
newcol_list = ['id', 'proj_code', 'pq_no', 'po_no', 'ship_no', 'country'
     , 'mngr', 'fulfill_via','vendor_terms', 'ship_mode', 'pq_date'
     , 'po_date', 'del_date_scheduled' ,'del_date_client', 'del_date_recorded'
     , 'prod_grp', 'sub_class', 'vendor', 'itm_desc', 'molecule_test', 'brand'
     , 'dosage','dosage_form', 'units', 'ln_itm_qty', 'ln_itm_val', 'pk_price'
     , 'unit_price', 'factory', 'first_line', 'weight', 'freight_cost', 'line_itm_ins']
data = mhf.rename_data_columns(data, newcol_list)


# Update Data Reference Dictionary
# Add these new columns to reference and make a lookup function in case we forget what it means
ref['NewColumn']= data.columns 
#ref.to_excel("Reference.xlsx") # save to disk
# Example usage of the reference function below:
mhf.getReferenceInfo(data, data.columns[5], ref)


#Convert columns data types
# First use helper function to get column report and blocks of data by column type
blocks = mhf.get_blocks_by_dtype(data)
##https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.as_blocks.html##
##Deprecated since version 0.21.0.
## need conda install pandas=0.20.3








# ######## wang liang ########
# full.sheet_names

# full.parse('Data Dictionary')
# full.parse('SCMS Delivery History Dataset')
# ######## wang liang ########