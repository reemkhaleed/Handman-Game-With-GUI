import tkinter as tk
import random

def main():

    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("500x600")

    words = ['python', 'hangman', 'developer', 'GitHub', 'Tkinter', 'programming']
    state = {
        "word": random.choice(words),
        "guessed_letters": [],
        "tries": 0
    }

    word_display = tk.StringVar()
    status_text = tk.StringVar()

    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack(pady=10)


    def draw_gallows():
        canvas.delete("all")
        canvas.create_line(50, 250, 250, 250) 
        canvas.create_line(100, 250, 100, 50)  
        canvas.create_line(100, 50, 200, 50)   
        canvas.create_line(200, 50, 200, 80)   

    def draw_hangman(tries):
        if tries >= 1:  
            canvas.create_oval(175, 80, 225, 130)
        if tries >= 2:  
            canvas.create_line(200, 130, 200, 190)
        if tries >= 3:  
            canvas.create_line(200, 140, 170, 170)
        if tries >= 4:  
            canvas.create_line(200, 140, 230, 170)
        if tries >= 5:  
            canvas.create_line(200, 190, 170, 230)
        if tries >= 6:  
            canvas.create_line(200, 190, 230, 230)

    
    def update_word_display():
        display = ' '.join([letter if letter in state["guessed_letters"] else '_' for letter in state["word"]])
        word_display.set(display)

    
    def end_game():
        entry.config(state='disabled')
        button.config(state='disabled')
        restart_btn.pack(pady=10)

    
    def restart_game():
        state["word"] = random.choice(words)
        state["guessed_letters"] = []
        state["tries"] = 0
        status_text.set("")
        entry.config(state='normal')
        button.config(state='normal')
        restart_btn.pack_forget()
        draw_gallows()
        update_word_display()

    
    def guess_letter():
        guess = entry.get().lower()
        entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            status_text.set("❗ Enter a single letter.")
            return

        if guess in state["guessed_letters"]:
            status_text.set("⛔ Already guessed.")
            return

        state["guessed_letters"].append(guess)

        if guess in state["word"]:
            status_text.set("✅ Correct!")
        else:
            state["tries"] += 1
            status_text.set("❌ Wrong!")
            draw_hangman(state["tries"])

        update_word_display()

        if all(letter in state["guessed_letters"] for letter in state["word"]):
            status_text.set(f"🎉 You won! The word was: {state['word']}")
            end_game()
        elif state["tries"] >= 6:
            word_display.set(state["word"])
            status_text.set(f"💀 Game over! The word was: {state['word']}")
            end_game()

    
    tk.Label(root, text="Hangman", font=("Arial", 24)).pack()
    tk.Label(root, textvariable=word_display, font=("Arial", 20)).pack(pady=10)
    tk.Label(root, textvariable=status_text, font=("Arial", 14)).pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 14), width=5, justify='center')
    entry.pack()

    button = tk.Button(root, text="Guess", font=("Arial", 14), command=guess_letter)
    button.pack(pady=10)

    restart_btn = tk.Button(root, text="🔁 Restart", font=("Arial", 14), command=restart_game)

    
    restart_game()
    root.mainloop()

if __name__ == '__main__':
    main()
