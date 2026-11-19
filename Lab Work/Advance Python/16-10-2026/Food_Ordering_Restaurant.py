
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os
import tempfile
import sys
import subprocess

# =====================================================
# VEGGIE BLISS - COMPLETE RESTAURANT ORDERING SYSTEM
# Python + Tkinter | Windows bill printing supported
# =====================================================

root = tk.Tk()
root.title("Veggie Bliss - Restaurant Ordering System")
root.geometry("1250x800")
root.minsize(1000, 650)
root.configure(bg="#f3f5f4")

# ---------------- COLORS ----------------
DARK = "#17352b"
GREEN = "#198754"
BLUE = "#0d6efd"
WHITE = "#ffffff"
BG = "#f3f5f4"

# ---------------- COMPLETE FOOD MENU ----------------
menu = {
    "Gujarati Thali & Full Course": {
        "Regular Gujarati Thali": 180,
        "Special Gujarati Thali": 250,
        "Kathiyawadi Thali": 220,
        "Unlimited Gujarati Thali": 300,
        "Jain Gujarati Thali": 230,
        "Mini Gujarati Thali": 130,
        "Executive Gujarati Thali": 350,
        "Festival Special Thali": 400,
        "Gujarati Farsan Thali": 150
    },
    "Kathiyawadi Special": {
        "Ringan No Olo": 140,
        "Sev Tameta Nu Shaak": 110,
        "Lasaniya Bataka": 130,
        "Kathiyawadi Dahi Tikhari": 120,
        "Ringan Bataka Nu Shaak": 130,
        "Bharela Ringan": 150,
        "Bharela Marcha": 90,
        "Lasan Chutney": 30,
        "Bajra Rotla": 35,
        "Makai Rotla": 40,
        "Rotla with Ghee and Jaggery": 70
    },
    "Gujarati Shaak, Dal & Kadhi": {
        "Gujarati Undhiyu": 180,
        "Gujarati Dal": 90,
        "Gujarati Kadhi": 80,
        "Gujarati Tuvar Dal": 100,
        "Bhindi Masala": 130,
        "Aloo Matar": 110,
        "Mix Veg Shaak": 130,
        "Tindora Bataka": 120,
        "Chana Masala": 140,
        "Vaghareli Khichdi": 120
    },
    "Farsan & Gujarati Snacks": {
        "Khaman Dhokla": 60,
        "Nylon Khaman": 60,
        "Khandvi": 70,
        "Patra": 60,
        "Fafda": 70,
        "Gujarati Kachori": 40,
        "Lilva Kachori": 50,
        "Methi Gota": 60,
        "Handvo": 80,
        "Dabeli": 35,
        "Sev Khamani": 60,
        "Gujarati Samosa": 30,
        "Dalwada": 60,
        "Khichu": 50
    },
    "Punjabi & North Indian": {
        "Paneer Butter Masala": 220,
        "Paneer Tikka Masala": 240,
        "Kadai Paneer": 230,
        "Palak Paneer": 210,
        "Shahi Paneer": 250,
        "Dal Makhani": 190,
        "Dal Fry": 140,
        "Chole Masala": 150,
        "Malai Kofta": 220,
        "Veg Kolhapuri": 190,
        "Veg Handi": 200,
        "Paneer Bhurji": 210
    },
    "Roti, Paratha & Bread": {
        "Gujarati Rotli": 15,
        "Phulka": 15,
        "Tawa Roti": 15,
        "Butter Roti": 20,
        "Thepla": 25,
        "Methi Thepla": 30,
        "Plain Paratha": 40,
        "Aloo Paratha": 70,
        "Butter Naan": 45,
        "Garlic Naan": 60,
        "Tandoori Roti": 25,
        "Missi Roti": 40
    },
    "Rice, Khichdi & Biryani": {
        "Steamed Rice": 90,
        "Jeera Rice": 120,
        "Veg Pulao": 150,
        "Veg Biryani": 160,
        "Paneer Biryani": 200,
        "Gujarati Khichdi": 100,
        "Bajra Khichdi": 130,
        "Masala Khichdi": 130,
        "Dal Khichdi": 140,
        "Kadhi Khichdi Combo": 160,
        "Curd Rice": 120,
        "Vagharelo Bhaat": 120
    },
    "Fast Food & South Indian": {
        "Pav Bhaji": 120,
        "Vada Pav": 35,
        "Masala Dosa": 100,
        "Mysore Masala Dosa": 140,
        "Idli Sambhar": 80,
        "Medu Vada": 80,
        "Uttapam": 120,
        "Veg Sandwich": 80,
        "Cheese Sandwich": 110,
        "Veg Burger": 90,
        "Margherita Pizza": 180,
        "French Fries": 80,
        "Veg Hakka Noodles": 140,
        "Veg Manchurian": 150
    },
    "Sweets & Desserts": {
        "Gujarati Shrikhand": 80,
        "Kesar Shrikhand": 100,
        "Basundi": 100,
        "Gulab Jamun": 60,
        "Jalebi": 60,
        "Mohanthal": 70,
        "Sukhdi": 50,
        "Kaju Katli": 120,
        "Rasgulla": 60,
        "Gajar Halwa": 100,
        "Kulfi": 60,
        "Ice Cream": 80
    },
    "Beverages & Extras": {
        "Chaas": 25,
        "Masala Chaas": 35,
        "Sweet Lassi": 60,
        "Mango Lassi": 80,
        "Fresh Lime Soda": 50,
        "Nimbu Pani": 30,
        "Masala Chai": 20,
        "Filter Coffee": 40,
        "Cold Coffee": 80,
        "Mango Juice": 60,
        "Mineral Water": 20,
        "Papad": 20,
        "Pickle": 15,
        "Extra Chutney": 20
    }
}

