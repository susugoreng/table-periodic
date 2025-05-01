import streamlit as st
import math

st.set_page_config(page_title="Kalkulator pH & pOH", layout="centered")

# Title
st.title("⚗️ Games Kimia")

# Description
st.write("""
Aplikasi ini berguna untuk mempelajari tabel periodic unsur""")

import random

# Daftar unsur kimia: simbol dan nama
elements = [
    {"symbol": "H", "name": "hidrogen"},
    {"symbol": "He", "name": "helium"},
    {"symbol": "Li", "name": "litium"},
    {"symbol": "C", "name": "karbon"},
    {"symbol": "N", "name": "nitrogen"},
    {"symbol": "O", "name": "oksigen"},
    {"symbol": "F", "name": "fluorin"},
    {"symbol": "Na", "name": "natrium"},
    {"symbol": "Cl", "name": "klorin"},
    {"symbol": "K", "name": "kalium"}
]

def play_game():
    print("=== Game Tebak Unsur Kimia ===")
    print("Tebak nama unsur berdasarkan simbolnya.")
    score = 0

    for i in range(5):  # Main 5 ronde
        element = random.choice(elements)
        guess = input(f"\nApa nama unsur dengan simbol '{element['symbol']}'? ").lower().strip()

        if guess == element['name']:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah. Jawaban yang benar: {element['name'].capitalize()}")

    print(f"\nPermainan selesai. Skor akhir kamu: {score}/5")

if __name__ == "__main__":
    play_game()

