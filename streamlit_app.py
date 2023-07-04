import streamlit
import pandas

streamlit.header('Breakfast Menu')
streamlit.text('🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('Build your own Fruit Smoothie $3.60')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's add a pick lit for the selection
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display the table on the page
streamlit.dataframe(my_fruit_list)

# streamlit.title("My stream lit app")
# streamlit.header('Breakfast Menu')
# streamlit.text('🥑🍞Omega 3 & Blueberry Oatmeal')
# streamlit.text('🥑🍞Kale, Spinach & Rocket Smoothie')
# streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')
# streamlit.header('Fruit Slush $3.60')
# streamlit.text('🥣 🥗Grean Apple')
# streamlit.text('🥣 🥗Honeydew')
# streamlit.text('🥣 🥗Lemoonade')
# streamlit.text('🥣 🥗Luchee')
# streamlit.text('🥣 🥗Passion Fruit')
# streamlit.text('🥣 🥗Thai tea')
# streamlit.header('Coffee Blast Frappes $4.45')
# streamlit.text('🍌🥭 Cappuccino')
# streamlit.text('🍌🥭 Java chip')
# streamlit.text('🍌🥭 Mocha latte')



