import streamlit
import pandas
import requests

streamlit.title('Menu')
streamlit.header('My Smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
my_fruit_select=streamlit.multiselect('Pick some',list(my_fruit_list.index),['Avocado','Apple']);
my_fruit_show=my_fruit_list.loc[my_fruit_select]
streamlit.dataframe(my_fruit_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"watermelon")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
