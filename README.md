# ⌨️ Typing Speed Test Web App  
A lightweight, interactive **typing speed tester** built using **Python** and **Streamlit**.  
It measures **Words Per Minute (WPM)**, **accuracy**, **time taken**, and highlights mistakes  
to help users improve typing speed and precision.

---

## 🚀 Features

- ✔️ Random sentence generation  
- ✔️ Start-test timer  
- ✔️ Calculate **WPM**, **accuracy**, **time taken**  
- ✔️ Character-by-character mistake highlighting (green = correct, red = incorrect)  
- ✔️ "New Test" button to generate a fresh sentence  
- ✔️ Clean and simple Streamlit interface  
- ✔️ No HTML, CSS, or JavaScript required  

---

## 🛠️ Technologies Used

- **Python 3.x**  
- **Streamlit** (for UI)  
- **time** (for timer)  
- **random** (for sentence selection)

---

## 📁 Project Structure
.
├── typing_speed_app.py
├── README.md
└── requirements.txt

---

## 📥 Installation

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/typing-speed-test-app.git
cd typing-speed-test-app
2. Install dependencies

Create a file named requirements.txt with this content:
streamlit
Then install:
pip install -r requirements.txt
Run the Application
streamlit run typing_speed_app.py
This will launch the app in your browser at:
http://localhost:8501





How It Works

Click Start Test → timer begins

Type the displayed sentence in the text box

Click Calculate Results to view your:

WPM

Accuracy (%)

Time Taken

Mistake Highlighting

Click New Test for a fresh sentence


Formulae Used
Words Per Minute (WPM)
WPM = (words / time_taken) * 60


Accuracy (%)
accuracy = (correct_characters / total_characters) * 100

Example Output

Time Taken: 12.35 sec

Words Per Minute: 45.82

Accuracy: 87.50%

Mistake highlighting with green (correct) and red (incorrect) characters

📚 Future Enhancements

🔹 Live WPM counter (updates while typing)

🔹 Difficulty levels (Easy / Medium / Hard)

🔹 Countdown timer mode

🔹 Leaderboard system

🔹 Save results to a database

🔹 Additional typing passages

🔹 Graphs for user progress
