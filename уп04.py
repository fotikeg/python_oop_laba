import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import scrolledtext
from datetime import datetime


class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Создание мероприятий")
        self.root.geometry("500x400")
        self.events = []

        title_label = tk.Label(root, text="Создать новое мероприятие", font=("Arial", 16))
        title_label.pack(pady=10)

        tk.Label(root, text="Название:").pack(anchor='w', padx=20)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(padx=20)

        tk.Label(root, text="Дата (ДД.ММ.ГГГГ):").pack(anchor='w', padx=20, pady=(10, 0))
        self.date_entry = tk.Entry(root, width=50)
        self.date_entry.pack(padx=20)

        tk.Label(root, text="Описание:").pack(anchor='w', padx=20, pady=(10, 0))
        self.desc_text = scrolledtext.ScrolledText(root, width=50, height=5)
        self.desc_text.pack(padx=20)

        add_button = tk.Button(root, text="Добавить мероприятие", command=self.add_event)
        add_button.pack(pady=10)

        tk.Label(root, text="Список мероприятий:", font=("Arial", 14)).pack(anchor='w', padx=20, pady=(10, 0))
        self.events_listbox = tk.Listbox(root, width=70, height=8)
        self.events_listbox.pack(padx=20, pady=(0, 10))

    def add_event(self):
        name = self.name_entry.get().strip()
        date_str = self.date_entry.get().strip()
        desc = self.desc_text.get("1.0", tk.END).strip()

        if not name or not date_str:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите название и дату мероприятия.")
            return

        try:
            date = datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            messagebox.showerror("Ошибка", "Дата должна быть в формате ДД.ММ.ГГГГ.")
            return

        event_text = f"{date.strftime('%d.%m.%Y')} - {name}"
        self.events.append({
            "name": name,
            "date": date,
            "desc": desc
        })

        self.events_listbox.insert(tk.END, event_text)

        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()