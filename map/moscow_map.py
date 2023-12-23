import streamlit as st
import pydeck as pdk
import pandas as pd


def render_moscow_map(tab: st._DeltaGenerator, stations: pd.DataFrame):
    # Координаты Москвы
    moscow_latitude = 55.751244
    moscow_longitude = 37.618423

    view_state = pdk.ViewState(latitude=moscow_latitude, longitude=moscow_longitude, zoom=10, bearing=0, pitch=0)

    deck = pdk.Deck(map_style='mapbox://styles/mapbox/streets-v12',
                    initial_view_state=view_state,
                    layers=[
                        pdk.Layer('ScatterplotLayer',
                                  data=stations,
                                  pickable=True,
                                  get_position='[longitude, latitude]',
                                  get_fill_color=[255, 140, 0],
                                  get_line_color=[0, 0, 0],
                                  get_radius=25,
                                  opacity=0.8,
                                  stroked=True,
                                  filled=True,
                                  radius_scale=6,
                                  radius_min_pixels=1,
                                  radius_max_pixels=100,
                                  line_width_min_pixels=1),
                        ],
                    tooltip={'text': 'Название станции: {station}\nШирота: {latitude}\nДолгота: {longitude}'})

    tab.pydeck_chart(deck)
    