import tkinter as tk
import requests
from tkinter import messagebox

def search_word():
    word = word_entry.get().strip()   # Get the word entered by the user, remove trailing spaces

    if not word:
        # Show warning if input is empty
        messagebox.showwarning("Input Error", "Please enter a word.")
        return

    # URL for fetching dictionary data from the Free Dictionary API
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    try:
        # Send request to the API
        response = requests.get(url)
        data = response.json()   # Parse response JSON

        # Handle case if the word is not found in the dictionary
        if isinstance(data, dict) and data.get("title") == "No Definitions Found":
            messagebox.showerror("Not Found", f"No definitions found for '{word}'.")
            return

        # Clear previous search result from the result_box
        result_box.delete("1.0", tk.END)

        # Extract the list of meanings
        meanings = data[0]["meanings"]
        result_box.insert(tk.END, f"Word: {word}\n\n")  # Display the searched word

        # Loop through each meaning (part of speech + definitions)
        for meaning in meanings:
            part = meaning["partOfSpeech"]            # e.g., noun, verb, etc.
            defs = meaning["definitions"]             # List of definitions for that part of speech

            for d in defs:
                definition = d["definition"]          # Main definition text
                example = d.get("example", "")        # Example usage, if available

                # Insert definition and optional example into the text box
                result_box.insert(tk.END, f"{part}: {definition}\n")
                if example:
                    result_box.insert(tk.END, f"   e.g. {example}\n")
                result_box.insert(tk.END, "\n")       # Line break between definitions

    except Exception as e:
        # Catch and show any unexpected errors (like no internet)
        messagebox.showerror("Error", str(e))

bg_color = "#1e1e1e"       # Background color of the main window
fg_color = "#ffffff"       # Text color (white)
entry_bg = "#2d2d2d"       # Background color for Entry and Text boxes
button_bg = "#3a3a3a"      # Background color for the button

root = tk.Tk()                         # Create main application window
root.title("QuickWord - Dictionary App")  # Window title
root.geometry("500x500")              # Window size
root.config(bg=bg_color)              # Apply dark background

# Label prompting user to enter a word
tk.Label(root, text="Enter Word:", font=("Arial", 14), bg=bg_color, fg=fg_color).pack(pady=10)

# Entry widget where user types the word
word_entry = tk.Entry(
    root, font=("Arial", 14), width=30,
    bg=entry_bg, fg=fg_color, insertbackground=fg_color  # insertbackground changes cursor color
)
word_entry.pack()

# Button to trigger the search_word() function
tk.Button(
    root, text="Search", font=("Arial", 12), command=search_word,
    bg=button_bg, fg=fg_color,
    activebackground="#444", activeforeground=fg_color  # Color when button is clicked
).pack(pady=10)

# Text box where meanings and examples are displayed
result_box = tk.Text(
    root, wrap="word", font=("Arial", 12), height=20, width=60,
    bg=entry_bg, fg=fg_color, insertbackground=fg_color  # insertbackground makes typing cursor visible
)
result_box.pack(padx=10, pady=10)

# Run the Tkinter main loop — keeps the window open and responsive
root.mainloop()
