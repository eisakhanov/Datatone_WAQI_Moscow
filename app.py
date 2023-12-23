import datetime as dt
import streamlit as st
import pandas as pd

from map.moscow_map import render_moscow_map
from chart.chart import render_chart


def main():
    stations_data = pd.read_csv('data/26stations.csv')

    st.title("Уровень загрязнения воздуха в городе Москва")

    st.sidebar.markdown("## Выберите станцию")

    station_select_event = st.sidebar.selectbox('Выберите станцию', stations_data['station'])

    today = dt.datetime.now()
    month_ago = today - dt.timedelta(days=30)
    three_months_ago = today - dt.timedelta(days=90)

    start_date = st.sidebar.date_input("Выберите начало временного промежутка",
                                       month_ago,
                                       three_months_ago,
                                       today,
                                       format="DD.MM.YYYY")

    end_date = st.sidebar.date_input("Выберите конец временного промежутка",
                                     today,
                                     three_months_ago,
                                     today,
                                     format="DD.MM.YYYY")

    map_tab, chart_tab = st.tabs(["🗺️ Карта", "📈 График"])

    map_tab.subheader('Карта Москвы')

    render_moscow_map(map_tab, stations_data)

    if station_select_event:
        chart_tab.subheader("График загрязнения воздуха на станции: {}".format(station_select_event))
        render_chart(chart_tab, station_select_event, start_date, end_date)


if __name__ == "__main__":
    st.set_page_config(page_title="Уровень загрязнения воздуха в городе Москва",
                       page_icon=":chart_with_upwards_trend:")

    main()
