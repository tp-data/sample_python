import pandas as pd

items = pd.read_csv("items.csv")
orders = pd.read_csv("orders.csv")
query_info = pd.read_csv("filter_info.csv")

orders_with_items = orders.merge(items, how='left', on='item_id')
orders_with_items['amount'] = orders_with_items['price'] * orders_with_items['quantity']

orders_with_items['date'] = pd.to_datetime(orders_with_items.date)
query_info['start'] = pd.to_datetime(query_info.start)
query_info['end'] = pd.to_datetime(query_info.end)

output = []

for i in range(0,query_info.shape[0]):
    item_id = query_info.iloc[i][0]
    start = query_info.iloc[i][1]
    end = query_info.iloc[i][2]
    temp_orders_with_items = orders_with_items[
        (orders_with_items['item_id'] == item_id) 
        & (orders_with_items['date'] >= start) 
        & (orders_with_items['date'] <= end) 
    ]    
    temp_orders_with_items = temp_orders_with_items.groupby(['item_id','item_name'])['amount'].sum().reset_index()
    temp_output = pd.DataFrame(temp_orders_with_items)
    output.append(temp_output)
    print('Data for '+str(item_id)+' recorded.')
all_output = pd.concat(output)
