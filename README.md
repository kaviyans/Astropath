# 🚀 AstroPath : A Multi-Agent Space Mission Planner & Astronomical Assistant

Orion Nexus is a smart, interactive, and educational platform designed to simulate space missions and plan astronomical observations. Built using real-time data from NASA, Skyfield, and weather APIs, this project is ideal for students, educators, and space enthusiasts who want a realistic yet simplified mission control experience.

---
Google Adk Resource-[https://google.github.io/adk-docs/]

## Project - Status : ---IN PROGRESS --

## 🌌 Table of Contents

- [🚀 AstroPath : A Multi-Agent Space Mission Planner \& Astronomical Assistant](#-astropath--a-multi-agent-space-mission-planner--astronomical-assistant)
  - [Project - Status : ---IN PROGRESS --](#project---status-----in-progress---)
  - [🌌 Table of Contents](#-table-of-contents)
  - [🔭 Features](#-features)
  - [🤖 Multi-Agent Architecture](#-multi-agent-architecture)
  - [🧠 Team Roles](#-team-roles)
  - [🧰 Tech Stack](#-tech-stack)
    - [Frontend:](#frontend)
    - [Backend:](#backend)
    - [Libraries \& Tools:](#libraries--tools)
  - [🌐 Live APIs \& Data Sources](#-live-apis--data-sources)
  - [⚙️ Setup Instructions](#️-setup-instructions)

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

---

## 🤖 What is an “Agent”?

In AI and software systems, an **agent** is an independent program (or microservice) that:

* **Perceives** information from its environment.
* **Processes** it using rules or models.
* **Acts** or gives output (suggestions, alerts, decisions).
  Each agent has a **goal** and **autonomy**, yet collaborates with others in a system like a real **space agency mission team**.

---

## 🛰️ AstroPath Agents — Roles, Design & Workflows

---

### 1. **Trajectory Agent**

* **Goal:** Calculate the best path to travel between planets.
* **Inputs:** Start date, source planet, destination planet.
* **Output:** Orbital trajectory, travel time, delta-v required.
* **How to Make It Work:**

  * Use `Skyfield` to get planetary positions.
  * Implement Hohmann transfer or Lambert's problem using orbital mechanics formulas.
  * Respond with optimal path based on energy-efficient routes.
* **Acts like an Agent by:**

  * Reacting to user destination choices.
  * Calculating and updating route if launch date or planet changes.

---

### 2. **Launch Window Agent**

* **Goal:** Find the best date to launch based on planetary alignment.
* **Inputs:** Source and target planets, mission duration.
* **Output:** Best launch windows (dates).
* **How to Make It Work:**

  * Use `Skyfield` or `Astroquery` to get ephemerides.
  * Compute angular positions between planets to find closest approach dates.
* **Acts like an Agent by:**

  * Watching planetary motion and triggering updates when optimal conditions approach.

---

### 3. **Fuel Agent**

* **Goal:** Calculate fuel and Δv requirements.
* **Inputs:** Spacecraft model, trajectory, payload.
* **Output:** Required propellant, optimal fuel type.
* **How to Make It Work:**

  * Use Tsiolkovsky Rocket Equation.
  * Store spacecraft configurations (mass, Isp) in a dictionary or DB.
* **Acts like an Agent by:**

  * Listening to trajectory and payload changes.
  * Recalculating when constraints change.

---

### 4. **Weather Agent**

* **Goal:** Predict weather at launch site to approve/reject launch.
* **Inputs:** Location, launch date.
* **Output:** Weather condition (cloud cover, wind, storms).
* **How to Make It Work:**

  * Query OpenWeatherMap API for forecast.
  * Logic: If cloud > 80% or wind > threshold → recommend delay.
* **Acts like an Agent by:**

  * Fetching real-time data, alerting Mission Control to reschedule.

---

### 5. **Mission Control Agent** *(Main Brain)*

* **Goal:** Manage all agents, combine insights, interact with the user.
* **Inputs:** User input (target, budget), agent outputs.
* **Output:** Final plan, alerts, user feedback.
* **How to Make It Work:**

  * Use `FastAPI` or `LangChain`-style flow manager.
  * Acts as the **central orchestrator**:

    * Receives all agent outputs.
    * Applies mission rules (e.g., can't launch if weather is bad).
    * Makes final decisions based on agent consensus.
* **Acts like an Agent by:**

  * Governing and re-routing decisions based on dynamic agent data.

---

### 6. **Event Agent**

* **Goal:** Find upcoming celestial events like meteor showers, eclipses.
* **Inputs:** User location/date.
* **Output:** List of events and viewing conditions.
* **How to Make It Work:**

  * Use NASA APIs or scrape from `TimeAndDate.com`.
  * Maintain a calendar of events.
* **Acts like an Agent by:**

  * Constantly monitoring external APIs.
  * Notifying users when events are visible in their area.

---

### 7. **Geo Agent**

* **Goal:** Get user’s location for visibility and event planning.
* **Inputs:** User IP or manual input.
* **Output:** Latitude/longitude.
* **How to Make It Work:**

  * Use `Geopy` or `IPinfo` API.
* **Acts like an Agent by:**

  * Providing live geographic context to other agents (Event, Weather).

---

### 8. **Recommendation Agent**

* **Goal:** Suggest best times and places to view space events.
* **Inputs:** Weather, event data, geo-location.
* **Output:** Time and spot for best viewing.
* **How to Make It Work:**

  * Combine weather and event visibility rules.
  * Logic: Suggest only if cloud < 30% and event peak visible.
* **Acts like an Agent by:**

  * Filtering and scoring conditions to give final suggestion.

---

### 9. **Scientist Agent (UI Agent)**

* **Goal:** Present all the information clearly to the user.
* **Inputs:** Data from all agents.
* **Output:** Graphs, maps, alerts, chat summaries.
* **How to Make It Work:**

  * Acts as the **visual face** of the AI.
  * Uses frameworks like Streamlit or Next.js to display data interactively.
* **Acts like an Agent by:**

  * Listening to all backend outputs and keeping the UI updated dynamically.

---
