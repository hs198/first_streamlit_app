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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.text(fruityvice_response)

#New Section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
                                   
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list ")
my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
  
Allow the end user to add a fruit to the list

import pandas
add_my_fruit = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(add_my_fruit)




