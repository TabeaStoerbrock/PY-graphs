import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import plotly.express as px
import plotly.io as pio

file_path = 'data.csv'
df = pd.read_csv(file_path)
print("Length of the DataFrame:", len(df))

#Update changes to csv
new_file_path = 'DataUpdated.csv'

##update data and reload
df.to_csv(new_file_path, index=False)
#following formats are supported for export: png, jpg (or jpeg), webp, svg, pdf

df = pd.read_csv(file_path)

# Filter out initiatives with zero values in April and either May or June
df_zero_values = df[(df['Apr'] == 0) & (df['Mai'] == 0) & (df['Jun'] == 0)]
df_non_zero_values = df[(df['Apr'] != 0) | (df['Mai'] != 0) | (df['Jun'] != 0)]
df = pd.concat([df_non_zero_values, df_zero_values])

df['Total_Value'] = df[['Apr', 'Mai', 'Jun']].sum(axis=1)

df_NotPlanned = df[
    ((df['Apr'] == 0) & ((df['Mai'] == 0) | (df['Jun'] == 0)))
]
# Update filtered initiatives to grey
df_NotPlanned['Color'] = 'Not Planned'

# Update  Gantt chart to include initiatives with zero values in grey
fig = px.timeline(df, x_start='Start', x_end='End', y='topics', title='Initiatives Gantt Chart',
                  labels={'topics': 'Initiativen'})

df['Month'] = pd.to_datetime(df['Start']).dt.strftime('%B')


###LAYOUT GANTT #######
fig.update_layout(yaxis=dict(tickmode='array', tickvals=df['topics'], ticktext=df['topics']),
                  height=400)


fig = px.timeline(df, x_start='Start', x_end='End', y='topics', title='Roadmap Q2',
                  labels={'topics': 'Initiative'}, color='priority',
                   color_discrete_map={1: 'rgb(0, 0, 255)', 3: 'rgb(255, 0, 0)'}, hover_name='topics',
                  hover_data=['Start', 'End', 'priority', 'Total_Value'],
                  )

# Export the Gantt 
pio.write_image(fig, 'gantt_chart.pdf', format='pdf')

# Show the Gantt chart
fig.update_yaxes(categoryorder='total ascending')
fig.show()

# Export the Gantt 
pio.write_html(fig, 'roadmap.html')
pio.write_image(fig, 'roadmap.pdf', format='pdf')


# df_NotPlanned.plot(kind='line', x='x_column', y='y_column', color='grey', ax=plt.gca())

###Filter Themenbereiche intern
#df = df[~df['Initiatives'].isin(['IT-Security', 'TiM (Telefonie im Markt)','Group Product / NEO', 'Meetings','Multi Channel Contact Center', 'Telefonie Verwaltung','Smarter Work im Markt', 'Sonstiges (produktfremd)', 'Sonstiges (ohne Feature Aufnahme)', 'Spitzensupport', 'Produktoptimierung CM', 'technische Schulden'])]

    ####  TOP 3 PER MONTH ####

# # Find the top three most dense initiatives for each month
# most_dense_per_month = df[['Initiatives', 'Apr', 'Mai', 'Jun']].nlargest(3, ['Apr', 'Mai', 'Jun'])
# top_three_initiatives = most_dense_per_month['Initiatives'].tolist()
# df_filtered_top_three = df_filtered[df_filtered['Initiatives'].isin(top_three_initiatives)]
# palette = sns.light_palette("blue", n_colors=len(df_filtered_top_three['Initiatives']))

# # Plot
# plt.figure(figsize=(12, 6))  
# ax = sns.barplot(data=df_filtered_top_three.melt(id_vars='Initiatives', var_name='Month', value_name='Density'),
#                  x='Month', y='Density', hue='Initiatives', palette='husl')


# plt.xlabel('Monat', fontname='Calibri Light') 
# plt.ylabel('PTs', fontname='Calibri Light')   
# plt.title('Meiste PT pro Monat', fontname='Calibri Light') 

# # Move legend to the right side of the plot
# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Initiativen', title_fontsize='Calibri Light')

# plt.xticks(fontname='Calibri Light') 
# plt.yticks(fontname='Calibri Light')  
# plt.show()


df['Total_Weight'] = df[['Apr', 'Mai', 'Jun']].sum(axis=1)


