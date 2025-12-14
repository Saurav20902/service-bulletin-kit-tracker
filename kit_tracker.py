import streamlit as st
import pandas as pd
import sqlite3
from io import BytesIO

st.set_page_config(page_title="Kit Tracker", layout="wide")
st.title("Service Bulletin & Kit Readiness Tracker")

conn = sqlite3.connect("kits.db", check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS parts (part TEXT PRIMARY KEY, stock INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS kits (bulletin TEXT, part TEXT, qty INTEGER)''')
conn.commit()

menu = st.sidebar.selectbox("Navigation", 
    ["Add Spare Parts", "Define Kit (Bulletin)", "Check & Order", "Full Dashboard"])

if menu == "Add Spare Parts":
    st.header("Update Spare Parts Stock")
    part = st.text_input("Part Name")
    qty = st.number_input("Add Quantity", min_value=1)
    if st.button("Save Stock"):
        c.execute("INSERT OR REPLACE INTO parts VALUES (?, ?)", (part, qty))
        conn.commit()
        st.success(f"Updated → {part}: {qty} units")

elif menu == "Define Kit (Bulletin)":
    st.header("Define Kit from Service Bulletin")
    bulletin = st.text_input("Bulletin / Upgrade ID")
    part = st.text_input("Part Name")
    qty = st.number_input("Quantity Needed", min_value=1)
    if st.button("Add to Kit"):
        c.execute("INSERT INTO kits VALUES (?, ?, ?)", (bulletin, part, qty))
        conn.commit()
        st.success(f"Added {qty} × {part} to {bulletin}")

elif menu == "Check & Order":
    st.header("Instant Missing Parts Report")
    bulletin = st.text_input("Enter Bulletin ID")
    if st.button("Generate Report"):
        c.execute("SELECT part, qty FROM kits WHERE bulletin=?", (bulletin,))
        needed = c.fetchall()
        data = []
        for part, req in needed:
            c.execute("SELECT stock FROM parts WHERE part=?", (part,))
            stock = c.fetchone()
            stock = stock[0] if stock else 0
            order = max(0, req - stock)
            data.append([bulletin, part, req, stock, order])
        if data:
            df = pd.DataFrame(data, columns=["Bulletin", "Part", "Needed", "In Stock", "Order Now"])
            st.dataframe(df.style.apply(lambda x: ['background:#ffcccc' if v>0 else '' for v in x], subset=["Order Now"]))
            excel = BytesIO()
            df.to_excel(excel, index=False)
            excel.seek(0)
            st.download_button("Download Excel for SAP", excel, f"{bulletin}_order.xlsx")
        else:
            st.balloons()
            st.success("All parts available!")

else:
    st.header("Live Dashboard")
    kits = pd.read_sql("SELECT * FROM kits", conn)
    parts = pd.read_sql("SELECT * FROM parts", conn)
    st.write("Defined Kits", kits)
    st.write("Current Stock", parts)