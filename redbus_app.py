import streamlit as st
import pandas as pd
import mysql.connector
from streamlit_option_menu import option_menu
import time

lists_k=[]
df_k=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Kerala.csv")
lists_k = df_k["Route_name"].tolist()


#Andhra bus
lists_A=[]
df_A=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/AP.csv")
lists_A = df_A["Route_name"]

#Rajasthan
lists_RJ=[]
df_RJ=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Rajasthan.csv")
lists_RJ = df_RJ["Route_name"].tolist()


#Telungana bus
lists_T=[]
df_T=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Telugana.csv")
lists_T = df_T["Route_name"].tolist()


#Himachal bus
lists_H=[]
df_H=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Himachal.csv")
lists_H = df_H["Route_name"].tolist()


#Chandigarh bus
lists_CR=[]
df_CR=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Chandigarh.csv")
lists_CR = df_CR["Route_name"].tolist()



#UP bus 
lists_UP=[]
df_UP=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/UP.csv")
lists_UP = df_UP["Route_name"].tolist()


#Kadamba bus
lists_KD=[]
df_KD=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Goa.csv")
lists_kD = df_KD["Route_name"].tolist()


#Jammu and Kashmir bus
lists_JK=[]
df_JK=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Jammu.csv")
lists_JK = df_JK["Route_name"].tolist()

#Assam bus
lists_AS=[]
df_AS=pd.read_csv(r"C:/Users/sinwa/projects/RED_BUS_project/csv_files/Assam.csv")
lists_AS = df_AS["Route_name"].tolist()

#st.title("KSD TRAVEL PARTNER",)
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("<h1 class='centered-title'>TRUSTLINE TRAVEL PARTNER </h1>", unsafe_allow_html=True)
st.markdown("<h2 class='centered-title'>ESCAPE THE ORDINARY </h2>", unsafe_allow_html=True)

web=option_menu(menu_title="Ready to Get Started?",
                options=["ABOUT","FIND YOUR BUS"],
                icons=["info-circle",":directions_bus:"],
                orientation="horizontal")
if web=="ABOUT":
    
    st.title("Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader(":red[Domain:]  Transportation")               
    
    st.subheader(":red[Objective:] ")
    st.markdown(''"The 'Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    st.subheader(":red[Overview:]") 
    st.markdown("Selenium: Selenium is a tool used for automating web pages. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, clicking buttons, to collect the desired data...")
    st.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    st.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    st.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    st.subheader(":red[Skill-take:]")
    st.markdown("Selenium, Python, Pandas, MySQL,  Streamlit.")
    st.subheader(":red[Developed-by:]  Sinwan_Siraj")   
if web == "FIND YOUR BUS":
    S = st.selectbox("Lists of States", ["Kerala", "Adhra Pradesh", "Rajasthan", "Telungana", "Himachal" , "Kadamba", 
                                           "Chandigarh", "Jammu and kashmir", "Uttar Pradesh", "Assam"])
    
    col1,col2=st.columns(2)
    with col1:
        select_type = st.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = st.radio("Choose bus fare range", ("50-500", "500-1000", "1000 and above"))
    TIME=st.time_input("select the time")
    
    if S == "Kerala":
        K = st.selectbox("List of routes",lists_k)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  
 # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}" AND {bus_type_condition}
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        st.dataframe(df_result)
    if S=="Adhra Pradesh":
        A=st.selectbox("list of routes",lists_A)

        def type_and_fare_A(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_A(select_type, select_fare)
        st.dataframe(df_result)
          

    # Gujarat bus fare filtering
    if S=="Rajasthan":
        RJ=st.selectbox("list of routes",lists_RJ)

        def type_and_fare_RJ(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{RJ}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_RJ(select_type, select_fare)
        st.dataframe(df_result)

    # Telungana bus fare filtering
    if S=="Telungana":
        T=st.selectbox("list of routes",lists_T)

        def type_and_fare_T(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_type, select_fare)
        st.dataframe(df_result)

    # Himachal bus fare filtering
    if S=="Himachal":
        H=st.selectbox("list of routes",lists_H)

        def type_and_fare_H(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_H(select_type, select_fare)
        st.dataframe(df_result)
          

    # Kadamba bus fare filtering       
    if S=="Kadamba":
        KD=st.selectbox("list of routes",lists_KD)

        def type_and_fare_KD(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{KD}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_KD(select_type, select_fare)
        st.dataframe(df_result)
  


    # Chandigarh bus fare filtering
    if S=="Chandigarh":
        CR=st.selectbox("list of rotes",lists_CR)

        def type_and_fare_CR(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{CR}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_CR(select_type, select_fare)
        st.dataframe(df_result)

    # Jammu and kashmir fare filtering
    if S=="Jammu and kashmir":
        JK=st.selectbox("list of rotes",lists_JK)

        def type_and_fare_JK(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{JK}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_JK(select_type, select_fare)
        st.dataframe(df_result)

    # Uttar pradesh bus fare filtering
    if S=="Uttar pradesh":
        UP=st.selectbox("list of rotes",lists_UP)

        def type_and_fare_UP(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  


            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{UP}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_UP(select_type, select_fare)
        st.dataframe(df_result)

    # Assam bus fare filtering
    if S=="Assam":
        AS=st.selectbox("list of rotes",lists_AS)

        def type_and_fare_AS(bus_type, fare_range):
            conn = mysql.connector.connect(host='localhost', user='root', password='Saran@12',database = "RED_BUS")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-500":
                fare_min, fare_max = 50, 500
            elif fare_range == "500-1000":
                fare_min, fare_max = 500, 1000
            else:
                fare_min, fare_max = 1000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
        df_result = type_and_fare_AS(select_type, select_fare)
        st.dataframe(df_result)
print("filtered_buses")
st.write("Streamlit app loaded")
