import streamlit as st
import pandas as pd
import numpy as np


def render_chart(tab: st._DeltaGenerator, station_index, start_time, end_time):
    chart_data = pd.read_csv('data/сухаревка,-москва, москва, россия-air-quality.csv')
    chart_data = chart_data.rename(columns=lambda x: x.strip())
    chart_data = chart_data.replace(r'^\s*$', np.nan, regex=True)
    chart_data['date'] = pd.to_datetime(chart_data['date'])

    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)

    chart_data = chart_data[(chart_data['date'] > start_time) & (chart_data['date'] < end_time)]

    for column in ['pm25', 'pm10', 'o3', 'no2', 'so2', 'co']:
        chart_data[column] = chart_data[column].astype('Float64')

    tab.line_chart(chart_data, x='date', y=['pm25', 'pm10', 'o3', 'no2', 'so2', 'co'])
