# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

import socket

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ecommerce_transactions = dataiku.Dataset("ecommerce_transactions")
df = ecommerce_transactions.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

df_merchants = pd.DataFrame(data = {'MerchantURL' : df['MerchantURL'].unique()})

df_merchants['MerchantIP'] = df_merchants['MerchantURL'].apply(socket.gethostbyname)

df = df.merge(df_merchants, on=['MerchantURL'])

# # -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# ecommerce_transactions_with_ip_df = ecommerce_transactions_df # For this sample code, simply copy input to output


# Write recipe outputs
ecommerce_transactions_with_ip = dataiku.Dataset("ecommerce_transactions_with_ip")
ecommerce_transactions_with_ip.write_with_schema(df)