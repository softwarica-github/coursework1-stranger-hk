import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports():
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid port range. Please enter valid numbers.")
        return

    result_text.delete(1.0, tk.END)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_domain = website_entry.get().lower()
    target_ip = socket.gethostbyname(f"www.{target_domain}.com")

    for port in range(start_port, end_port + 1):
        res = s.connect_ex((target_ip, port))
        if res == 0:
            result_text.insert(tk.END, f"Port {port} is open\n")
        else:
            result_text.insert(tk.END, f"Port {port} is closed\n")

def on_exit():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Port Scanner")

website_label = tk.Label(root, text="Enter a website name:")
website_label.pack()

website_entry = tk.Entry(root)
website_entry.pack()

start_port_label = tk.Label(root, text="Enter starting point of port:")
start_port_label.pack()

start_port_entry = tk.Entry(root)
start_port_entry.pack()

end_port_label = tk.Label(root, text="Enter ending point of port:")
end_port_label.pack()

end_port_entry = tk.Entry(root)
end_port_entry.pack()

scan_button = tk.Button(root, text="Scan Ports", command=scan_ports)
scan_button.pack()

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

root.mainloop()
