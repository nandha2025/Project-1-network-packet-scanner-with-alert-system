import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import sniffer_core
from sniffer_core import start_sniffer, stop_sniffer


class SnifferApp:
    def _init_(self, root):
        self.root = root
        root.title("Simple IDS - Packet Sniffer")

        self.text = ScrolledText(root, width=100, height=30)
        self.text.pack(fill="both", expand=True)

        button_frame = tk.Frame(root)
        button_frame.pack(fill="x")

        tk.Button(
            button_frame,
            text="Start Sniffing",
            command=self.start_sniffing,
        ).pack(side="left", padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Stop Sniffing",
            command=self.stop_sniffing,
        ).pack(side="left", padx=5, pady=5)

        def gui_log(msg):
            self.text.insert("end", msg + "")
            self.text.see("end")

        sniffer_core.log_callback = gui_log

    def start_sniffing(self):
        t = threading.Thread(target=start_sniffer, daemon=True)
        t.start()

    def stop_sniffing(self):
        stop_sniffer()


if __name__ == "__main__":
    root = tk.Tk()
    app = SnifferApp(root)
    root.mainloop()
