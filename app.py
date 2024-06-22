import streamlit as st
import base64

# Define the SVG content
battlefield_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="auto">
    <defs>
        <radialGradient id="smokeGradient" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#888888" stop-opacity="0.9"/>
            <stop offset="100%" stop-color="#888888" stop-opacity="0"/>
        </radialGradient>
    </defs>
    <rect x="0" y="0" width="400" height="300" fill="#4A3C31"/>
    <rect x="250" y="50" width="150" height="100" fill="#1E90FF" stroke="#000000" stroke-width="2"/>
    <text x="325" y="100" fill="white" font-size="10" text-anchor="middle">ONI Outpost</text>
    <rect x="390" y="120" width="10" height="20" fill="#000000" stroke="#00FF00" stroke-width="1"/>
    <text x="385" y="135" fill="white" font-size="8" text-anchor="end">Hatch</text>
    <circle cx="395" cy="130" r="5" fill="#0000FF" opacity="0.7"/>
    <circle cx="395" cy="130" r="5" fill="#FFFF00" opacity="0.7">
        <animate attributeName="cx" from="395" to="400" dur="0.5s" fill="freeze" />
        <animate attributeName="cy" from="130" to="130" dur="0.5s" fill="freeze" />
    </circle>
    <circle cx="395" cy="130" r="5" fill="#00FF00" opacity="0.7">
        <animate attributeName="cx" from="395" to="400" dur="0.7s" fill="freeze" />
        <animate attributeName="cy" from="130" to="130" dur="0.7s" fill="freeze" />
    </circle>
    <circle cx="390" cy="130" r="5" fill="#FF0000" opacity="0.7"/>
    <circle cx="380" cy="130" r="40" fill="url(#smokeGradient)">
        <animate attributeName="r" from="0" to="40" dur="1s" fill="freeze" />
    </circle>
    <path d="M50 50 Q 150 30, 250 50" fill="none" stroke="#FF00FF" stroke-width="2">
        <animate attributeName="d" values="M50 50 Q 150 30, 250 50; M100 100 Q 200 80, 300 100; M150 150 Q 250 130, 350 150" dur="2s" repeatCount="indefinite" />
    </path>
    <path d="M30 30 Q 130 10, 230 30" fill="none" stroke="#FF00FF" stroke-width="2">
        <animate attributeName="d" values="M30 30 Q 130 10, 230 30; M80 80 Q 180 60, 280 80; M130 130 Q 230 110, 330 130" dur="2s" repeatCount="indefinite" />
    </path>
    <text x="150" y="40" fill="#FF00FF" font-size="10">Banshees</text>
    <circle cx="300" cy="110" r="2" fill="#FF00FF">
        <animate attributeName="cx" values="300;310;320" dur="0.2s" repeatCount="indefinite" />
        <animate attributeName="cy" values="110;120;130" dur="0.2s" repeatCount="indefinite" />
    </circle>
    <circle cx="320" cy="130" r="2" fill="#FF00FF">
        <animate attributeName="cx" values="320;330;340" dur="0.2s" repeatCount="indefinite" />
        <animate attributeName="cy" values="130;140;150" dur="0.2s" repeatCount="indefinite" />
    </circle>
</svg>
'''

# Function to render the SVG
def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" style="max-width: 70%; height: 50%;"/>'
    return html

# Streamlit app
def main():
    st.set_page_config(layout="wide", page_title="Reach Surface - Entering ONI Facility")

    # Custom CSS
    st.markdown("""
    <style>
    .main-content { background-color: #1E1E1E; color: #FFFFFF; padding: 20px; border-radius: 5px; }
    .title { color: #4CAF50; text-align: left; }
    .subtitle { color: #3498db; }
    </style>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown('<h1 class="title">Reach Surface - Entering ONI Facility</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">Battlefield Status</h2>', unsafe_allow_html=True)
    st.markdown("""
        🔓 Facility Access: Hatch Open, Team Entering\n
        💨 Smoke Screen: Deployed, Obscuring Entry\n
        ✈️ Air Threat: Banshees Engaged, Visibility Reduced\n
        🛡️ Team Status: Transitioning to Interior, Exposed Momentarily\n
        """)

    st.markdown('<h2 class="subtitle">Battlefield View</h2>', unsafe_allow_html=True)
    st.markdown(render_svg(battlefield_svg), unsafe_allow_html=True)

    # Sidebar content
    with st.sidebar:
        st.header("Current Mission")
        st.info("Enter ONI facility. Secure interior position. Assess internal situation and potential threats.")
        
        st.header("Spartan Status")
        st.progress(95, text="Health: 95")
        st.progress(75, text="Shield: 75 (Recharging)")
        st.write("🎯 Ammo: 45 / 12")
        
        st.header("Inventory")
        inventory = ["🔪 Combat Knife", "💣 Frag Grenade (x1)", "🩹 Medkit", "🔫 MA5B Assault Rifle",
                     "🔫 M6D Pistol", "📡 ODST Drop Pod Beacon", "💾 Recovered Datapad", "🔮 Forerunner Artifact"]
        for item in inventory:
            st.write(item)

if __name__ == "__main__":
    main()
