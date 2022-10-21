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



# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.


my_fruit_list = my_fruit_list.set_index('Fruit'),['avacado','strawberries']

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("picksome fruits:', list(my_fruit_list.index),['Avocado','strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
                                        #display the table on the page
                                        streamlit.dataframe(fruits_to_show)
