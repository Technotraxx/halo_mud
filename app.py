import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Reach Surface - Entering ONI Facility")

# Custom CSS for improved styling
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50;
        margin-bottom: 20px;
        text-align: center;
    }
    .section-title {
        font-size: 1.5em;
        font-weight: bold;
        color: #3498db;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    .info-box {
        background-color: #2C3E50;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .status-item {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
    }
    .status-icon {
        font-size: 24px;
        margin-right: 10px;
    }
    .progress-label {
        margin-bottom: 0;
    }
    .inventory-item {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
    }
    .inventory-icon {
        font-size: 20px;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

def create_battlefield_view():
    # Your existing battlefield view code here
    # ...

def battlefield_status():
    st.markdown('<p class="section-title">Battlefield Status</p>', unsafe_allow_html=True)
    status = [
        ("🔓", "Facility Access: Hatch Open, Team Entering"),
        ("💨", "Smoke Screen: Deployed, Obscuring Entry"),
        ("✈️", "Air Threat: Banshees Engaged, Visibility Reduced"),
        ("🛡️", "Team Status: Transitioning to Interior, Exposed Momentarily"),
    ]
    for icon, text in status:
        st.markdown(f'<div class="status-item"><span class="status-icon">{icon}</span>{text}</div>', unsafe_allow_html=True)

def spartan_status():
    st.markdown('<p class="section-title">Spartan Status</p>', unsafe_allow_html=True)
    st.markdown('<p class="progress-label">❤️ Health: 95</p>', unsafe_allow_html=True)
    st.progress(95)
    st.markdown('<p class="progress-label">🛡️ Shield: 75 (Recharging)</p>', unsafe_allow_html=True)
    st.progress(75)
    st.markdown('<p class="progress-label">🎯 Ammo: 45 / 12</p>', unsafe_allow_html=True)

def inventory():
    st.markdown('<p class="section-title">Inventory</p>', unsafe_allow_html=True)
    inventory_items = [
        ("🔪", "Combat Knife"),
        ("💣", "Frag Grenade (x1)"),
        ("🩹", "Medkit"),
        ("🔫", "MA5B Assault Rifle"),
        ("🔫", "M6D Pistol"),
        ("📡", "ODST Drop Pod Beacon"),
        ("💾", "Recovered Datapad"),
        ("🔮", "Forerunner Artifact")
    ]
    for icon, name in inventory_items:
        st.markdown(f'<div class="inventory-item"><span class="inventory-icon">{icon}</span>{name}</div>', unsafe_allow_html=True)

def current_mission():
    st.markdown('<p class="section-title">Current Mission</p>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">Enter ONI facility. Secure interior position. Assess internal situation and potential threats.</div>', unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-title">Reach Surface - Entering ONI Facility</h1>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        current_mission()
        spartan_status()
        inventory()

    # Main content
    col1, col2 = st.columns([1, 3])

    with col1:
        battlefield_status()

    with col2:
        st.plotly_chart(create_battlefield_view(), use_container_width=True)

if __name__ == "__main__":
    main()
