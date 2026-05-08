import tkinter as tk
from tkinter import scrolledtext
import threading

from core.llm import generate_response
from core.memory import Memory

# ✅ New ML + LIME imports
from core.emotion_model import predict
from core.explainer import explain
from core.storage import save_emotion
from core.emotion import get_timestamp

from core.visualization import show_emotion_graph

# Initialize memory
memory = Memory(max_history=6)


def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return

    chat.insert(tk.END, "You: " + user_text + "\n")
    chat.yview(tk.END)

    entry.delete(0, tk.END)

    # Run processing in background thread
    threading.Thread(target=process_response, args=(user_text,), daemon=True).start()


def process_response(user_text):
    # --- Emotion Prediction ---
    score = predict(user_text)
    timestamp = get_timestamp()
    save_emotion(timestamp, score)

    # --- LIME Explanation ---
    explanation = explain(user_text)

    # Show typing indicator
    chat.after(0, lambda: chat.insert(tk.END, "Bot is typing...\n"))
    chat.after(0, chat.yview, tk.END)

    # Context for LLM
    context = memory.get_context()

    prompt = f"""
    You are a human-like emotional assistant.

    Guidelines:
    - Understand emotions deeply (even mixed emotions)
    - Respond naturally like a real person
    - Do NOT repeat phrases
    - Keep responses short (2–4 sentences)
    - If user shares good news → celebrate
    - If user shares stress → acknowledge and support
    - If mixed emotions → address both sides

    Conversation so far:
    {context}

    User: {user_text}
    Bot:
    """

    reply = generate_response(prompt).strip()

    def update_ui():
        # Remove typing indicator
        chat.delete("end-2l", "end-1l")

        print("\n--- Emotion Analysis ---")
        print(f"Text: {user_text}")
        print(f"Score: {score}")
        print("Explanation:")
        for word, weight in explanation:
            print(f"  {word}: {round(weight, 2)}")
        print("------------------------\n")

        # --- Show Bot Reply ---
        chat.insert(tk.END, "Bot: " + reply + "\n\n")
        chat.yview(tk.END)

    chat.after(0, update_ui)

    # Save conversation memory
    memory.add(user_text, reply)


def start_ui():
    global chat, entry

    root = tk.Tk()
    root.title("AI Chatbot")

    # Chat display
    chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    chat.pack(padx=10, pady=10)

    # Input area
    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=5)

    entry = tk.Entry(input_frame, width=45)
    entry.pack(side=tk.LEFT, padx=(0, 10))

    send_btn = tk.Button(input_frame, text="Send", command=send_message)
    send_btn.pack(side=tk.LEFT)

    # Emotional Health button
    emotion_btn = tk.Button(
        root,
        text="Emotional Health",
        command=lambda: show_emotion_graph(root)
    )
    emotion_btn.pack(pady=5)

    # Enter key binding
    root.bind("<Return>", lambda event: send_message())

    root.mainloop()