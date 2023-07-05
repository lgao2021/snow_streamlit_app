import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('TeaStories New Healthy menu')

# favorite items
streamlit.header('Breakfast Favorites')
streamlit.text('🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

# select from a drop down list
streamlit.header('Build your own Fruit Smoothie $3.60')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's add a pick lit for the selection
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
# display the table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  # normalize fruityvice response
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
# add fruityvice line item
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information")
  else:
      streamlit.write('The User entered', fruit_choice)
      fruityvice_normalized = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()

streamlit.stop()


# add snowfalke connection to retrive data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
# my_cur.execute("select current_user(), current_account(), current_region()")
my_data_raw = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_raw)

#add another fruit selection box
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('The User entered', add_my_fruit)
streamlit.text('thanks for adding ' +  add_my_fruit)

# insert new roaw
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')");



