import tkinter as tk

def on_button_click():
    # Get the text from the text box
    input_text = text_entry.get("1.0", tk.END) # .strip()

    # Changing words
    # .........................................................

    input_text = input_text.replace("she", "Trump")

    input_text = input_text.replace("She", "Trump")

    input_text = input_text.replace("her", "Trump's")

    input_text = input_text.replace("Her", "Trump's")

    input_text = input_text.replace("something", "shit")


    # Display the output in the output_label
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)  # Clear previous content
    output_text.insert(tk.END, "Output: " + input_text)
    output_text.config(state=tk.DISABLED)

    # Hide the text box
    text_entry.pack()

# Create the main window
root = tk.Tk()
root.title("Paul's Text Editor")
root.geometry("1800x1200") #setting original window size (resizable)

# Box for user to choose words to modify (choses which words to modify not what the mod is)

label_variable = tk.Label(root, text = "Word to replace")
label_variable.pack(padx=1, pady=3)

#label_variable1 = tk.Label(root, text = "replace")
#label_variable1.pack(padx=5, pady=3)

#modifying replacement words
mod_entry = tk.Text(root, height=2, width=10, wrap=tk.WORD)
mod_entry.pack(pady=5)

# Create a text entry widget
text_entry = tk.Text(root, height=20, width=100, wrap=tk.WORD)
text_entry.pack(pady=10)

# Create a button to trigger the action
button = tk.Button(root, text="Convert", command=on_button_click)
button.pack(pady=10)
##########################################
# Create a label for displaying the output
output_label = tk.Label(root, text="Output: ")
output_label.pack()
##########################################

output_text = tk.Text(root, height=5, width=100, wrap=tk.WORD)
output_text.insert(tk.END, "Output: ")
output_text.config(state=tk.DISABLED)  # Make it read-only
output_text.pack()


# Start the tkinter event loop
root.mainloop()