# Cart stores: food name -> quantity
cart = {}

# Keep the latest generated bill available for printing
last_bill_text = ""
last_bill_path = None

# ---------------- HEADER ----------------
header = tk.Frame(root, bg=DARK, height=82)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="VEGGIE BLISS",
    font=("Arial", 25, "bold"),
    fg=WHITE,
    bg=DARK
).pack(pady=(7, 0))

tk.Label(
    header,
    text="Gujarati | Kathiyawadi | Punjabi | Pure Vegetarian",
    font=("Arial", 11),
    fg="#d6eadc",
    bg=DARK
).pack()

# ---------------- CUSTOMER DETAILS ----------------
customer_frame = tk.LabelFrame(
    root,
    text=" Customer Details ",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    padx=10,
    pady=8
)
customer_frame.pack(fill="x", padx=12, pady=8)

tk.Label(customer_frame, text="Name:", bg=WHITE).grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
name_entry = ttk.Entry(customer_frame, width=22)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(customer_frame, text="Mobile:", bg=WHITE).grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
mobile_entry = ttk.Entry(customer_frame, width=16)
mobile_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(customer_frame, text="Address:", bg=WHITE).grid(
    row=0, column=4, padx=5, pady=5, sticky="w"
)
address_entry = ttk.Entry(customer_frame)
address_entry.grid(row=0, column=5, padx=5, pady=5, sticky="ew")
customer_frame.columnconfigure(5, weight=1)

# ---------------- MAIN LAYOUT ----------------
main_frame = tk.Frame(root, bg=BG)
main_frame.pack(fill="both", expand=True, padx=12, pady=4)

# ================= MENU PANEL =================
menu_frame = tk.LabelFrame(
    main_frame,
    text=" Restaurant Menu ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    padx=9,
    pady=8
)
menu_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

tk.Label(
    menu_frame,
    text="Food Category",
    bg=WHITE,
    font=("Arial", 10, "bold")
).pack(anchor="w")

category_var = tk.StringVar(value="All Categories")
category_combo = ttk.Combobox(
    menu_frame,
    textvariable=category_var,
    values=["All Categories"] + list(menu.keys()),
    state="readonly"
)
category_combo.pack(fill="x", pady=4)

tk.Label(
    menu_frame,
    text="Search Food",
    bg=WHITE,
    font=("Arial", 10, "bold")
).pack(anchor="w")

search_var = tk.StringVar()
search_entry = ttk.Entry(menu_frame, textvariable=search_var)
search_entry.pack(fill="x", pady=4)

food_columns = ("food", "category", "price")
food_tree = ttk.Treeview(
    menu_frame,
    columns=food_columns,
    show="headings",
    height=13,
    selectmode="browse"
)

food_tree.heading("food", text="Food Item")
food_tree.heading("category", text="Category")
food_tree.heading("price", text="Price (Rs.)")

food_tree.column("food", width=175)
food_tree.column("category", width=140)
food_tree.column("price", width=75, anchor="e")

food_scroll = ttk.Scrollbar(
    menu_frame,
    orient="vertical",
    command=food_tree.yview
)
food_tree.configure(yscrollcommand=food_scroll.set)

food_scroll.pack(side="right", fill="y")
food_tree.pack(fill="both", expand=True, pady=5)

quantity_frame = tk.Frame(menu_frame, bg=WHITE)
quantity_frame.pack(fill="x", pady=5)

