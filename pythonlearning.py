import tkinter as tk

# === Create main window ===
root = tk.Tk()
root.title("Atharva's Python Learning App")
root.geometry("800x400")
root.config(bg="#121212")  # Dark background

# === Topic List: Each topic has a title and description ===
topics = [
    ("Programming", "A set of instructions to perform a task, programming is a collaboration between humans and computers,\nwhere humans create instructions (code) that computers can follow to perform tasks efficiently."),
    ("Coding", "Writing instructions in a programming language.\nThe process of writing, implementing, and testing instructions in a programming language to create software or applications."),
    ("Python", "Guido van Rossum created Python. He began developing the language in December 1989, and the first version, Python 0.9.0, was released on February 20, 1991."),
    ("Loops", "Loops in Python are used to repeat a block of code multiple times. There are two main types of loops: for loops and while loops."),
    ("Conditionals", "Conditional statements in Python are used to execute certain blocks of code based on specific conditions. These help control the program's flow.")
]

# Track which topic is currently shown
current_index = 0

# === FUNCTIONS ===

def show_topic(index):
    # Get the topic's title and content from the list using the provided index
    title, content = topics[index]

    # Update the title label with the topic name (e.g., "Loops", "Python")
    title_label.config(text=title)

    # Update the content label with the topic description text
    content_label.config(text=content)

    # Highlight the corresponding button for the current topic
    highlight(title)


# Go to next topic or show thank-you message if done
def next_topic():
    global current_index  # Let Python know we’re using the global variable, not a local copy

    current_index += 1  # Move to the next topic in the list

    # Check if we've reached past the last topic
    if current_index >= len(topics):
        learn_frame.pack_forget()  # Hide the learning screen
        thank_you_frame.pack(fill="both", expand=True)  # Show the final 'Thanks for Learning' screen
    else:
        show_topic(current_index)  # Otherwise, display the next topic

# Go to previous topic (loops back if at start)
def previous_topic():
    global current_index  # Use the global index tracker

    # Go one topic back. The % len(topics) ensures it loops around to the last topic if you go before the first.
    current_index = (current_index - 1) % len(topics)

    # Display the newly selected previous topic
    show_topic(current_index)


# Highlight active topic button
def highlight(active_title):
    # Loop through all topic buttons (title name and its button object)
    for name, btn in buttons.items():

        # If this button's title matches the currently active topic
        if name == active_title:
            # Highlight it: change to bright cyan bg with black text (active)
            btn.config(bg="#00ffd0", fg="black")
        else:
            # Otherwise, set it to default dark mode (inactive)
            btn.config(bg="#1e1e1e", fg="white")


# Switch from front page to learning page
def show_learning_page():
    # Hide the front welcome screen
    front_frame.pack_forget()

    # Show the learning content frame in full window
    learn_frame.pack(fill="both", expand=True)

    # Display the current topic (starting from index 0 or wherever the learner left off)
    show_topic(current_index)


# Go back to start from thank-you screen
def go_back_to_start():
    # Hide the thank you screen
    thank_you_frame.pack_forget()

    # Show the welcome/front screen again
    front_frame.pack(fill="both", expand=True)

    # Reset the topic index so the journey starts fresh
    global current_index
    current_index = 0


# === FRONT PAGE ===
front_frame = tk.Frame(root, bg="#121212")
front_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(front_frame, text="Welcome to\nAtharva's Python Learning App",
                         font=("Segoe UI", 22, "bold"), fg="#00ffd0", bg="#121212")
welcome_label.pack(pady=60)

start_btn = tk.Button(front_frame, text="Start Learning", font=("Segoe UI", 14, "bold"),
                      bg="#00ffd0", fg="black", padx=20, pady=10, command=show_learning_page)
start_btn.pack()

# === LEARNING PAGE ===
learn_frame = tk.Frame(root, bg="#121212")

# Buttons bar at top
button_frame = tk.Frame(learn_frame, bg="#121212")
button_frame.pack(pady=10)

buttons = {}  # Dictionary to store topic buttons for later highlighting

# Loop through each topic in the topics list
for topic in topics:
    title = topic[0]  # Extract the title 

    # Create a button for this topic
    btn = tk.Button(
        button_frame,                   # Parent container
        text=title,                     # Button label
        font=("Segoe UI", 10, "bold"),
        bg="#1e1e1e",
        fg="white",
        padx=10, pady=5,
        
    )
    btn.pack(side="left", padx=5)

    # Save the button reference to the buttons dictionary
    buttons[title] = btn

# Topic title
title_label = tk.Label(learn_frame, text="", font=("Segoe UI", 18, "bold"),
                       fg="#00ffd0", bg="#121212")
title_label.pack(pady=(20, 10))

# Topic description
content_label = tk.Label(learn_frame, text="", font=("Consolas", 13),
                         fg="white", bg="#121212", wraplength=700, justify="left")
content_label.pack(padx=20)

# Navigation buttons (Prev & Next)
nav_frame = tk.Frame(learn_frame, bg="#121212")
nav_frame.pack(pady=10)

prev_btn = tk.Button(nav_frame, text="Previous", font=("Segoe UI", 10, "bold"),
                     bg="#00ffd0", fg="black", command=previous_topic)
prev_btn.pack(side="left", padx=10)

next_btn = tk.Button(nav_frame, text="Next", font=("Segoe UI", 10, "bold"),
                     bg="#00ffd0", fg="black", command=next_topic)
next_btn.pack(side="left", padx=10)

# === THANK YOU PAGE ===
thank_you_frame = tk.Frame(root, bg="#121212")

thank_label = tk.Label(thank_you_frame, text="🎉 Thanks for Learning with Atharva! 🎉",
                       font=("Segoe UI", 22, "bold"), fg="#00ffd0", bg="#121212")
thank_label.pack(pady=80)

exit_btn = tk.Button(thank_you_frame, text="Exit", font=("Segoe UI", 12, "bold"),
                     bg="#00ffd0", fg="black", padx=20, pady=10, command=root.destroy)
exit_btn.pack(pady=10)

# === Start the GUI event loop ===
root.mainloop()
