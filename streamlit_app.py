#import streamlit
#import pandas
#import requests
import snoflake.connector
from urllib.error import URLError




import streamlit

streamlit.header ('Breakfast favorites')
streamlit.text ('🥣 Omega3 & blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard- boiled Free-Range Egg')
streamlit.text('🥑Avacado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
#import requests

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#streamlit.text(fruityvice_response)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.text(fruityvice_response)

#New Section to display fruitvice api response
#streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
                                   
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)


#New Section to display fruitvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice=streamlit.text_input('what fruit would you like informtion about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
    else:
      fruityvice_response= requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.jason())
      streamlit.dataframe(fruityvice__normalized)
      expect URLERROR as e:
        streamlit.error()

# Don't run anything past here while we troubleshoot
streamlit.stop


import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list ")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
  
#Allow the end user to add a fruit to the list

import pandas
add_my_fruit = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
add_my_fruit = add_my_fruit.set_index('Fruit')

#Let's put a pick ist here so they can pick the fruit they want to include
streamlit.multiselect("Pick somefruits:",list(add_my_fruit.index))

streamlit.write ('Thanks for adding ', add_my_fruit)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


