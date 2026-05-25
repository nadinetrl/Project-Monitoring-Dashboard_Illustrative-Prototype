# Project Monitoring Dashboard (Illustrative Prototype)

This project simulates a lightweight monitoring dashboard for projects that could be used by international organizations or companies to track and assess project planning and execution across regions.

The dashboard is based on fully simulated project data and is intended for demonstration purposes only.

---

## Project Overview

The dashboard provides an analytical overview of project activities, including:

- Distribution of projects across regions
- Current project phase status
- Capacity efficiency (planned vs. staffed capacity)
- Delay analysis across project phases


The project demonstrates a simplified end-to-end analytics workflow, including:

- Data loading and preprocessing
- Basic data validation and quality checks
- Feature engineering
- Interactive dashboarding in Python

Please note that the analytics presented in this dashboard are illustrative and intentionally simplified and designed to demonstrate selected monitoring concepts rather than provide a fully-fledged model.

---

## Features

### 1. Data Validation

The implemented validation logic includes a basic set of consistency checks to ensure data usability, including:
- Basic checks on capacity values
- Logical sequencing of project phases (chronological validation)
- Handling of missing or invalid date values

These checks are intended as a minimal example of data quality checks and do not constitute a complete validation framework.

### 2. Key Metrics

The dashboard includes simplified monitoring indicators, such as:

- Project counts by region
- Project phase distribution
- Capacity gap (planned vs. staffed)
- Average delays per project phase

### 3. Interactive Dashboard

The dashboard is built using Dash & Plotly for interactive visual analytics.

---

## Project Structure

Project-Monitoring-Dashboard_Illustrative-Prototype/
│
├── main.py
├── requirements.txt
└── projects.csv

---

## How to Run

### 1. Clone repository

git clone https://github.com/nadinetrl/Project-Monitoring-Dashboard_Illustrative-Prototype.git

### 2. Navigate into project folder

cd Project-Monitoring-Dashboard_Illustrative-Prototype

### 3. Install dependencies

python3 -m pip install -r requirements.txt

### 4. Run dashboard

python3 main.py

### 5. Open in browser
http://127.0.0.1:8050/

---

## Tech Stack

- Python
- Pandas
- NumPy
- Plotly
- Dash