tk.Label(
    quantity_frame,
    text="Quantity:",
    bg=WHITE,
    font=("Arial", 10, "bold")
).pack(side="left", padx=5)

quantity_spin = ttk.Spinbox(
    quantity_frame,
    from_=1,
    to=99,
    width=7
)
quantity_spin.set(1)
quantity_spin.pack(side="left", padx=5)

# ================= CART PANEL =================
cart_frame = tk.LabelFrame(
    main_frame,
    text=" Shopping Cart & Bill ",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    padx=9,
    pady=8,
    width=480
)
cart_frame.pack(side="right", fill="both", expand=True)
cart_frame.pack_propagate(False)

cart_columns = ("food", "qty", "price", "amount")
cart_tree = ttk.Treeview(
    cart_frame,
    columns=cart_columns,
    show="headings",
    height=11,
    selectmode="browse"
)

cart_tree.heading("food", text="Food Item")
cart_tree.heading("qty", text="Qty")
cart_tree.heading("price", text="Price")
cart_tree.heading("amount", text="Amount")

cart_tree.column("food", width=160)
cart_tree.column("qty", width=40, anchor="center")
cart_tree.column("price", width=70, anchor="e")
cart_tree.column("amount", width=85, anchor="e")

cart_tree.pack(fill="both", expand=True, pady=4)

# ---------------- BILL TOTALS ----------------
bill_frame = tk.Frame(
    cart_frame,
    bg="#dff3e6",
    padx=10,
    pady=6
)
bill_frame.pack(fill="x", pady=6)

subtotal_var = tk.StringVar(value="Rs. 0.00")
gst_var = tk.StringVar(value="Rs. 0.00")
total_var = tk.StringVar(value="Rs. 0.00")

def bill_row(label, variable, bold=False):
    row = tk.Frame(bill_frame, bg="#dff3e6")
    row.pack(fill="x", pady=2)

    tk.Label(
        row,
        text=label,
        bg="#dff3e6",
        font=("Arial", 10, "bold" if bold else "normal")
    ).pack(side="left")

    tk.Label(
        row,
        textvariable=variable,
        bg="#dff3e6",
        font=("Arial", 10, "bold" if bold else "normal")
    ).pack(side="right")

bill_row("Subtotal:", subtotal_var)
bill_row("GST (5% estimate):", gst_var)
bill_row("GRAND TOTAL:", total_var, True)

# ---------------- MENU FUNCTIONS ----------------
def get_all_foods():
    result = []
    for category, items in menu.items():
        for food, price in items.items():
            result.append((food, category, price))
    return result

def find_price(food):
    for items in menu.values():
        if food in items:
            return items[food]
    return 0

def show_menu(event=None):
    for item in food_tree.get_children():
        food_tree.delete(item)

    selected_category = category_var.get()
    search_text = search_var.get().strip().lower()

    for food, category, price in get_all_foods():
        if (
            selected_category != "All Categories"
            and category != selected_category
        ):
            continue

        if search_text and search_text not in food.lower():
            continue

        food_tree.insert(
            "",
            "end",
            values=(food, category, f"{price:.2f}")
        )

# ---------------- BILL CALCULATION ----------------
def calculate_bill():
    subtotal = sum(
        find_price(food) * quantity
        for food, quantity in cart.items()
    )
    gst = subtotal * 0.05
    total = subtotal + gst
    return subtotal, gst, total

def update_bill():
    subtotal, gst, total = calculate_bill()

    subtotal_var.set(f"Rs. {subtotal:.2f}")
    gst_var.set(f"Rs. {gst:.2f}")
    total_var.set(f"Rs. {total:.2f}")

    return subtotal, gst, total

def update_cart():
    for item in cart_tree.get_children():
        cart_tree.delete(item)

    for food, quantity in cart.items():
        price = find_price(food)
        amount = price * quantity

        cart_tree.insert(
            "",
            "end",
            values=(
                food,
                quantity,
                f"{price:.2f}",
                f"{amount:.2f}"
            )
        )

    update_bill()

# ---------------- ADD FOOD ----------------
def add_to_cart():
    selected = food_tree.selection()

    if not selected:
        messagebox.showwarning(
            "Select Food",
            "Please select a food item from the menu."
        )
        return

    try:
        quantity = int(quantity_spin.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Quantity",
            "Please enter a valid quantity."
        )
        return

    if quantity < 1 or quantity > 99:
        messagebox.showwarning(
            "Invalid Quantity",
            "Quantity must be between 1 and 99."
        )
        return

    values = food_tree.item(selected[0], "values")
    food = values[0]

    cart[food] = cart.get(food, 0) + quantity
    update_cart()

