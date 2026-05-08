# AI-Emotional-Chatbot-XAI
AI Emotional Distress Detection Chatbot using Ollama, Machine Learning, and Explainable AI (LIME)

A local AI chatbot built with Python, Tkinter, and Ollama that:

* Chats naturally using a local LLM
* Detects user emotion using an ML model
* Explains predictions using LIME (Explainable AI)
* Tracks emotional trends over time

---

## Features

* Human-like conversation (via local LLM)
* Emotion detection (-2 to +2 scale)
* Explainable AI (LIME explanations in terminal)
* Emotional health tracking (graph visualization)
* Clean Tkinter-based UI

---

## Project Structure

```
ChatBot/
│
├── main.py
├── requirements.txt
│
├── core/
│   ├── emotion_model.py
│   ├── explainer.py
│   ├── storage.py
│   ├── visualization.py
│   ├── llm.py
│   ├── memory.py
│   └── emotion.py
│
├── ui/
│   └── chat_ui.py
│
└── data/
    └── emotions.csv (auto-created)
```

---

##  Setup Instructions

###  1. Clone or Download the Project

```bash
git clone <your-repo-url>
cd ChatBot
```

---

### 2. Install Python Dependencies

Make sure Python 3.10+ is installed.

```bash
pip install -r requirements.txt
```

---

###  3. Install Ollama (Local LLM)

This project uses a local LLM via Ollama.

#### ▶ Windows (PowerShell)

```powershell
winget install Ollama.Ollama
```

OR:

```powershell
Invoke-WebRequest https://ollama.com/install.ps1 -OutFile install.ps1
.\install.ps1
```

---

###  4. Download the Model

Run the following command to download the model (one-time setup):

```bash
ollama run llama3
```

⏳ This may take a few minutes (~4–5GB download)

---

###  5. Run the Chatbot

```bash
python main.py
```

---

##  Usage

* Type messages in the UI
* Chat naturally with the AI
* Emotion scores + explanations appear in the terminal
* Click **"Emotional Health"** to view your mood trend graph

---

##  Emotion Scale

| Score | Meaning       |
| ----- | ------------- |
| +2    | Very Positive |
| +1    | Positive      |
|  0    | Neutral       |
| -1    | Negative      |
| -2    | Very Negative |

---

##  Explainable AI

This project uses LIME to explain:

* Why a certain emotion score was assigned
* Which words influenced the prediction

Example (terminal output):

```
--- Emotion Analysis ---
Text: I feel stressed and tired
Score: -1
Explanation:
  stressed: -0.65
  tired: -0.32
------------------------
```

---

##  Notes

* Ensure Ollama is running at:

  ```
  http://localhost:11434
  ```
* First response may be slow due to model loading
* Emotion model is basic and can be improved with more data

---

##  Acknowledgements

* Ollama for local LLM support
* LIME for explainability
* Scikit-learn for ML model
* Tkinter for UI
