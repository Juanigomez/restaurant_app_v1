import streamlit as st
import pandas as pd
import plotly.express as px
import requests

def search_Place(location, food):
    url = f"https://nominatim.openstreetmap.org/search?q={location}+{food}+restaurante&format=json&country=Uruguay&limit=1"
    response = requests.get(url)
    data = response.json()
    results = data
    return results

def display_Map(name, lat, lon):
    data = pd.DataFrame({'lat': [lat], 'lon': [lon], 'text': [name]})
    fig = px.scatter_mapbox(data_frame=data, lat='lat', lon='lon', text='text', zoom=15)
    fig.update_layout(mapbox_style="open-street-map")
    return fig

def homepage():
    header = st.container()
    search_Box = st.container()
    top_Results = st.container()
    with header:
        st.header("Busqueda de Restaurantes")
    with search_Box: 
        location = st.selectbox("Selecciona una ubicacion:", ["Montevideo", "Punta del Este"])
        keyword_Input, inp_Btn = st.columns([7, 1])
        with keyword_Input: 
            all_Foods = ["Empanadas", "Pizza", "Hamburguesa", "Ensaladas", "Sushi", "Comida china", "Pescado"]
            food = st.selectbox("Que quieres comer? ", all_Foods)
        with inp_Btn:
            st.text("")
            st.text("")
            submit_Food_Btn = st.button("Buscar")
    with top_Results:
        if submit_Food_Btn:
            results = search_Place(location, food)
            if not results:
                st.warning("No se encontraron resultados para tu busqueda.")
            else:
                st.write("Resultados:")
                for result in results:
                    name = result["display_name"]
                    lat = result["lat"]
                    lon = result["lon"]
                    st.write(name)
                    map = display_Map(name, lat, lon)
                    st.plotly_chart(map)

if __name__ == "__main__":
    homepage()
