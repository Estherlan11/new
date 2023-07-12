import streamlit as st
from streamlit_option_menu import option_menu
from pages import healthcenters, raster, settlements # import your app modules here

# Call set_page_config() as the first Streamlit command
st.set_page_config(page_title="Uganda travel time", layout="wide")

# Rest of your Streamlit app code goes here
# ...

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = {
    "settlements": {"title": "Settlements", "icon": "people"},
    #"polygon": {"title": "Travel Time Vector", "icon": "bounding-box"},
    "raster": {"title": "Travel Time Raster", "icon": "box-fill"},
    "health_centers": {"title": "Health Centers Distribution", "icon": "hospital"},
    #"split": {"title": "Travel Time Raster Comparison", "icon": "map"},
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
     selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

     st.sidebar.title("About")
     st.sidebar.info(
         """
         Just a test
        
         """
     )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
