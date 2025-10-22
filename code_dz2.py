import tkinter as tk
from tkinter import PhotoImage


class UserProfileApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2.1 - User Profile GUI (Tkinter)")
        self.geometry("250x400")
        self.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        # Фон
        try:
            bg_img = PhotoImage(file="images/photo_2025-10-22_18-51-26.jpg")
            bg_label = tk.Label(self, image=bg_img)
            bg_label.image = bg_img
            bg_label.place(x=0, y=0)
        except Exception as e:
            print(f"Ошибка загрузки фона: {e}")

        # Фото профиля
        try:
            profile_img = PhotoImage(file="images/photo_2025-10-22_17-49-33.jpg")
            profile_label = tk.Label(self, image=profile_img)
            profile_label.image = profile_img
            profile_label.place(x=80, y=20)
        except Exception as e:
            print(f"Ошибка загрузки фото профиля: {e}")

        # Имя пользователя
        tk.Label(self, text="Иван Абрамович", font=("Arial", 20)).place(x=70, y=140)

        # Биография
        tk.Label(self, text="Биография", font=("Arial", 17)).place(x=15, y=175)
        tk.Label(
            self,
            text="Я филантроп",
            wraplength=220,
            justify="left"
        ).place(x=15, y=195)

        # Умения
        tk.Label(self, text="Умения", font=("Arial", 17)).place(x=15, y=240)
        tk.Label(self, text="Python / PHP \ SQL / JavaScript").place(x=15, y=260)

        # Опыт
        tk.Label(self, text="Опыт", font=("Arial", 17)).place(x=15, y=290)
        tk.Label(self, text="Миллионер").place(x=15, y=310)
        tk.Label(self, text="Март 2020 - настоящее время", font=("Arial", 10)).place(x=15, y=330)
        tk.Label(self, text="Таксист").place(x=15, y=350)
        tk.Label(self, text="Август 2017 - Декабрь 2025", font=("Arial", 10)).place(x=15, y=370)


if __name__ == "__main__":
    app = UserProfileApp()
    app.mainloop()
