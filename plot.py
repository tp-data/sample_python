import matplotlib.pyplot as plt
import pandas as pd

items = pd.read_csv("items.csv")
orders = pd.read_csv("orders.csv")

orders_with_items = orders.merge(items, how='left', on='item_id')

# create amount column as price * quantity
orders_with_items['amount'] = orders_with_items['price'] * orders_with_items['quantity']

# plot activity by item
orders_by_item = orders_with_items.groupby('item_name').agg({'price': 'mean', 'quantity': 'sum', 'amount': 'sum'}).reset_index()
orders_by_item

x = orders_by_item['item_name']
y = orders_by_item['amount']
plt.bar(x,y)

# plot activity by month and item (using pivot)
orders_with_items['date'] = pd.to_datetime(orders_with_items.date)
orders_with_items['month'] = orders_with_items['date'] + pd.offsets.MonthBegin(-1)
orders_by_month = orders_with_items.groupby(['month','item_name']).agg({'price': 'mean', 'quantity': 'sum', 'amount': 'sum'}).reset_index()

item_amount_by_month = orders_by_month.pivot(index='month', columns='item_name', values='amount')
item_amount_by_month.plot()
