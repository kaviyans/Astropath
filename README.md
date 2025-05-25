🚀 Orion Nexus: A Multi-Agent Space Mission Planner & Astronomical Assistant
Orion Nexus is a web-based multi-agent simulation and planning platform that enables users to plan interplanetary space missions and discover upcoming celestial events using real-time astronomical data. Designed for students, educators, and space enthusiasts, it blends educational visualization with intelligent agent coordination.

—

🌌 Table of Contents

🔭 Features

🤖 Multi-Agent Architecture

🧠 Team Roles

🧰 Tech Stack

🌐 Live APIs & Data Sources

📸 Screenshots (Optional)

⚙️ Setup Instructions

👨‍💻 Contributors

📄 License

—

🔭 Features

Plan space missions (e.g. Earth to Mars) using realistic data

Get optimal launch windows, Δv, and fuel estimates

Visualize orbital paths in 2D/3D

Discover upcoming celestial events (ISS passes, meteor showers)

Personalized observation suggestions with weather integration

AI-based educational assistant to guide users through planning

Download/share mission reports or stargazing cards

—

🤖 Multi-Agent Architecture

Agent Name	Role & Description
Trajectory Agent	Computes orbital transfers (e.g., Hohmann transfer) using Skyfield or NASA APIs
Launch Window Agent	Calculates best dates to launch based on planetary alignment
Fuel Agent	Simulates Δv requirements and spacecraft fuel usage
Weather Agent	Checks launch site/cloud visibility weather (via OpenWeatherMap)
Event Agent	Fetches upcoming events like eclipses, meteor showers (NASA, Timeanddate, etc.)
Geo Agent	Determines best observation spots via user location
Recommendation Agent	Suggests ideal mission schedules and stargazing times
Mission Control (UI)	Takes user input, handles coordination between agents

—

🧠 Team Roles

Name	Designation	Skills
Kaviyan S	Chief Systems Architect & Mission Interface Commander	Full Stack · DSA · Logical Thinking
Lakshmi Narayanan	Orbital Mechanics Strategist & Computational Analyst	DSA · Algorithms · Aptitude · Mathematics
Madhan Kumar M	Autonomous Intelligence Architect & Multi-Agent Orchestrator	AI Logics · Automation · Logic Building

—

🧰 Tech Stack

Frontend:

HTML / CSS / JavaScript

Streamlit (for rapid dashboard prototyping)

Plotly / Three.js (for orbital visualizations)

Backend:

Python

FastAPI / Flask

Libraries & Tools:

Skyfield (planetary positions)

Astroquery / PyEphem (astronomical calculations)

NumPy, Matplotlib (math/visuals)

OpenWeatherMap API (weather)

NASA Open APIs (ephemeris data)

IPinfo / Geolocation APIs

—

🌐 Live Data Sources & APIs

NASA APIs: https://api.nasa.gov

Skyfield Ephemeris: https://rhodesmill.org/skyfield/

OpenWeatherMap: https://openweathermap.org/api

IP Geolocation: https://ipinfo.io/

Time and Date API: https://www.timeanddate.com/

—

📸 Screenshots (Coming Soon)

📊 Mission Planner UI
🪐 Orbital Path Visualizer
📅 Stargazing Recommendations Card
📍 Map-based Best Viewing Locations

—

⚙️ Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/orion-nexus.git
cd orion-nexus

Install dependencies:

pip install -r requirements.txt

Run the backend server:

uvicorn main:app --reload

Launch the frontend:

streamlit run ui_dashboard.py

—

👨‍💻 Contributors

✨ Kaviyan S – Full Stack & Architecture
🔬 Lakshmi Narayanan – Backend Logic & Orbital Math
🧠 Madhan Kumar M – AI Planner & Agent Intelligence

—

📄 License

This project is licensed under the MIT License.
See LICENSE for details.

—

🌟 Acknowledgements

Inspired by NASA Mission Planning tools, ISRO’s Aryabhata & Chandrayaan, and Carl Sagan’s vision of cosmic curiosity.

Open-source data powered by NASA, Skyfield, and OpenWeatherMap.

—
