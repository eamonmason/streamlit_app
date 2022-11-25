import streamlit
import pandas

streamlit.title('First streamlit app')
streamlit.header('Gonna do something')
streamlit.text('test1')
streamlit.text('test2')
streamlit.text('test3')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
