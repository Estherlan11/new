import streamlit as st


st.set_page_config(
    page_title="Uganda Travel Time",
    page_icon="👋",
    layout="centered")

st.sidebar.image("Figure/earth.jpg")

st.sidebar.title("Contribution")
st.sidebar.info(
            """
            This web app is developed based on Streamlit URL: <https://streamlit.geemap.org>
        """
        )

st.title('Welcome to this Uganda Travel Time Spatial Datasets Visualization Platform')


st.markdown(
'<p style="font-family:sans-serif; color:#000205; font-size: 60px;"><b>Introduction</b></p>',
unsafe_allow_html=True)

url1 = 'https://www.nature.com/articles/s41597-022-01274-w#citeas'
url2 = 'https://datashare.ed.ac.uk'

st.markdown("""
<style>
.link {
    font-size:40px;
    color:#0547ab
}
</style>
""", unsafe_allow_html=True)

st.markdown('''
        <p style="font-family:sans-serif; color:#000205; font-size: 40px;"> 
        <a class="link", href="url1">The previous study</a>
        have developed travel time estimates for Uganda and made these available for download through the 
        <a class="link", href="url2">Edinburgh Data Share Platform</a>.
        This platform was created to display geospatial datasets with different data formats. 
        The web maps on this platform could help you have a fast navigation around the datasets without professional software. </p>
        ''', 
        unsafe_allow_html=True)


st.image("Figure/data.png")
st.markdown('''<a class="link", href="url1">Travel time to any health centre in Uganda</a>''')

st.markdown('''
        <p style="font-family:sans-serif; color:#000205; font-size: 40px;">
        All spatial datasets have been categorized into five sections. You can easily navigate to the respective map pages using the navigation bar on the left side.</p>
        
        <p style="font-family:sans-serif; color:#000205; font-size: 40px;">
        <b>Village Distribution:</b> &nbsp; This section contains the main settlements data in Uganda.</p>

        <p style="font-family:sans-serif; color:#000205; font-size: 40px;">
        <b>Health Centres: </b> &nbsp;This section displays the distribution of health facilities at different levels.

        <p style="font-family:sans-serif; color:#000205; font-size: 40px;">
        <b>Raster Data Visualization:</b> &nbsp; 
        This section presents the 100-metre resolution maps in raster format of travel time to the nearest health facility at different levels.</p>

        <p style="font-family:sans-serif; color:#000205; font-size: 40px;">
        <b>Resolution Comparison:</b> &nbsp; This section features a comparison split map of the Uganda Travel Time to any health facility dataset. 
        The left layer shows data at 20-meter resolution, while the right layer presents data at 1000-meter resolution.</p>

        <p style="font-family:sans-serif; color:#000205; font-size: 40px;">
        <b>Vector Data Visualization:</b> &nbsp; In this section, the travel time to the nearest health facility maps are displayed in vector format. 
        The travel time values are shown for each district of Uganda.</p>

        ''', 
        unsafe_allow_html=True)
