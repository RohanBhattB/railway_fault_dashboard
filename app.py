import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_and_predict

# Page setup
st.set_page_config(
    page_title="Railway Track Health Monitor",
    layout="wide"
)

# Title
st.title("🚆 Railway Track Health Monitoring Dashboard")

# Load ML results
df = train_and_predict()

# Initialize maintenance state in session
if "maintenance_status" not in st.session_state:
    st.session_state.maintenance_status = {}


# Add maintenance status if not present
if "Maintenance_Done" not in df.columns:
    df["Maintenance_Done"] = False


# =======================
# TOP METRICS
# =======================
good_count = (df["Condition"] == "Good").sum()
ok_count = (df["Condition"] == "OK").sum()
danger_count = (df["Condition"] == "Danger").sum()

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        label="🟢 Good Tracks",
        value=good_count
    )

with m2:
    st.metric(
        label="🟡 OK Tracks",
        value=ok_count
    )

with m3:
    if danger_count > 0:
        st.error(f"🚨 Dangerous Tracks: {danger_count}")
        st.caption("Immediate inspection required")
    else:
        st.success("✅ Dangerous Tracks: 0")
        st.caption("All track segments are safe")


# =======================
# SIDEBAR – EMERGENCY PANEL
# =======================
# =======================
# SIDEBAR – EMERGENCY PANEL
# =======================
st.sidebar.title("🚨 Emergency Alerts")

# Severity ranking
severity_map = {
    "Danger": 3,
    "OK": 2,
    "Good": 1
}

df["Severity"] = df["Condition"].map(severity_map)

# Convert time column
df["path_time"] = pd.to_datetime(df["path"])

# Filter only dangerous & unresolved tracks
emergency_df = df[
    (df["Condition"] == "Danger") &
    (~df.index.isin(st.session_state.maintenance_status.keys()))
]


# Sort by severity then time
emergency_df = emergency_df.sort_values(
    by=["Severity", "path_time"],
    ascending=[False, False]
)

if len(emergency_df) > 0:
    st.sidebar.error(f"{len(emergency_df)} Dangerous Track Segments")

    # Download emergency alerts as CSV
    csv_data = emergency_df.to_csv(index=False).encode("utf-8")

    st.sidebar.download_button(
        label="⬇️ Download Emergency CSV",
        data=csv_data,
        file_name="railway_emergency_alerts.csv",
        mime="text/csv"
    )

    # Select emergency
    selected_index = st.sidebar.radio(
        "⚠️ Select a track for details:",
        emergency_df.index.tolist(),
        format_func=lambda i: f"⏱️ {emergency_df.loc[i, 'path_time']}"
    )
else:
    st.sidebar.success("No dangerous conditions detected")
    selected_index = None

# =======================
# MAIN DASHBOARD
# =======================
col1, col2 = st.columns(2)

# Pie chart
with col1:
    st.subheader("📊 Track Condition Percentage")
    pie_fig = px.pie(
        df,
        names="Condition",
        title="Overall Track Health",
        color="Condition",
        color_discrete_map={
            "Good": "green",
            "OK": "orange",
            "Danger": "red"
        }
    )
    st.plotly_chart(pie_fig, use_container_width=True)

# Bar chart
# Bar chart
with col2:
    st.subheader("📈 Condition Count")

    condition_counts = (
        df["Condition"]
        .value_counts()
        .reset_index()
        .rename(columns={"index": "Condition", "count": "Count"})
    )

    bar_fig = px.bar(
        condition_counts,
        x="Condition",
        y="Count",
        color="Condition",
        color_discrete_map={
            "Good": "green",
            "OK": "orange",
            "Danger": "red"
        }
    )

    st.plotly_chart(bar_fig, use_container_width=True)
# =======================
# SELECTED EMERGENCY DETAILS
# =======================
# =======================
# SELECTED EMERGENCY DETAILS
# =======================
if selected_index is not None:
    st.markdown("---")
    st.subheader("🚨 Selected Emergency Details")

    selected_row = df.loc[selected_index]

    st.write("**Time:**", selected_row["path_time"])
    st.write("**Condition:**", selected_row["Condition"])
    st.write("**Predicted Fault:**", selected_row["Predicted_Label"])

 
        # Maintenance checkbox with session state
    checkbox_key = f"maintenance_{selected_index}"

    maintenance_done = st.checkbox(
        "✅ Mark maintenance as completed",
        key=checkbox_key
    )

    if maintenance_done:
        st.session_state.maintenance_status[selected_index] = True
        st.success("Maintenance marked as completed.")
        st.info("This alert will no longer appear in Emergency Alerts.")


# =======================
# DATA TABLE
# =======================
st.subheader("📋 Detailed Track Analysis")
st.dataframe(df)

st.markdown("---")
st.subheader("ℹ️ Track Condition Definitions")

st.markdown("""
🟢 **Good**  
- Normal vibration levels  
- No detectable faults  
- Safe for railway operation  

🟡 **OK**  
- Minor misalignment detected  
- Requires monitoring  
- Maintenance recommended  

🔴 **Dangerous**  
- Bearing or unbalance faults detected  
- High vibration severity  
- Immediate inspection required  
""")

