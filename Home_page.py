import streamlit as st


st.set_page_config(
    page_title="Uganda Travel Time",
    page_icon="👋",
    layout="wide")

col3, col4= st.sidebar.columns([1, 7])

with col3:
    st.write(' ')

with col4:
   st.image("Figure/earth.png",width=150)

st.sidebar.title("Contribution")
st.sidebar.info(
            """
            This web app is developed based on Streamlit URL: <https://streamlit.geemap.org>
        """
        )
st.sidebar.markdown("<a href='http://google.com.au/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/edinburgh.png?raw=true' style='width: 240px;'></a>", unsafe_allow_html=True)


st.title('Welcome to this Uganda Travel Time Spatial Datasets Visualization Platform')

tab1, tab2 = st.tabs(["Introduction","Disclaimer and Acknowledgement"])

with tab1:
    st.markdown(
    '</br><p style="font-family:sans-serif; color:#3b3a37; font-size: 32px;"><b>Introduction</b></p>',
    unsafe_allow_html=True)


    st.markdown("""
    <style>
    .link {
        font-size:17px;
        color:#093259
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('''
            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;"> 
            <a class="link", href="https://www.nature.com/articles/s41597-022-01274-w#citeas">The previous study</a>
            have developed travel time estimates for Uganda and made these available for download through the 
            <a class="link", href="https://datashare.ed.ac.uk">Edinburgh Data Share Platform</a>.
            This platform was created to display geospatial datasets with different data formats. 
            The web maps on this platform could help you have a fast navigation around the datasets without professional software. </p>
            ''', 
            unsafe_allow_html=True)

    col1, col2= st.columns([1, 7])

    with col1:
        st.write(' ')

    with col2:
        st.image("Figure/data.png", width=800)




    st.markdown('''
                <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:center; "> 
                <a class="link", href="https://www.nature.com/articles/s41597-022-01274-w#citeas">
                Travel time to any health centre in Uganda</a> </p>''',
                unsafe_allow_html=True)

    st.markdown('''
            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
            All spatial datasets have been categorized into five sections. You can easily navigate to the respective map pages using the navigation bar on the left side.</p>
            
            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
            <b>Village Distribution:</b> &nbsp; This section contains the main settlements data in Uganda.</p>

            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
            <b>Health Centres: </b> &nbsp;This section displays the distribution of health facilities at different levels.

            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
            <b>Raster Data Visualization:</b> &nbsp; 
            This section presents the 100-metre resolution maps in raster format of travel time to the nearest health facility at different levels.</p>

            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
            <b>Resolution Comparison:</b> &nbsp; This section features a comparison split map of the Uganda Travel Time to any health facility dataset. 
            The left layer shows data at 17-meter resolution, while the right layer presents data at 1000-meter resolution.</p>

            <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
            <b>Vector Data Visualization:</b> &nbsp; In this section, the travel time to the nearest health facility maps is displayed in vector format. 
            The travel time values are shown for each district of Uganda.</p>

            ''', 
            unsafe_allow_html=True)

with tab2:
    
    st.markdown(
    '</br><p style="font-family:sans-serif; color:#3b3a37; font-size: 32px;"><b>Disclaimer</b></p>',
    unsafe_allow_html=True)
     
    st.markdown('''
                <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                Any content (e.g., images, published data, domain names, etc.) displayed on the web pages of this website is the sole ownership of the original authors.</li>
                <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                All data published on this website is open-source and obtained with permission. </li>
                <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                This website is only for academic research purposes. </li>
                <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                All data sources can be accessed through the Contribution part on the disclaimer page. </li>
                ''', 
            unsafe_allow_html=True)
    
    st.markdown(
    '</br><p style="font-family:sans-serif; color:#3b3a37; font-size: 32px;"><b>Contribution</b></p>',
    unsafe_allow_html=True)
    
    st.markdown('''
                <li style="font-family:sans-serif; color:#3b3a37; font-size: 22px;">
                <b>With special thanks to: </b></li>
                ''', unsafe_allow_html=True)
    
    col5, col6, col20= st.columns([1.5,1.5,4])

    with col5:
        st.markdown("<a href='https://www.esri.com/en-us/home'><img src='https://github.com/Estherlan11/new/blob/main/Figure/ArcGIS_logo.png?raw=true' style='width: 150px;'></a>", unsafe_allow_html=True)

    with col6:
        st.markdown("<a href='https://leafmap.org/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/leafmap_logo.png?raw=true' style='width: 135px;'></a>", unsafe_allow_html=True)
    
    with col20:
        st.write(' ')
    
    col7, col8, col9, col30= st.columns([2,2,2,4])

    with col8:   
        st.markdown("<a href='https://geoserver.org/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/geoserver_logo.png?raw=true' style='width: 200px;'></a>", unsafe_allow_html=True)
    with col9:
        st.markdown("<a href='https://streamlit.io/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/streamlit.png?raw=true' style='width: 200px;'></a>", unsafe_allow_html=True)
    with col7:    
        st.markdown("<a href='https://leafletjs.com/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/Leaflet.png?raw=true' style='width: 200px;'></a>" , unsafe_allow_html=True)

    with col30:
        st.write(' ')  
    st.write(' ')

    st.markdown('''
                <li style="font-family:sans-serif; color:#3b3a37; font-size: 22px;">
                <b>All the data source are from: </b></li>
                ''', unsafe_allow_html=True)
    st.write(' ')

    col10, col11, col40= st.columns([1,1,2])
    with col10:
        st.markdown("<a href='https://datashare.ed.ac.uk'><img src='https://github.com/Estherlan11/new/blob/main/Figure/datashare.png?raw=true' style='width: 200px;'></a>", unsafe_allow_html=True)
    
    with col11: 
        st.write(' ')  
        st.markdown("<a href='https://data.humdata.org/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/hdx_new_logo_accronym.png?raw=true' style='width: 200px;'></a>", unsafe_allow_html=True)
    with col40:
        st.write(' ') 

    col12, col13, col50= st.columns([1,1,2])     
    with col12:
        st.write(' ')
        st.write(' ')
        st.markdown("<a href='https://springernature.figshare.com/ '><img src='https://github.com/Estherlan11/new/blob/main/Figure/logo%20health.png?raw=true' style='width: 160px;'></a>", unsafe_allow_html=True)
    with col13:
        st.markdown("<a href='https://gadm.org/'><img src='https://github.com/Estherlan11/new/blob/main/Figure/GAMD.png?raw=true' style='width: 120px;'></a>", unsafe_allow_html=True)

    with col50:
        st.write(' ')   
    st.write(' ')

    st.markdown(
        '</br><p style="font-family:sans-serif; color:#3b3a37; font-size: 32px;"><b>Acknowledgement</b></p>',
        unsafe_allow_html=True)

    st.markdown('''
                    <p style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                    We express our gratitude for your usage of this website. Thank you for your support and trust. </br>
                    Any concerns, questions, ideas, or criticism on this website please do not hesitate to reach out to me 
                    <a href="mailto:R.Lan-1@sms.ed.ac.uk"><img src= 'https://github.com/Estherlan11/new/blob/main/Figure/email.png?raw=true' style='width: 30px;'></a>.</br>
                    Your feedback is highly valuable to us since it allows us to continually develop and improve this website. </br>
                    Thank you for visiting our website again, and hope you have a pleasant and meaningful experience here! </p>
                    ''', 
                unsafe_allow_html=True)
        
        