# ---------------- REMOVE FOOD ----------------
def remove_item():
    selected = cart_tree.selection()

    if not selected:
        messagebox.showwarning(
            "Select Item",
            "Please select an item in the cart."
        )
        return

    food = cart_tree.item(selected[0], "values")[0]
    cart.pop(food, None)
    update_cart()

def decrease_quantity():
    selected = cart_tree.selection()

    if not selected:
        messagebox.showwarning(
            "Select Item",
            "Please select a cart item."
        )
        return

    food = cart_tree.item(selected[0], "values")[0]

    if food in cart:
        cart[food] -= 1

        if cart[food] <= 0:
            del cart[food]

    update_cart()

def clear_cart():
    if not cart:
        messagebox.showinfo("Cart", "Your cart is already empty.")
        return

    if messagebox.askyesno(
        "Clear Cart",
        "Do you want to remove all items?"
    ):
        cart.clear()
        update_cart()

# ---------------- CUSTOMER VALIDATION ----------------
def validate_customer():
    name = name_entry.get().strip()
    mobile = mobile_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not mobile or not address:
        messagebox.showwarning(
            "Customer Details",
            "Please enter name, mobile number and address."
        )
        return None

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showwarning(
            "Invalid Mobile",
            "Please enter a valid 10-digit mobile number."
        )
        return None

    if not cart:
        messagebox.showwarning(
            "Empty Cart",
            "Please add food items before continuing."
        )
        return None

    return name, mobile, address

# ---------------- GENERATE FULL BILL ----------------
def generate_bill_text():
    global last_bill_text

    customer = validate_customer()
    if customer is None:
        return None

    name, mobile, address = customer
    subtotal, gst, total = calculate_bill()

    order_id = datetime.now().strftime("%Y%m%d%H%M%S")
    order_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    lines = [
        "=" * 54,
        "                    VEGGIE BLISS",
        "              VEGETARIAN RESTAURANT",
        "=" * 54,
        f"Order ID : {order_id}",
        f"Date     : {order_time}",
        "-" * 54,
        f"Customer : {name}",
        f"Mobile   : {mobile}",
        f"Address  : {address}",
        "-" * 54,
        f"{'Food Item':27} {'Qty':>4} {'Amount (Rs.)':>14}",
        "-" * 54
    ]

    for food, quantity in cart.items():
        amount = find_price(food) * quantity
        lines.append(
            f"{food[:27]:27} {quantity:>4} {amount:>14.2f}"
        )

    lines.extend([
        "-" * 54,
        f"{'Subtotal':36} Rs. {subtotal:>12.2f}",
        f"{'GST (5% estimate)':36} Rs. {gst:>12.2f}",
        "=" * 54,
        f"{'GRAND TOTAL':36} Rs. {total:>12.2f}",
        "=" * 54,
        "",
        "Thank you for ordering from Veggie Bliss!",
        "             Have a wonderful day!",
        "",
        "GST is an illustrative estimate only.",
        "This application does not process online payments."
    ])

    last_bill_text = "\n".join(lines)
    return last_bill_text

# ---------------- SAVE BILL TO FILE ----------------
def save_bill_to_file(bill_text):
    global last_bill_path

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        prefix="VeggieBliss_Bill_",
        encoding="utf-8",
        delete=False
    ) as file:
        file.write(bill_text)
        last_bill_path = file.name

    return last_bill_path

