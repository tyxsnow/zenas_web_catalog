import streamlit
import snowflake.connector

streamlit.title('Zenas Test')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),
CURRENT_REGION()")




