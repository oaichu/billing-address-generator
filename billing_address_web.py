# File: billing_address_web_display.py

import streamlit as st
import pandas as pd
import random

# Danh sách thành phố, bang và ZIP code mẫu
us_cities = [
    ("New York", "NY", "10001"),
    ("Los Angeles", "CA", "90001"),
    ("Chicago", "IL", "60601"),
    ("Houston", "TX", "77001"),
    ("Phoenix", "AZ", "85001"),
    ("Philadelphia", "PA", "19019"),
    ("San Antonio", "TX", "78201"),
    ("San Diego", "CA", "92101"),
    ("Dallas", "TX", "75201"),
    ("San Jose", "CA", "95101")
]

# Hàm random tên đường
def random_street():
    street_number = random.randint(100, 9999)
    street_names = [
        "Main St", "Maple Ave", "Oak Dr", "Pine St",
        "Elm St", "Cedar Ln", "Washington Blvd", "Sunset Blvd",
        "Park Ave", "Broadway"
    ]
    return f"{street_number} {random.choice(street_names)}"

# Hàm random số điện thoại US
def random_phone():
    return f"+1-{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}"

# Hàm random họ tên
def random_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "Chris", "Ashley", "Brian", "Jessica"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Taylor", "Thomas"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Hàm tạo danh sách địa chỉ
def generate_addresses(n=50):
    addresses = []
    for _ in range(n):
        name = random_name()
        street = random_street()
        city, state, zip_code = random.choice(us_cities)
        phone = random_phone()
        addresses.append({
            "Full Name": name,
            "Street Address": street,
            "City": city,
            "State": state,
            "ZIP Code": zip_code,
            "Phone Number": phone
        })
    return pd.DataFrame(addresses)

# Giao diện Streamlit
st.title("🎯 Billing Address Generator")

num_addresses = st.number_input("Số lượng địa chỉ muốn tạo:", min_value=1, max_value=500, value=50, step=1)

if st.button("Tạo Billing Address"):
    df = generate_addresses(num_addresses)
    
    st.success(f"✅ Đã tạo {num_addresses} địa chỉ!")
    
    st.dataframe(df, use_container_width=True)
    
    st.caption("📋 Bạn có thể bấm chọn, copy toàn bộ bảng nếu cần sử dụng nhanh!")

