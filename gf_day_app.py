import urllib.parse
import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="Happy Girlfriend's Day, My Little Annie Bunny!",
    page_icon="💖",
    layout="centered",
)

# 2. Romantic CSS Styling
st.markdown(
    """
    <style>
    /* Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #feada6 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Main Header Styling */
    h1 {
        color: #8b0032 !important;
        text-align: center;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.6);
    }
    
    h2, h3 {
        color: #a81c51 !important;
    }

    /* Warning / Info Box Styling */
    .stAlert {
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    /* Custom Cards for Questions */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(139, 0, 50, 0.15);
        backdrop-filter: blur(4px);
    }

    /* Buttons Styling */
    .stButton > button {
        background: linear-gradient(45deg, #ff4b2b, #ff416c);
        color: white !important;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        padding: 10px 25px;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Question Bank Definition
questions = [
    {
        "q": "1. When did you meet your boyfriend for the very first time?",
        "options": [
            "Select an option...",
            "December, 2023",
            "January, 2024",
            "March, 2024",
        ],
        "correct": "January, 2024",
        "hint": "Correct! That special day started it all. 🥰",
        "wrong": "Wrong! Memory check needed! 😉",
    },
    {
        "q": "2. What's your boyfriend's pseudo / nickname?",
        "options": [
            "Select an option...",
            "A. Eliezer Nlandu",
            "B. Eleazar Nlandu",
            "C. Bruce Wayne",
            "D. Elie",
        ],
        "correct": "C. Bruce Wayne",
        "hint": "Bingo! You remembered I'm Batman! 🦇",
        "wrong_special": {
            "A. Eliezer Nlandu": "Tricky! That's my government name, not my nickname! 🛑 Did you forget you're dating Batman? 🦇 Bruce Wayne is the answer!"
        },
        "wrong": "Nope! Remember, government name doesn't count! Think Gotham City... 🦇",
    },
    {
        "q": "3. Who is better at outside activities?",
        "options": [
            "Select an option...",
            "A. Me (Ann)",
            "B. You (Eliezer)",
            "C. Both of us",
        ],
        "correct": "A. Me (Ann)",
        "hint": "Correct! You know I hate going outside and would rather code! 🏠",
        "wrong": "Nice try, but you know I'd rather stay indoors!",
    },
    {
        "q": "4. How long have you been away from each other since the last time you met?",
        "options": [
            "Select an option...",
            "2 months",
            "Exactly 4 months",
            "6 months",
            "Too long!",
        ],
        "correct": "Exactly 4 months",
        "hint": "Correct! Counting down the days since March 31st! ✈️",
        "wrong": "Incorrect! Calculate from the last day of March 2026!",
    },
    {
        "q": "5. What's your favorite memory of us?",
        "options": [
            "Select an option...",
            "A. Before work outings",
            "B. Journey to Mombasa",
            "C. Evening town walks",
            "D. ETC",
            "E. All of the above",
        ],
        "correct": "E. All of the above",
        "hint": "Correct! Every single moment counts. 💕",
        "wrong": "Try again! Think bigger!",
    },
    {
        "q": "6. Who is the better cook?",
        "options": ["Select an option...", "Ann", "Elie", "Neither"],
        "correct": "Elie",
        "hint": "Correct! Chef Elie at your service! 🧑‍🍳",
        "wrong": "Wrong answer! I make the best meals!",
    },
    {
        "q": "7. What's your boyfriend's favorite fast food?",
        "options": [
            "Select an option...",
            "Burgers",
            "Pizza",
            "Tacos",
            "Fried Chicken",
        ],
        "correct": "Pizza",
        "hint": "Correct! Always pizza! 🍕",
        "wrong": "Nope! You should know my favorite food by now!",
    },
    {
        "q": "8. Complete the couple's catchphrase: 'Forever...'",
        "options": [
            "Select an option...",
            "Forever together",
            "Forever us ♾️",
            "Forever and ever",
        ],
        "correct": "Forever us ♾️",
        "hint": "Correct! Forever us ♾️❤️",
        "wrong": "Incorrect! Think of our phrase!",
    },
    {
        "q": "9. What's your boyfriend's favorite alcoholic drink?",
        "options": ["Select an option...", "Beer", "Whiskey", "Wine", "None"],
        "correct": "None",
        "hint": "Correct! Spot on—water and juice only because I don't drink! 🥤",
        "wrong": "Wrong! I don't drink alcohol at all!",
    },
    {
        "q": "10. Do you know what day it is today?",
        "options": [
            "Select an option...",
            "Girlfriend's Day ❤️",
            "Xmas Day 🎄",
            "Just a normal day 😴",
        ],
        "correct": "Girlfriend's Day ❤️",
        "hint": "HAPPY GIRLFRIEND'S DAY! 🎉💕",
        "wrong": "Check your calendar! 😉",
    },
]

# 4. Initialize State
if "step" not in st.session_state:
    st.session_state.step = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 5. Header Section
st.title("💖 The Ultimate Couple Quiz")
st.markdown(
    "<h3 style='text-align: center;'>For Ann Akinyi Ogwayo</h3>",
    unsafe_allow_html=True,
)
st.warning("⚠️ **Rules:** If you fail, you owe Eliezer 20,000 KES!")
st.caption("Designed with ❤️ by Eliezer Nlandu")

# 6. Step-By-Step Logic
current_step = st.session_state.step

if current_step < len(questions):
    # Progress Bar
    progress = (current_step + 1) / len(questions)
    st.progress(progress)
    st.write(f"**Question {current_step + 1} of {len(questions)}**")

    q_data = questions[current_step]

    # Pre-select previous choice if available
    default_val = st.session_state.answers.get(current_step, "Select an option...")
    default_index = (
        q_data["options"].index(default_val)
        if default_val in q_data["options"]
        else 0
    )

    user_choice = st.radio(
        q_data["q"],
        q_data["options"],
        index=default_index,
        key=f"q_{current_step}",
    )

    # Show instant feedback comments on screen as soon as an option is picked
    if user_choice != "Select an option...":
        if user_choice == q_data["correct"]:
            st.success(q_data["hint"])
        elif "wrong_special" in q_data and user_choice in q_data["wrong_special"]:
            st.warning(q_data["wrong_special"][user_choice])
        else:
            st.error(q_data["wrong"])

    col1, col2 = st.columns([1, 1])

    with col2:
        if st.button("Next Question ➡️"):
            if user_choice != "Select an option...":
                st.session_state.answers[current_step] = user_choice

                # Recalculate full score accurately before moving forward
                temp_score = 0
                for idx, ans in st.session_state.answers.items():
                    if ans == questions[idx]["correct"]:
                        temp_score += 1
                st.session_state.score = temp_score

                st.session_state.step += 1
                st.rerun()
            else:
                st.error("Please pick an answer first!")

    with col1:
        if current_step > 0:
            if st.button("⬅️ Previous"):
                st.session_state.step -= 1
                st.rerun()

# 7. Grand Finale Screen
else:
    st.balloons()
    st.header("🎉 Happy Girlfriend's Day, my Little Annie Bunny! 🐇 💕")

    st.write(f"### Your Final Score: {st.session_state.score}/10")

    if st.session_state.score < 7:
        st.error("👀 Looks like you owe Eliezer 20,000 KES! Pay up! 😉")
    else:
        st.success("🏆 Perfect Score! You know us so well!")

    # Photo Gallery
    st.write("---")
    st.subheader("📸 Our Moments")

    try:
        st.image(
            ["photo1.jpg", "photo2.jpg", "photo3.jpg"],
            caption=[
                "Our Favorite Memory",
                "Journey Memories",
                "Forever Us ♾️",
            ],
            use_container_width=True,
        )
    except Exception:
        st.info(
            "💡 Make sure photo1.jpg, photo2.jpg, and photo3.jpg are saved in your project folder!"
        )

    # WhatsApp Link
    message = f"Hey Eliezer! I finished the quiz! My score was {st.session_state.score}/10. Happy Girlfriend's Day! ❤️"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/?text={encoded_message}"

    st.markdown("---")
    st.markdown(
        f"<a href='{whatsapp_url}' target='_blank' style='text-decoration:none;'><button style='width:100%; height:50px; font-size:18px;'>👉 Send My Score to Eliezer on WhatsApp!</button></a>",
        unsafe_allow_html=True,
    )

    if st.button("🔄 Restart Quiz"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.answers = {}
        st.rerun()