import pandas as pd

items = pd.read_csv("items.csv")
orders = pd.read_csv("orders.csv")

# create datasets for just item id columns
item_ids = items['item_id']
orders_item_ids = orders['item_id']

# create variable to store ids missing from the orders dataset
missing_ids = item_ids[~item_ids.isin(orders_item_ids)]

# grab records from items dataset where id matches missing id
items_missing = items[items['item_id'].isin(missing_ids)]