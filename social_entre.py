import streamlit as st

# ------------------------------
# Page configuration
# ------------------------------
st.set_page_config(page_title="Tea No Life", page_icon="🍵", layout="centered")

# Header with smaller font
st.markdown("<h2 style='text-align: center; color: #90ee90; font-size:24px;'>Tea No Life</h2>", unsafe_allow_html=True)

# ------------------------------
# Items and prices
# ------------------------------
items = [
    ("Milk Tea", 5.99),
    ("Oolong Tea", 2.49),
    ("Toast Roll", 3.49),
    ("Set A", 8.99),
    ("Set B", 11.99),
    ("Set C", 9.49),
    ("Set D", 14.99)
]

# ------------------------------
# Reset flag
# ------------------------------
if "reset_trigger" not in st.session_state:
    st.session_state["reset_trigger"] = False

if st.button("Reset All"):
    st.session_state["reset_trigger"] = True

# Initialize session state for items
for name, price in items:
    if name not in st.session_state or st.session_state["reset_trigger"]:
        st.session_state[name] = 0

st.session_state["reset_trigger"] = False

# ------------------------------
# Quantity selectors
# ------------------------------
st.markdown("<div style='color: #90ee90; font-size:18px;'>Select quantities:</div>", unsafe_allow_html=True)

total_sales = 0.0
for name, price in items:
    qty = st.number_input(
        f"{name} (RM{price:.2f})",
        min_value=0,
        max_value=50,
        value=st.session_state[name],
        step=1,
        key=name
    )
    total_sales += qty * price

# ------------------------------
# Display total sales with smaller font
# ------------------------------
st.markdown(f"<h3 style='text-align:center; color: #90ee90; font-size:22px;'>Total Sales: RM{total_sales:.2f}</h3>", unsafe_allow_html=True)
