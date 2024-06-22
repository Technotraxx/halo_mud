import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Reach Surface - Entering ONI Facility")

# Custom CSS
st.markdown("""
<style>
    .main-content {
        background-color: #666666;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 5px;
    }
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #4CAF50 !important;
        margin-bottom: 20px;
        text-align: center;
    }
    .section-title {
        font-size: 1.5em;
        font-weight: bold;
        color: #3498db !important;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    .info-box {
        background-color: #34495e;
        color: #FFFFFF;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
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
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

def create_battlefield_view():
    fig = go.Figure()

    # Background
    fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100, fillcolor="#4A3C31", line_color="#4A3C31")

    # ONI outpost
    fig.add_shape(type="rect", x0=60, y0=60, x1=100, y1=100, fillcolor="#1E90FF", line_color="black")
    fig.add_annotation(x=80, y=80, text="ONI Outpost", showarrow=False, font=dict(color="white", size=12))

    # Open hatch
    fig.add_shape(type="rect", x0=95, y0=95, x1=100, y1=100, fillcolor="black", line_color="#00FF00")
    fig.add_annotation(x=94, y=97, text="Hatch", showarrow=False, font=dict(color="white", size=10), xanchor="right")

    # Team entering facility
    fig.add_trace(go.Scatter(x=[97, 97, 97, 96], y=[93, 93, 93, 93], mode="markers",
                             marker=dict(size=10, color=["blue", "yellow", "green", "red"], opacity=0.7)))

    # Banshees
    t = np.linspace(0, 1, 100)
    x = 10 + 50 * t
    y = 20 + 30 * np.sin(2 * np.pi * t)
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", line=dict(color="#FF00FF", width=2)))
    fig.add_annotation(x=35, y=10, text="Banshees", showarrow=False, font=dict(color="#FF00FF", size=12))

    # Smoke effect
    fig.add_trace(go.Scatter(x=[95], y=[93], mode="markers", marker=dict(size=20, color="rgba(169,169,169,0.7)")))

    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig

def battlefield_status():
    st.markdown('<p class="section-title">Battlefield Status</p>', unsafe_allow_html=True)
    status = [
        ("🔓", "Facility Access: Hatch Open, Team Entering"),
        ("💨", "Smoke Screen: Deployed, Obscuring Entry"),
        ("✈️", "Air Threat: Banshees Engaged, Visibility Reduced"),
        ("🛡️", "Team Status: Transitioning to Interior, Exposed Momentarily"),
    ]
    for icon, text in status:
        st.markdown(f'<div style="display: flex; align-items: center; margin-bottom: 5px;"><span style="font-size: 24px; margin-right: 10px;">{icon}</span>{text}</div>', unsafe_allow_html=True)

def sidebar_content():
    st.markdown('<p class="section-title">Current Mission</p>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">Enter ONI facility. Secure interior position. Assess internal situation and potential threats.</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">Spartan Status</p>', unsafe_allow_html=True)
    st.markdown('❤️ Health: 95', unsafe_allow_html=True)
    st.progress(95)
    st.markdown('🛡️ Shield: 75 (Recharging)', unsafe_allow_html=True)
    st.progress(75)
    st.markdown('🎯 Ammo: 45 / 12', unsafe_allow_html=True)
    
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

def main():
    st.markdown('<div class="main-content"><h1 class="main-title">Reach Surface - Entering ONI Facility</h1>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        sidebar_content()

    # Main content
    col1, col2 = st.columns([1, 3])

    with col1:
        battlefield_status()

    with col2:
        st.plotly_chart(create_battlefield_view(), use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
