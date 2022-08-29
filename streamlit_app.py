import streamlit
import pandas

streamlit.title('Menu')
streamlit.header('My Smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect('Pick some',list(my_fruit_list.index),['Avacado','Apple']);
