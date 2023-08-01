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

st.title('Welcome to this Uganda Travel Time Spatial Datasets Visualization Platform')


st.markdown(
'</br><p style="font-family:sans-serif; color:#3b3a37; font-size: 35px;"><b>Introduction</b></p>',
unsafe_allow_html=True)


st.markdown("""
<style>
.link {
    font-size:18px;
    color:#093259
}
</style>
""", unsafe_allow_html=True)

st.markdown('''
        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;"> 
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
            <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:center; "> 
            <a class="link", href="https://www.nature.com/articles/s41597-022-01274-w#citeas">
            Travel time to any health centre in Uganda</a> </p>''',
            unsafe_allow_html=True)

st.markdown('''
        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
        All spatial datasets have been categorized into five sections. You can easily navigate to the respective map pages using the navigation bar on the left side.</p>
        
        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
        <b>Village Distribution:</b> &nbsp; This section contains the main settlements data in Uganda.</p>

        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
        <b>Health Centres: </b> &nbsp;This section displays the distribution of health facilities at different levels.

        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
        <b>Raster Data Visualization:</b> &nbsp; 
        This section presents the 100-metre resolution maps in raster format of travel time to the nearest health facility at different levels.</p>

        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
        <b>Resolution Comparison:</b> &nbsp; This section features a comparison split map of the Uganda Travel Time to any health facility dataset. 
        The left layer shows data at 18-meter resolution, while the right layer presents data at 1000-meter resolution.</p>

        <p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
        <b>Vector Data Visualization:</b> &nbsp; In this section, the travel time to the nearest health facility maps is displayed in vector format. 
        The travel time values are shown for each district of Uganda.</p>

        ''', 
        unsafe_allow_html=True)
