import streamlit as st
import time
import random
# Sample sentences
SENTENCES = [
 "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and beginner friendly programming language.",
    "Typing speed tests are a fun way to improve productivity.",
    "Machine learning and data science are changing the world.",
    "Streamlit makes it easy to build web apps using pure Python.",
    "The quick brown fox jumps over the lazy dog.",
    "Jackdaws love my big sphinx of quartz.",
    "Glib jocks quiz nymph to vex dwarf.",
    "How vexing a fumble might jeopardize six big ducks.",
    "Quick zephyrs blow over the quaintly jumbled xylophone.",
    "Goals are the compass that guides you towards your dreams.",
    "Without them, you're like a ship adrift at sea, vulnerable to the whims of fate.",
    "Set goals that are meaningful to you, that resonate with your values and aspirations.",
    "Don't be afraid to dream big, but make sure your goals are also realistic and achievable.",
    "Break down large, intimidating goals into smaller, manageable steps.",
    "This will not only make them seem less daunting but also provide a sense of accomplishment as you complete each milestone.",
    "Remember, the journey of a thousand miles begins with a single step.",
]
st.set_page_config(page_title="Typing Speed Test", layout="centered")
st.title("⌨️ Typing Speed Test")
st.write("Improve your typing speed and accuracy!")
# Pick random sentence
if "sentence" not in st.session_state:
    st.session_state.sentence = random.choice(SENTENCES)
sentence = st.session_state.sentence
# Timer start value
if "start_time" not in st.session_state:
    st.session_state.start_time = None
st.subheader("Text to Type:")
st.info(sentence)
# BUTTON to start timer
if st.button("Start Test"):
    st.session_state.start_time = time.time()
typed_text = st.text_area("Start typing below:", height=150)
if st.button("Calculate Results"):
    if st.session_state.start_time is None:
        st.warning("Click **Start Test** before typing!")
    else:
        end_time = time.time()
        time_taken = end_time - st.session_state.start_time
        time_taken = max(time_taken, 1)
        # WPM
        words = len(typed_text.split())
        wpm = (words / time_taken) * 60
        # Accuracy
        correct_chars = sum(
            1 for i, c in enumerate(typed_text)
            if i < len(sentence) and c == sentence[i]
        )
        total_chars = len(sentence)
        accuracy = (correct_chars / total_chars) * 100
        st.subheader("📊 Results:")
        st.write(f"**Time Taken:** {time_taken:.2f} sec")
        st.write(f"**WPM:** {wpm:.2f}")
        st.write(f"**Accuracy:** {accuracy:.2f}%")
        # Highlight mistakes
        highlighted = ""
        for i in range(len(sentence)):
            if i < len(typed_text) and typed_text[i] == sentence[i]:
                highlighted += f"<span style='color:green;'>{sentence[i]}</span>"
            else:
                highlighted += f"<span style='color:red;'>{sentence[i]}</span>"
        st.subheader("🔍 Mistake Highlighting")
        st.markdown(f"<p style='font-size:18px'>{highlighted}</p>", unsafe_allow_html=True)
        st.session_state.start_time = None  # reset timer
# New test button
if st.button("New Test"):
    st.session_state.sentence = random.choice(SENTENCES)
    st.session_state.start_time = None
    st.rerun()
