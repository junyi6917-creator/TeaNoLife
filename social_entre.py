import streamlit as st

# ------------------------------
# Page configuration
# ------------------------------
st.set_page_config(page_title="Tea No Life", page_icon="🍵", layout="centered")

# Header
st.markdown("<h2 style='text-align: center; color: #90ee90; font-size:24px;'>Tea No Life</h2>", unsafe_allow_html=True)

# ------------------------------
# Items and prices
# ------------------------------
left_items = [
    ("Milk Tea", 5.99),
    ("Oolong Tea", 2.49),
    ("Toast Roll", 3.49)
]

right_items = [
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

# Reset button at top
if st.button("Reset All"):
    st.session_state["reset_trigger"] = True

# ------------------------------
# Initialize session state
# ------------------------------
for name, price in left_items + right_items:
    if name not in st.session_state or st.session_state["reset_trigger"]:
        st.session_state[name] = 0

st.session_state["reset_trigger"] = False

# ------------------------------
# Quantity selectors in two main columns
# ------------------------------
st.markdown("<div style='color: #90ee90; font-size:18px;'>Select quantities:</div>", unsafe_allow_html=True)

main_cols = st.columns(2)  # left and right
total = 0.0

# Left column
with main_cols[0]:
    for name, price in left_items:
        qty = st.number_input(
            f"{name} (RM{price:.2f})",
            min_value=0,
            max_value=50,
            value=st.session_state[name],
            step=1,
            key=name
        )
        total += qty * price

# Right column
with main_cols[1]:
    for name, price in right_items:
        qty = st.number_input(
            f"{name} (RM{price:.2f})",
            min_value=0,
            max_value=50,
            value=st.session_state[name],
            step=1,
            key=name
        )
        total += qty * price

# ------------------------------
# Display total
# ------------------------------
st.markdown(f"<h3 style='text-align:center; color: #90ee90; font-size:20px;'>Total: RM{total:.2f}</h3>", unsafe_allow_html=True)
