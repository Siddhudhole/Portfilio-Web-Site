import streamlit 
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

streamlit.set_page_config(layout='wide')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_data_scienc = load_lottieurl(url="https://lottie.host/bfda9522-c7e9-4a29-8a5e-1e7a27d3c27d/VGN73p4NeD.json")



    # Set the title of the app 

streamlit.title("My data science portfolio !")
streamlit.write("""Welcome to my data science portfolio! I'm Siddharth Dhole, a passionate data scientist with solid foundation in Machine Learning , Deep Learning ,Natural Language Processing . This Web site showcases some of my projects and contributions in the field of data science.""")

streamlit.write('----------------------------------------------------------------')


with streamlit.container():
    selected = option_menu(None, ["About Me", "Projects","Contact"], 
        icons=['person','code-slash','chat-left-text-fill'], 
        menu_icon="cast", default_index=0, orientation="horizontal")


if selected =='About Me':
    col1,col2 = streamlit.columns(2)
    with col1:
        streamlit.title("I am Siddharth Dhole")
        streamlit.write("""I am a passionate and dedicated Data Scientist with a solid foundation in statistical analysis, machine learning, and data visualization. My journey into data science has been driven by a love for problem-solving and a curiosity to uncover patterns within complex datasets.

Having completed rigorous training, including the IBM Data Analysis with Python course and ExcelR's comprehensive Data Science program, I've gained proficiency in Python, R, and key tools like Tableau and Streamlit. These experiences have equipped me with the skills to handle large datasets, perform exploratory data analysis, build predictive models, and visualize data effectively.
""")
    with col2:
        st_lottie(lottie_data_scienc)
    streamlit.write('----------------------------------------------------------------')

    with streamlit.container():
        col3,col4 = streamlit.columns(2)

        with col3:
            streamlit.subheader("""
            Education
            - Bachelor Of Technology in Artificial Intelligence
                - JD College of Engineering and Management Nagpur 
                - CGPA: 7.41 
            - Higher Secondary School Certificate 
                - Shri Datta Arts & Commerce College, Hadgaon Nanded 
                - Percentage: 52% 
            - Secondary School Certificate 
                -  Pancheshil High School,  Hadgaon Nanded 
                - Percentage: 88.80%        
    """)
            streamlit.subheader("""
            Training & Certificates
            - Certified Data Scientist
                - Certificate Provider: Excelr Solutions Pune
                - Certification Date: 20-09-2024
                - Link URL: https://drive.google.com/file/d/1nUt-Kw9m8htFjB2dc00b7ag_lYhg5Vx3/view
  """)
        with col4:
            streamlit.subheader("""
    Technical Skills
    - Programming Languages: Python, R, SQL

    - Data Manipulation and Analysis: pandas, NumPy, SciPy

    - Machine Learning: scikit-learn, TensorFlow, Keras, XGBoost

    - Deep Learning: neural networks, CNNs, RNNs using TensorFlow and Keras

    - Data Visualization: Tableau, Matplotlib, Seaborn, Plotly

    - Big Data Technologies: Spark, Hive

    - Natural Language Processing (NLP): NLTK, SpaCy,Hugging Face

    - Model Management and Experiment Tracking: MLflow, Optuna

    - Version Control: Git, GitHub , DVC , dagshub""")



        

