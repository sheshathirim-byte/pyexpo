import streamlit as st
import time
import random
from datetime import datetime


st.set_page_config(
    page_title="Smart Helmet with Fatigue Detection",
    page_icon="🪖",
    layout="centered"
)

st.title("🪖 Smart Helmet with Fatigue Detection")
st.markdown("""
This project simulates the **frontend alert system** of a smart helmet.
It detects **driver fatigue** and activates **buzzer and LED alerts**.

**Technology Used:**
- Python
- Streamlit (HTML-based UI)
- Simulation logic (can be connected to sensors later)
""")

st.divider()

st.sidebar.header("⚙ Control Panel")

mode = st.sidebar.radio(
    "Select Detection Mode",
    ("Automatic Mode", "Manual Mode")
)

refresh_time = st.sidebar.slider(
    "Refresh Time (seconds)",
    min_value=1,
    max_value=5,
    value=2
)

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Project: PyExpo")
st.sidebar.write("🧠 Topic: Smart Helmet")

if "buzzer" not in st.session_state:
    st.session_state.buzzer = False

if "led" not in st.session_state:
    st.session_state.led = False

if "status" not in st.session_state:
    st.session_state.status = "Normal"

if "log" not in st.session_state:
    st.session_state.log = []


def fatigue_check(signal):
    current_time = datetime.now().strftime("%H:%M:%S")

    if signal == 1:
        st.session_state.buzzer = True
        st.session_state.led = True
        st.session_state.status = "⚠ FATIGUE DETECTED"

        st.session_state.log.append(
            f"[{current_time}] Fatigue detected – Alert ON"
        )
    else:
        st.session_state.buzzer = False
        st.session_state.led = False
        st.session_state.status = "✅ NORMAL"

        st.session_state.log.append(
            f"[{current_time}] Normal condition"
        )


st.subheader("🚦 Helmet Status")

status_color = "red" if st.session_state.status.startswith("⚠") else "green"

st.markdown(
    f"<h3 style='color:{status_color};'>{st.session_state.status}</h3>",
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔊 Buzzer")
    if st.session_state.buzzer:
        st.success("BUZZER ON")
    else:
        st.info("Buzzer OFF")

with col2:
    st.markdown("### 💡 LED")
    if st.session_state.led:
        st.success("LED ON")
    else:
        st.info("LED OFF")

st.divider()


if mode == "Automatic Mode":
    st.subheader("🤖 Automatic Fatigue Detection")

    fatigue_signal = random.choice([0, 1])
    fatigue_check(fatigue_signal)

    st.write("System is automatically checking fatigue...")
    time.sleep(refresh_time)
    st.experimental_rerun()

else:
    st.subheader("🧍 Manual Fatigue Control")

    user_input = st.radio(
        "Select Helmet Condition",
        ("Normal", "Fatigue Detected")
    )

    if st.button("Update Status"):
        signal = 1 if user_input == "Fatigue Detected" else 0
        fatigue_check(signal)

st.divider()
st.subheader("📜 Activity Log")

if st.session_state.log:
    for entry in st.session_state.log[-10:]:
        st.write(entry)
else:
    st.write("No activity recorded yet.")


st.divider()
st.markdown("""
### 📌 Project Explanation (For Judges)
- This is the **frontend module** of the smart helmet
- Fatigue signal comes from backend / sensors
- When fatigue is detected:
  - Buzzer activates
  - LED turns ON
- Can be integrated with:
  - Arduino
  - Eye blink sensor
  - Camera-based AI
""")
