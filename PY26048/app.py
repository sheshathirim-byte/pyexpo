import streamlit as st
import random
import time

st.set_page_config(page_title="Smart Helmet Fatigue Detection", page_icon="🪖")
st.title("🪖 Smart Helmet Fatigue Detection System")
st.write("Simulation of Smart Helmet Frontend alerts")

# Sidebar controls
st.sidebar.header("Simulation Settings")
auto_mode = st.sidebar.checkbox("Automatic Fatigue Simulation", value=True)
manual_mode = st.sidebar.checkbox("Manual Fatigue Input", value=False)

# Session state for buzzer, LED, status
if "buzzer" not in st.session_state:
    st.session_state.buzzer = False
if "led" not in st.session_state:
    st.session_state.led = False
if "status" not in st.session_state:
    st.session_state.status = "Normal"

# Check fatigue function
def check_fatigue(fatigue_signal):
    if fatigue_signal:
        st.session_state.buzzer = True
        st.session_state.led = True
        st.session_state.status = "⚠ Fatigue Detected!"
    else:
        st.session_state.buzzer = False
        st.session_state.led = False
        st.session_state.status = "✅ Normal"

# Simulation
st.subheader("Helmet Status")

if auto_mode:
    fatigue_signal = random.choice([0, 1])
    check_fatigue(fatigue_signal)
    st.write("Automatic Mode Active")
else:
    st.write("Automatic Mode Off")

if manual_mode:
    user_input = st.radio("Manual Fatigue Input:", ("Normal", "Fatigue"))
    fatigue_signal = 1 if user_input == "Fatigue" else 0
    check_fatigue(fatigue_signal)

# Display status
st.markdown(f"### Status: {st.session_state.status}")
st.markdown(f"Buzzer: {'ON 🔊' if st.session_state.buzzer else 'OFF'}")
st.markdown(f"LED: {'ON 💡' if st.session_state.led else 'OFF'}")

# Auto-refresh for auto mode
if auto_mode:
    time.sleep(2)
    st.experimental_rerun()
