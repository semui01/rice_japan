# import libraries
import pandas as pd
import plotly.express as px
from PIL import Image


# read csv file and display the data
df_jp_loc = pd.read_csv('n336_337-Table 1.csv')
print(df_jp_loc.head(50))


# Check if any Nan input and show the Nan columns
print(df_jp_loc.isna().values.any())
print(df_jp_loc.isna().any())

# Data Cleaning (drop the columns and rows if all na, filled other na with 0, and replace special characters  with empty space)
df_jp_clean = df_jp_loc.dropna(axis=0,how='all').dropna(axis=1,how='all').fillna(0).replace('…','').head(50)
print(df_jp_clean)


# create a new dataframe with sub dataset from the existing dataframe, replace , with '' , sort data in descending order
df_jp_new=df_jp_clean.iloc[14:][['Unnamed: 2','Unnamed: 7','Unnamed: 9','Ⅶ　Crops　337']].replace(',','',regex=True).sort_values('Unnamed: 7', ascending=False)

# Convert strings to floats
df_jp_new['Unnamed: 7'] =df_jp_new['Unnamed: 7'].astype('float')
df_jp_new['Unnamed: 9'] =df_jp_new['Unnamed: 9'].astype('float')
print(df_jp_new)

fig= px.bar(df_jp_new,x='Ⅶ　Crops　337',y='Unnamed: 7',labels={'Ⅶ　Crops　337':'prefecture','Unnamed: 7':'planted area'})
# Open the image from local path
im = Image.open('010.jpg')

## Add image as background image
fig.add_layout_image(
    dict(source= im,
            xref="paper",
            yref="paper",
            x=-0.5,
            y=4.2,
            sizex=6,
            sizey=6,
            opacity=0.2,
            )
)

fig.update_layout(font_size=15,title={'text':'Japan Rice plantation area in 2019(ha)','y':0.95,'x':0.5,'xanchor':'center','yanchor':'top'},yaxis={'categoryorder':'total ascending'},paper_bgcolor='rgb(248,248,255)',
    plot_bgcolor='rgb(248,248,255)')


#display the chart
fig.show()

# Write the chart as html file
fig.write_html('japan_rice_land.html')