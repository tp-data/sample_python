# Sample Python / Jupyter Functionality

> This repository contains a mix of procedures that can be performed in python for simple analytics and operational workflows. These files and processes are designed to be moves to Jupyter for a more modular use case.
> The key areas of this respository consist of merging, isolating mismatching values, plotting, and query with dynamic inputs.

## Context
For these examples, we are utilizing two sample datasets. One of the examples is orders, and the other items. Below is a previe
* [items.csv](items.csv)
```
item_id,item_name
1,AAA
2,BBB
3,CCC
```
* [orders.csv](orders.csv)
```
order_id,item_id,date,price,quantity
1,1,2/3/21,10,5
2,2,2/3/21,20,10
3,3,2/3/21,30,15
```
### Merge
This code displays the two sample files, order and items, being joined together so that data from both tables can be visualized in a single dataframe. In this example, we take the orders data, and perform a left join so that the 'name' from the items data displays to the cordinating item_id in the orders data.See below for the line of code that executes the merge into a new dataframe:
```
orders_with_items = orders.merge(items, how='left', on='item_id')
```
### Mismatching Values
This section can be useful for comparing two like files to find a missing value. This can be done by isolating a unique column that matches between both datasets. In the sample files, we utilize the item_id to check which items are not present in the order data. After isolating the item_id value from both datasets into two dataframes, we run the following code to find missing ids in the items data: 
```
missing_ids = item_ids[~item_ids.isin(orders_item_ids)]

```
### Plot
In this section, we utilize the orders data to create two plots. For one plot, we focus on graphing activity over time. After merging both items and orders, we truncate the date field to group by month:
```
orders_with_items['month'] = orders_with_items['date'] + pd.offsets.MonthBegin(-1)

```
Next, we group by month and item, to perform the desired aggregations:
```
orders_by_month = orders_with_items.groupby(['month','item_name']).agg({'price': 'mean', 'quantity': 'sum', 'amount': 'sum'}).reset_index()

```
Using the grouped dataset, we can pivot by item to display a line graph with a line per item:
```
item_amount_by_month = orders_by_month.pivot(index='month', columns='item_name', values='amount')
item_amount_by_month.plot()
```
### Query
```
```
