import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html


# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("projects.csv")

df = pd.read_csv("projects.csv")

date_cols = [
    "planned_planning_start",
    "actual_planning_start",
    "planned_execution_start",
    "actual_execution_start",
    "planned_review_start",
    "actual_review_start",
    "planned_closure_start",
    "actual_closure_start"
]

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")


# -------------------------
# VALIDATION
# -------------------------
def is_valid(row):

    if row["planned_capacity"] <= 0 or row["staffed_capacity"] <= 0:
        return False

    if pd.notnull(row["actual_execution_start"]) and row["actual_execution_start"] < row["actual_planning_start"]:
        return False

    if pd.notnull(row["actual_review_start"]) and row["actual_review_start"] < row["actual_execution_start"]:
        return False

    if pd.notnull(row["actual_closure_start"]) and row["actual_closure_start"] < row["actual_review_start"]:
        return False

    return True


df["valid"] = df.apply(is_valid, axis=1)
df_valid = df[df["valid"]].copy()


# -------------------------
# FEATURE ENGINEERING
# -------------------------
df_valid["capacity_gap"] = df_valid["staffed_capacity"] - df_valid["planned_capacity"]


def compute_delay(planned, actual):
    if pd.isnull(planned) or pd.isnull(actual):
        return np.nan
    return (actual - planned).days


df_valid["delay_planning"] = df_valid.apply(
    lambda r: compute_delay(r["planned_planning_start"], r["actual_planning_start"]),
    axis=1
)

df_valid["delay_execution"] = df_valid.apply(
    lambda r: compute_delay(r["planned_execution_start"], r["actual_execution_start"]),
    axis=1
)

df_valid["delay_review"] = df_valid.apply(
    lambda r: compute_delay(r["planned_review_start"], r["actual_review_start"]),
    axis=1
)

df_valid["delay_closure"] = df_valid.apply(
    lambda r: compute_delay(r["planned_closure_start"], r["actual_closure_start"]),
    axis=1
)


delay_summary = pd.DataFrame({
    "phase": ["Planning", "Execution", "Review", "Closure"],
    "avg_delay_days": [
        df_valid["delay_planning"].dropna().mean(),
        df_valid["delay_execution"].dropna().mean(),
        df_valid["delay_review"].dropna().mean(),
        df_valid["delay_closure"].dropna().mean()
    ]
})


# -------------------------
# ANALYTICS
# -------------------------
region_counts = df_valid["region"].value_counts().reset_index()
region_counts.columns = ["region", "count"]

phase_counts = df_valid["current_phase"].value_counts().reset_index()
phase_counts.columns = ["current_phase", "count"]

capacity = df_valid.groupby("region")["capacity_gap"].mean().reset_index()


# -------------------------
# DASHBOARD
# -------------------------
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Project Monitoring Dashboard", style={"textAlign": "center"}),

    dcc.Graph(
        figure=px.bar(
            region_counts,
            x="region",
            y="count",
            title="Projects per Country"
        )
    ),

    dcc.Graph(
        figure=px.bar(
            phase_counts,
            x="current_phase",
            y="count",
            title="Projects by Phase"
        )
    ),

    dcc.Graph(
        figure=px.bar(
            capacity,
            x="region",
            y="capacity_gap",
            title="Capacity Gap"
        )
    ),

    dcc.Graph(
        figure=px.bar(
            delay_summary,
            x="phase",
            y="avg_delay_days",
            title="Average Delay per Phase (days)"
        )
    ),

])


# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
