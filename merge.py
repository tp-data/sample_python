import pandas as pd
import tabulate

items = pd.read_csv("items.csv")
orders = pd.read_csv("orders.csv")

orders_with_items = orders.merge(items, how='left', on='item_id')