# ---------------- PRINT BILL ----------------
def print_bill():
    bill_text = generate_bill_text()

    if bill_text is None:
        return

    try:
        file_path = save_bill_to_file(bill_text)

        if sys.platform == "win32":
            # Opens the bill in Notepad.
            # Use Ctrl+P in Notepad to print.
            os.startfile(file_path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", file_path])
        else:
            subprocess.Popen(["xdg-open", file_path])

        messagebox.showinfo(
            "Print Bill",
            "Your bill has been opened in a text editor.\n\n"
            "Press Ctrl+P (or use the editor's Print option), "
            "select your printer, and print the bill."
        )

    except Exception as error:
        messagebox.showerror(
            "Printing Error",
            f"Could not open the bill:\n{error}"
        )

# ---------------- COMPLETE ORDER ----------------
def complete_order():
    global last_bill_text

    bill_text = generate_bill_text()

    if bill_text is None:
        return

    if not messagebox.askyesno(
        "Complete Order",
        "Complete this order and display the final bill?"
    ):
        return

    # Save the final bill before clearing the cart.
    try:
        saved_path = save_bill_to_file(bill_text)
    except Exception as error:
        messagebox.showerror(
            "Save Error",
            f"Could not save the bill:\n{error}"
        )
        return

    bill_window = tk.Toplevel(root)
    bill_window.title("Completed Order - Veggie Bliss")
    bill_window.geometry("650x700")
    bill_window.configure(bg=WHITE)
    bill_window.transient(root)

    tk.Label(
        bill_window,
        text="ORDER COMPLETED",
        font=("Arial", 18, "bold"),
        bg=GREEN,
        fg=WHITE,
        pady=12
    ).pack(fill="x")

    tk.Label(
        bill_window,
        text=f"Bill saved to:\n{saved_path}",
        font=("Arial", 9),
        bg=WHITE,
        fg=DARK,
        wraplength=600
    ).pack(padx=10, pady=5)

    text_frame = tk.Frame(bill_window)
    text_frame.pack(fill="both", expand=True, padx=10, pady=5)

    bill_display = tk.Text(
        text_frame,
        font=("Courier New", 10),
        wrap="none",
        padx=10,
        pady=10
    )

    bill_scroll = ttk.Scrollbar(
        text_frame,
        orient="vertical",
        command=bill_display.yview
    )
    bill_display.configure(yscrollcommand=bill_scroll.set)

    bill_scroll.pack(side="right", fill="y")
    bill_display.pack(side="left", fill="both", expand=True)

    bill_display.insert("1.0", bill_text)
    bill_display.configure(state="disabled")

    def print_saved_bill():
        try:
            if sys.platform == "win32":
                os.startfile(saved_path)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", saved_path])
            else:
                subprocess.Popen(["xdg-open", saved_path])

            messagebox.showinfo(
                "Print Bill",
                "The saved bill has been opened.\n"
                "Use Ctrl+P in the text editor to print."
            )
        except Exception as error:
            messagebox.showerror(
                "Printing Error",
                str(error)
            )

    def finish_and_clear():
        cart.clear()
        update_cart()

        name_entry.delete(0, tk.END)
        mobile_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        bill_window.destroy()

        messagebox.showinfo(
            "Order Successful",
            "Order completed successfully!\n\n"
            f"Your bill is saved at:\n{saved_path}\n\n"
            "The cart has been cleared."
        )

    bottom = tk.Frame(bill_window, bg=WHITE)
    bottom.pack(fill="x", padx=10, pady=10)

    ttk.Button(
        bottom,
        text="Print Bill",
        command=print_saved_bill
    ).pack(side="left", padx=5)

    ttk.Button(
        bottom,
        text="Finish Order & Clear Cart",
        command=finish_and_clear
    ).pack(side="right", padx=5)

# ---------------- BUTTONS ----------------
button_frame = tk.Frame(cart_frame, bg=WHITE)
button_frame.pack(fill="x", pady=4)

tk.Button(
    button_frame,
    text="ADD SELECTED FOOD",
    command=add_to_cart,
    bg=GREEN,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    pady=7,
    cursor="hand2"
).pack(fill="x", pady=2)

ttk.Button(
    button_frame,
    text="Decrease Selected Quantity",
    command=decrease_quantity
).pack(fill="x", pady=2)

ttk.Button(
    button_frame,
    text="Remove Selected Item",
    command=remove_item
).pack(fill="x", pady=2)

ttk.Button(
    button_frame,
    text="Clear Entire Cart",
    command=clear_cart
).pack(fill="x", pady=2)

tk.Button(
    button_frame,
    text="PRINT COMPLETE BILL",
    command=print_bill,
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    pady=7,
    cursor="hand2"
).pack(fill="x", pady=3)

tk.Button(
    button_frame,
    text="COMPLETE ORDER",
    command=complete_order,
    bg=DARK,
    fg=WHITE,
    font=("Arial", 11, "bold"),
    relief="flat",
    pady=9,
    cursor="hand2"
).pack(fill="x", pady=3)

# ---------------- EVENT BINDINGS ----------------
category_combo.bind("<<ComboboxSelected>>", show_menu)
search_var.trace_add("write", lambda *_: show_menu())

# Double-click a food row to add it to cart.
food_tree.bind("<Double-1>", lambda event: add_to_cart())

# ---------------- FOOTER ----------------
tk.Label(
    root,
    text="Veggie Bliss | Restaurant Ordering System",
    bg=DARK,
    fg=WHITE,
    font=("Arial", 9),
    pady=6
).pack(side="bottom", fill="x")

# ---------------- START APPLICATION ----------------
show_menu()
root.mainloop()
