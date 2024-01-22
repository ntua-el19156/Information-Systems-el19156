import matplotlib.pyplot as plt
import pandas as pd

# Load data from different sheets into pandas DataFrames
df1 = pd.read_excel('full.xlsx', sheet_name='Quest time')
df2 = pd.read_excel('full.xlsx', sheet_name='Influx time')

# Combine the DataFrames based on the common columns
#combined_df = pd.concat([df1['single-groupby-1-1-1'], df1['single-groupby-1-1-12'], df2['single-groupby-1-1-1'], df2['single-groupby-1-1-12']], axis=1)

# Choose the columns you want to compare
column_to_compare = ['single-groupby-1-1-1', 'single-groupby-1-1-12',
                     'single-groupby-1-8-1', 'single-groupby-5-1-1',
                     'single-groupby-5-1-12', 'single-groupby-5-8-1',
                     'double-groupby-1', 'double-groupby-5',
                     'double-groupby-all', 'high-cpu-all',
                     'high-cpu-1', 'lastpoint',
                     'groupby-orderby-limit']

selected_rows = [0, 3, 6, 9, 12]
speedup_rows = [17,18,19,20]
bar_width = 0.3

# Set position of bar on X axis 
br1 = [1,2,3,4,5]
br2 = [x + bar_width for x in br1]

# Set position of bar on X axis for speedup chart
br1_s = [2,3,4,5]
br2_s = [x + bar_width for x in br1_s]

# To properly place the annotations
bit_right = 0.12
bit_down = 0.15

# Color of each db
influx_col = "#0096FF"
quest_col = "#D14671"

#for i in range(13):
for i in range(13):
    plt.figure(2*i)
    #plt.bar([1,2,3,4,5],df1.loc[selected_rows, column_to_compare[i]], label='Quest')
    plt.barh(br1,df1.loc[selected_rows, column_to_compare[i]],height=bar_width, color=quest_col, label='Quest')

    # Plot data from the second sheet
    plt.barh(br2,df2.loc[selected_rows, column_to_compare[i]],height=bar_width, color=influx_col, label='Influx')

    # Add precise numbers at the end of each bar
    for index, value in enumerate(df1.loc[selected_rows, column_to_compare[i]]):
        print(index, value)
        plt.text(value + bit_right, br1[index] + bar_width / 2 - bit_down, str(value), ha='left', va='center')

    for index, value in enumerate(df2.loc[selected_rows, column_to_compare[i]]):
        plt.text(value + bit_right, br2[index] + bar_width / 2 - bit_down, str(value), ha='left', va='center')

    # Add labels and title
    plt.ylabel('Number of workers')
    plt.xlabel('Time for 300 queries (s)')
    plt.title(f'{column_to_compare[i]}')

    # Add legend
    plt.legend()
    plt.legend(reverse=True)

    # Show the plot
    plt.show()

    # Speedup chart
    plt.figure(2*i + 1)
    
    plt.barh(br1_s,df1.loc[speedup_rows, column_to_compare[i]], height=bar_width, color=quest_col, label='Quest')
    plt.barh(br2_s,df2.loc[speedup_rows, column_to_compare[i]], height=bar_width, color=influx_col, label='Influx')
    plt.yticks(range(1,6))

    # Add precise numbers at the end of each bar
    for index, value in enumerate(df1.loc[speedup_rows, column_to_compare[i]]):
        print(index, value)
        plt.text(value + bit_right/5, br1[index] + bar_width / 2 - bit_down + 1, str(value)[:5], ha='left', va='center')

    for index, value in enumerate(df2.loc[speedup_rows, column_to_compare[i]]):
        plt.text(value + bit_right/5, br2[index] + bar_width / 2 - bit_down + 1, str(value)[:5], ha='left', va='center')

    plt.ylabel('Number of workers')
    plt.xlabel('Speedup')
    plt.title(f'{column_to_compare[i]} speedup')
    plt.legend()
    plt.legend(reverse=True)
    plt.show()
