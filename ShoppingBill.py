# ShoppingCartApp.py
import streamlit as st
from PIL import Image
import os

# Sample inventory with image paths and prices
inventory = {
    "Groceries": {
        "Rice (1kg)": {"price": 60, "image": "images/rice.jpg"},
        "Milk (1L)": {"price": 30, "image": "images/milk.jpg"},
        "Eggs (12 pcs)": {"price": 75, "image": "images/eggs.jpg"},
        "Bread": {"price": 35, "image": "images/bread.jpg"}
    },
    "Electronics": {
        "USB Cable": {"price": 150, "image": "images/usb.jpg"},
        "Bluetooth Speaker": {"price": 1200, "image": "images/speaker.jpg"},
        "LED Bulb": {"price": 200, "image": "images/bulb.jpg"},
        "Smartphone": {"price": 12500, "image": "images/phone.jpg"}
    },
    "Clothing": {
        "T-Shirt": {"price": 400, "image": "images/tshirt.jpg"},
        "Jeans": {"price": 1200, "image": "images/jeans.jpg"},
        "Jacket": {"price": 2500, "image": "images/jacket.jpg"},
        "Cap": {"price": 200, "image": "images/cap.jpg"}
    }
}

gst_rate = {
    "Groceries": 5,
    "Electronics": 18,
    "Clothing": 12
}

discounts = {"SAVE10": 10, "FREESHIP": 0}

st.set_page_config(page_title="🛍️ Full-Featured Shopping Cart", page_icon="🛒")
st.title("🛍️ Smart Shopping Cart with GST & Discounts")

category = st.selectbox("Select a Shopping Category", list(inventory.keys()))
selected_items = st.multiselect("Choose Items", list(inventory[category].keys()))

quantity_dict = {}
subtotal = 0

for item in selected_items:
    item_data = inventory[category][item]
    col1, col2 = st.columns([3, 1])
    with col1:
        if os.path.exists(item_data["image"]):
            st.image(Image.open(item_data["image"]), width=120)
        st.write(f"📦 {item} - ₹{item_data['price']}")
    with col2:
        qty = st.number_input(f"Qty: {item}", min_value=1, value=1, key=item)
        quantity_dict[item] = qty
        subtotal += item_data["price"] * qty

promo = st.text_input("🎁 Enter Promo Code (e.g. SAVE10)")
discount = 0
if promo in discounts:
    discount = subtotal * (discounts[promo] / 100)
    subtotal -= discount
    st.info(f"🎉 Promo '{promo}' applied: -₹{round(discount,2)}")

gst_percent = gst_rate[category]
gst_amount = subtotal * gst_percent / 100
total = round(subtotal + gst_amount, 2)

if selected_items:
    st.subheader("🧾 Detailed Bill Summary")
    for item in selected_items:
        price = inventory[category][item]["price"]
        qty = quantity_dict[item]
        st.write(f"{item} x {qty} = ₹{price * qty}")
    if promo in discounts:
        st.write(f"Promo Discount: ₹{round(discount,2)}")
    st.write(f"Subtotal: ₹{round(subtotal,2)}")
    st.write(f"GST ({gst_percent}%): ₹{round(gst_amount,2)}")
    st.success(f"Total Payable: ₹{total}")

    if st.checkbox("📄 Export Bill as TXT"):
        with open("shopping_bill.txt", "w") as file:
            file.write(f"Category: {category}\n")
            file.write("Items Purchased:\n")
            for item in selected_items:
                qty = quantity_dict[item]
                price = inventory[category][item]["price"]
                file.write(f"- {item} x {qty} = ₹{price * qty}\n")
            if promo in discounts:
                file.write(f"Promo Code: {promo} (-₹{round(discount,2)})\n")
            file.write(f"\nSubtotal: ₹{round(subtotal,2)}")
            file.write(f"\nGST ({gst_percent}%): ₹{round(gst_amount,2)}")
            file.write(f"\nTotal: ₹{total}")
        st.info("✅ Bill saved as shopping_bill.txt")