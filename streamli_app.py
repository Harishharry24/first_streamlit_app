import streamlit

streamlit.title('Harish had dinner')

streamlit.title( 'chapathi with ghee and peas')

streamlit.text('hey how are you')

streamlit.header('harish will get job in Amazon')

streamlit.header('🥣 🥗 🐔 🥑🍞Breakfast Menu🥣 🥗 🐔 🥑🍞')
streamlit.text('🥣 🥗 🐔 🥑🍞🥣 🥗 🐔 🥑🍞🥣 🥗 🐔 🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 🥗 🐔 🥑🍞🥣 🥗 🐔 🥑🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🥣 🥗 🐔 🥑🍞Hard-Boiled Free-Range Egg🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#new section to display fruityvise response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)  #adda text entry box and send input to fruity vice as part of api call

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 


#streamlit.text(fruityvice_response.json()) #just writes data to the screen

# takes the json of the  response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output it as a screen of the table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
