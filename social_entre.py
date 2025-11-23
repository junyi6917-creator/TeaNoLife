import streamlit as st

# ------------------------------
# Page configuration
# ------------------------------
st.set_page_config(
    page_title="Tea No Life",
    page_icon="🍵",
    layout="centered"
)

st.markdown("<h1 style='text-align: center; color: #90ee90;'>Tea No Life</h1>", unsafe_allow_html=True)

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
# Initialize session state
# ------------------------------
for name, price in items:
    if name not in st.session_state:
        st.session_state[name] = 0

# ------------------------------
# Quantity selectors
# ------------------------------
st.markdown("<div style='color: #90ee90; font-size:20px;'>Select quantities:</div>", unsafe_allow_html=True)

total_sales = 0.0

for name, price in items:
    qty = st.number_input(
        f"{name} (RM{price:.2f})",
        min_value=0,
        max_value=50,
        value=st.session_state.get(name, 0),
        step=1,
        key=name
    )
    total_sales += qty * price

# ------------------------------
# Display total sales
# ------------------------------
st.markdown(
    f"<h2 style='text-align:center; color: #90ee90;'>Total Sales: RM{total_sales:.2f}</h2>",
    unsafe_allow_html=True
)

# ------------------------------
# Reset button
# ------------------------------
if st.button("Reset All"):
    for name, price in items:
        st.session_state[name] = 0
