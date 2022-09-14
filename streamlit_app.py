import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  #streamlit.text(fruityvice_response.json())
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.title('Menu')
streamlit.header('My Smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
my_fruit_select=streamlit.multiselect('Pick some',list(my_fruit_list.index),['Avocado','Apple']);
my_fruit_show=my_fruit_list.loc[my_fruit_select]
streamlit.dataframe(my_fruit_show)

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    #streamlit.write('The user entered ', fruit_choice)
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

def insert_row_sf(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('" + new_fruit + "')")
    streamlit.text(new_fruit)
    return "Thanks for adding " + new_fruit

#streamlit.stop()
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
    
if streamlit.button('Get Fruit List Load'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  
add_my_fruit=streamlit.text_input('What fruit would you like to add?') 
if streamlit.button('Add a Fruit to List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_fun=insert_row_sf(add_my_fruit)
  streamlit.text(back_from_fun)
