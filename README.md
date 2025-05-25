# 🚀 Orion Nexus: A Multi-Agent Space Mission Planner & Astronomical Assistant

Orion Nexus is a smart, interactive, and educational platform designed to simulate space missions and plan astronomical observations. Built using real-time data from NASA, Skyfield, and weather APIs, this project is ideal for students, educators, and space enthusiasts who want a realistic yet simplified mission control experience.

---

## 🌌 Table of Contents

- [🔭 Features](#-features)
- [🤖 Multi-Agent Architecture](#-multi-agent-architecture)
- [🧠 Team Roles](#-team-roles)
- [🧰 Tech Stack](#-tech-stack)
- [🌐 Live APIs & Data Sources](#-live-apis--data-sources)
- [⚙️ Setup Instructions](#️-setup-instructions)
- [👨‍💻 Contributors](#-contributors)
- [📄 License](#-license)
- [🌟 Acknowledgements](#-acknowledgements)

---

## 🔭 Features

- Plan missions from Earth to other planets using live orbital data.
- Determine best launch windows based on planetary alignment.
- Calculate fuel requirements and Δv using simplified astrodynamics.
- Visualize orbits and planetary paths in 2D/3D.
- Discover upcoming celestial events (eclipses, ISS passes, meteor showers).
- Get weather-based recommendations for observation or launch.
- Interactive AI-powered Mission Assistant.

---

## 🤖 Multi-Agent Architecture

| Agent Name             | Functionality                                                                 |
|------------------------|-------------------------------------------------------------------------------|
| Trajectory Agent       | Computes orbital paths (e.g., Hohmann transfer) using Skyfield/NASA APIs.    |
| Launch Window Agent    | Determines ideal planetary alignment dates.                                  |
| Fuel Agent             | Simulates required Δv and fuel based on spacecraft and mission type.         |
| Weather Agent          | Fetches weather/cloud data at launch or observation site.                    |
| Event Agent            | Fetches upcoming space events via NASA or timeanddate APIs.                  |
| Geo Agent              | Gets user's location and visibility conditions.                              |
| Recommendation Agent   | Suggests best observation or launch times.                                   |
| Mission Control Agent  | Main coordinator and user interaction manager.                               |

---

## 🧠 Team Roles

| Name               | Designation                                                   | Skills                                      |
|--------------------|---------------------------------------------------------------|---------------------------------------------|
| Kaviyan S          | Chief Systems Architect & Mission Interface Commander         | Full Stack · DSA · Logical Thinking         |
| Lakshmi Narayanan  | Orbital Mechanics Strategist & Computational Analyst          | DSA · Algorithms · Aptitude · Mathematics   |
| Madhan Kumar M     | Autonomous Intelligence Architect & Multi-Agent Orchestrator  | AI Logics · Automation · Logical Reasoning  |

---

## 🧰 Tech Stack

### Frontend:
- HTML / CSS / JavaScript
- Streamlit (for interactive dashboard)
- Plotly / Three.js (for orbit visualizations)

### Backend:
- Python
- FastAPI / Flask

### Libraries & Tools:
- Skyfield
- Astroquery / PyEphem
- NumPy / Matplotlib
- OpenWeatherMap API
- NASA APIs
- IPinfo / Geolocation APIs

---

## 🌐 Live APIs & Data Sources

- NASA APIs: https://api.nasa.gov
- Skyfield Ephemeris: https://rhodesmill.org/skyfield/
- OpenWeatherMap: https://openweathermap.org/api
- Time and Date: https://www.timeanddate.com
- IPinfo Location API: https://ipinfo.io/

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/kaviyans/Astropath
   cd Astropath
