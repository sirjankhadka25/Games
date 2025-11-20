import streamlit as st
import random

st.title("✊ Rock ✋ Paper ✌ Scissors")

st.write("Play against the computer!")

choices = ["Rock", "Paper", "Scissors"]

# Let the player choose
user_choice = st.selectbox("Your choice:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"**Computer chose:** {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie! 🤝"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win! 🎉"
    else:
        result = "You lose! 😢"

    st.subheader(result)
