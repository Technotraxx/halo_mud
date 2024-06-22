import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(layout="wide", page_title="Reach Surface - Entering ONI Facility")

# Custom CSS to improve the look
st.markdown("""
<style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .stAlert {
        background-color: #2C3E50;
        color: #FFFFFF;
    }
    .css-1aumxhk {
        background-color: #2C3E50;
    }
</style>
""", unsafe_allow_html=True)

def create_battlefield_view():
    fig = go.Figure()

    # Background
    fig.add_shape(type="rect", x0=0, y0=0, x1=400, y1=300, fillcolor="#4A3C31", line_color="#4A3C31")

    # ONI outpost
    fig.add_shape(type="rect", x0=250, y0=200, x1=400, y1=300, fillcolor="#1E90FF", line_color="black")
    fig.add_annotation(x=325, y=250, text="ONI Outpost", showarrow=False, font=dict(color="white", size=12))

    # Open hatch
    fig.add_shape(type="rect", x0=390, y0=280, x1=400, y1=300, fillcolor="black", line_color="#00FF00")
    fig.add_annotation(x=385, y=290, text="Hatch", showarrow=False, font=dict(color="white", size=10), xanchor="right")

    # Team entering facility (simplified)
    fig.add_trace(go.Scatter(x=[395, 395, 395, 390], y=[270, 270, 270, 270], mode="markers",
                             marker=dict(size=10, color=["blue", "yellow", "green", "red"], opacity=0.7)))

    # Banshees (improved)
    t = np.linspace(0, 1, 100)
    x = 50 + 200 * t
    y = 50 + 100 * np.sin(2 * np.pi * t)
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", line=dict(color="#FF00FF", width=2)))
    fig.add_annotation(x=150, y=40, text="Banshees", showarrow=False, font=dict(color="#FF00FF", size=12))

    # Add smoke effect (simplified)
    fig.add_trace(go.Scatter(x=[380], y=[270], mode="markers", marker=dict(size=40, color="rgba(169,169,169,0.7)")))

    fig.update_layout(
        showlegend=False,
        width=600,
        height=450,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return fig

def battlefield_status():
    st.subheader("Battlefield Status")
    status = [
        ("🔓", "Facility Access: Hatch Open, Team Entering"),
        ("💨", "Smoke Screen: Deployed, Obscuring Entry"),
        ("✈️", "Air Threat: Banshees Engaged, Visibility Reduced"),
        ("🛡️", "Team Status: Transitioning to Interior, Exposed Momentarily"),
        ("⚡", "Artifact: Active, Entering Facility"),
        ("👁️", "Visibility: Limited Outside, Unknown Inside"),
        ("⏰", "Time Pressure: Critical, Seconds to Clear Entry")
    ]
    for icon, text in status:
        st.markdown(f"<div style='display: flex; align-items: center;'><div style='font-size: 24px; margin-right: 10px;'>{icon}</div><div>{text}</div></div>", unsafe_allow_html=True)

def character_info():
    st.subheader("Spartan Status")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Stats**")
        st.markdown("<div style='display: flex; align-items: center;'><div style='color: red; margin-right: 10px;'>❤️</div><div>Health: 95</div></div>", unsafe_allow_html=True)
        st.progress(95)
        st.markdown("<div style='display: flex; align-items: center;'><div style='color: yellow; margin-right: 10px;'>🛡️</div><div>Shield: 75 (Recharging)</div></div>", unsafe_allow_html=True)
        st.progress(75)
        st.markdown("<div style='display: flex; align-items: center;'><div style='color: yellow; margin-right: 10px;'>🎯</div><div>Ammo: 45 / 12</div></div>", unsafe_allow_html=True)

    with col2:
        st.write("**Inventory**")
        inventory = [
            "Combat Knife",
            "Frag Grenade (x1)",
            "Medkit",
            "MA5B Assault Rifle",
            "M6D Pistol",
            "ODST Drop Pod Beacon",
            "Recovered Datapad",
            "Forerunner Artifact"
        ]
        for item in inventory:
            st.markdown(f"• {item}")

    st.write("**Current Mission**")
    st.info("Enter ONI facility. Secure interior position. Assess internal situation and potential threats.")

def main():
    st.title("Reach Surface - Entering ONI Facility")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("Battlefield View")
        st.plotly_chart(create_battlefield_view(), use_container_width=True)
        battlefield_status()

    with col2:
        character_info()

if __name__ == "__main__":
    main()
