import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of time zones (general or famous ones)
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",  # Pakistan
    "Asia/Kolkata",  # India
    "Asia/Shanghai", # China
    "Asia/Dubai",    # UAE
    "Asia/Tokyo",    # Japan
    "America/New_York",  # USA (Eastern Time)
    "America/Los_Angeles",  # USA (Pacific Time)
    "Europe/London",  # UK
    "Europe/Paris",   # France
    "Europe/Berlin",  # Germany
    "Australia/Sydney",  # Australia
    "Africa/Cairo",   # Egypt
    "Canada/Pacific", # Canada (Pacific Time)
]

# Streamlit app title
st.title("Time Zone Converter")

# Multiselect widget to choose time zones
selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

# Display current time in selected time zones
st.subheader("Current Time in Selected Timezones")
for tz in selected_timezone:
    # Get current time in the selected time zone
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the time zone and current time
    st.write(f"**{tz}** : {current_time}")

# Time conversion section
st.subheader("Time Zone Converter")

# Time input widget to select a time
current_time = st.time_input("Select Time", value=datetime.now().time())

# Dropdown to select the "from" time zone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# Dropdown to select the "to" time zone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Button to trigger time conversion
if st.button("Convert Time"):
    # Combine the selected time with today's date and the "from" time zone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    
    # Convert the time to the "to" time zone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    # Display the converted time
    st.success(f"Converted Time in **{to_tz}** : {converted_time}")