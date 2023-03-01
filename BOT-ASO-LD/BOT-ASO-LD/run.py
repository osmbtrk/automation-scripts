import tkinter
import customtkinter
import subprocess

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x300")
app.title("LD-bot.py")


def button_callback():
    subprocess.call(['python', 'conn.py'])


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text = "run ASO-bot", justify=tkinter.LEFT)
label_1.pack(pady=30, padx=30)


button_1 = customtkinter.CTkButton(master=frame_1,text = "Button", command=button_callback)
button_1.pack(pady=20, padx=20)






app.mainloop()