######### SIMPLETON PLOT ##################
## Simple barplot, blues coloring

## I am important #
#df_sorted = df.sort_values(by='Total_Weight', ascending=False)

#plt.figure(figsize=(12, 6))
#sns.barplot(data=df_sorted, x='Total_Weight', y='Initiatives', palette='Blues_r')

#####################################################

########## ALL IN ONE && ONE FOR ALL #######################
# # Plot
# plt.figure(figsize=(20, 15))  
# ax = sns.barplot(data=df_filtered.melt(id_vars='Initiatives', var_name='Month', value_name='Density'),
#                  x='Month', y='Density', hue='Initiatives', palette='husl')

# plt.xlabel('Monat', fontname='Calibri Light')
# plt.ylabel('PTs', fontname='Calibri Light')
# plt.title('Meiste PT pro Monat', fontname='Calibri Light')
# # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Initiativen', title_fontsize='Calibri Light', legend=False)
# plt.xticks(fontname='Calibri Light')  
# plt.yticks(fontname='Calibri Light') 
# plt.show()

# # copy DataFrame
# df_copy2 = df.copy()
# print(df_copy2.columns)
# # Convert 'closed' columns to indicate closed status
# for col in ['closed_Apr', 'closed_Mai', 'closed_June']:
#     df_copy2[col] = df_copy2[col].astype(bool)

# # Plotting the Gantt chart
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plotting bars for each month
# for i, row in df_copy2.iterrows():
#     for month in ['Apr', 'Mai', 'Jun']:
#         color = 'green' if not row[f'closed_{month}'] else 'red'
#         ax.barh(row['Team/Thema/Initiative'], 1, left=i, color=color, alpha=0.6)

# # Formatting
# ax.set_xlabel('Months')
# ax.set_ylabel('Topics')
# ax.set_title('Topic Closure Roadmap')
# ax.set_yticks(range(len(df_copy2)))
# ax.set_yticklabels(df_copy2['Team/Thema/Initiative'])
# ax.invert_yaxis()  # Invert y-axis to have the first topic at the top

# # Adding legend
# ax.legend(['Open', 'Closed'], loc='upper left')

# # Show plot
# plt.tight_layout()
# plt.show()

###### closed initatives per month ##########

# closed_initiatives = df.copy()

# # Filtern der Themen mit Null-Werten ab einem bestimmten Monat
# closed_initiatives['Closed_Apr'] = (closed_initiatives['Apr'] == 0) | (closed_initiatives['Apr'] != 0)  & (closed_initiatives['Mai'] == 0) & (closed_initiatives['Jun'] == 0)
# closed_initiatives['Closed_Mai'] = (closed_initiatives['Mai'] == 0) | (closed_initiatives['Mai'] != 0) & (closed_initiatives['Jun'] == 0)
# closed_initiatives['Closed_Jun'] = (closed_initiatives['Jun'] == 0)
# # Zählen der Anzahl der geschlossenen Themen pro Monat
# closed_counts_per_month = closed_initiatives[['Closed_Apr', 'Closed_Mai', 'Closed_Jun']].sum()
# anzahl_closed_initiatives = len(closed_initiatives)

# # Filtern der geschlossenen Initiativen nach Themen in der topics-Liste
# closed_topics_per_month = closed_initiatives[closed_initiatives['Initiatives'].isin(topics)][['Initiatives', 'Closed_Apr', 'Closed_Mai', 'Closed_Jun']]

# # Konvertieren der Daten in ein geeignetes Format für die Heatmap
# closed_topics_per_month.set_index('Initiatives', inplace=True)

# # Erstellen der Heatmap
# plt.figure(figsize=(10, 10))
# sns.heatmap(closed_topics_per_month, cmap='Blues', annot=True, fmt='d')

# # Anpassen der Achsenbeschriftungen und Titel
# plt.xlabel('Monat')
# plt.ylabel('Initiativen')
# plt.title('Geschlossene Initiativen pro Monat')

# # Anzeigen des Plots
# plt.show()



# # Plot all closed per month
# plt.figure(figsize=(10, 6))
# closed_counts_per_month.plot(kind='bar', color='blue')
# plt.xlabel('Monat')
# plt.ylabel('Anzahl geschlossener Themen')
# plt.title('Geschlossene Themen pro Monat')
# plt.grid(axis='y')
# plt.xticks(rotation=0)
# plt.show()
