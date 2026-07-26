import streamlit as st
import pandas as pd
from datetime import datetime

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Usmani Billing",
    page_icon="🧾",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
 
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
 
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 45%, #2c5364 100%);
    }
 
    /* Header */
    .bill-header {
        text-align: center;
        padding: 25px 10px 10px 10px;
        color: #ffffff;
    }
    .bill-header h1 {
        font-weight: 700;
        font-size: 2.4rem;
        margin-bottom: 0px;
        background: linear-gradient(90deg, #f7971e, #ffd200);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .bill-header p {
        color: #cfd8dc;
        font-size: 0.95rem;
        margin-top: 4px;
    }
    .bill-header .maker-tag {
        color: #ffd200;
        font-size: 0.8rem;
        letter-spacing: 0.5px;
        margin-top: 2px;
        opacity: 0.85;
    }
 
    /* Glass card container */
    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 22px 26px;
        margin-bottom: 22px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
    }
 
    .glass-card h3 {
        color: #ffd200;
        font-weight: 600;
        margin-bottom: 14px;
    }
 
    /* Keep the item-row + delete-button columns side by side on all
       screen sizes, including mobile, instead of stacking vertically */
    div[data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        align-items: center !important;
        gap: 8px !important;
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
        min-width: 0 !important;
        width: auto !important;
    }

    /* Item row card */
    .item-row {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #ffffff;
        transition: all 0.2s ease-in-out;
        min-width: 0;
    }
    .item-name, .item-price {
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .item-row:hover {
        background: rgba(255, 255, 255, 0.12);
        transform: translateY(-2px);
    }
    .item-name {
        font-weight: 500;
        font-size: 1.02rem;
        color: #ffffff;
    }
    .item-sub {
        font-size: 0.8rem;
        color: #b0bec5;
    }
    .item-price {
        font-weight: 600;
        font-size: 1.05rem;
        color: #ffd200;
    }
 
    /* Grand total box */
    .grand-total {
        background: linear-gradient(90deg, rgba(247,151,30,0.25), rgba(255,210,0,0.25));
        border: 1px solid rgba(255, 210, 0, 0.4);
        border-radius: 14px;
        padding: 18px 24px;
        text-align: right;
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 10px;
    }
    .grand-total span {
        color: #ffd200;
    }
 
    /* Transparent circular + add button */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1.5px solid rgba(255, 210, 0, 0.6) !important;
        color: #ffd200 !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        transition: all 0.25s ease-in-out !important;
        backdrop-filter: blur(6px);
    }
    div.stButton > button:hover {
        background: rgba(255, 210, 0, 0.18) !important;
        border-color: #ffd200 !important;
        color: #ffffff !important;
        transform: scale(1.03);
    }
 
    /* Delete (small) buttons */
    .delete-btn button {
        background: rgba(255, 0, 0, 0.08) !important;
        border: 1.5px solid rgba(255, 90, 90, 0.5) !important;
        color: #ff8a8a !important;
        width: 38px !important;
        height: 38px !important;
        padding: 0 !important;
        min-width: 38px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .delete-btn button:hover {
        background: rgba(255, 0, 0, 0.2) !important;
        border-color: #ff5a5a !important;
        color: #fff !important;
    }
 
    /* Input fields */
    .stTextInput input, .stNumberInput input {
        background: rgba(255,255,255,0.07) !important;
        color: #fff !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }
    label {
        color: #e0e0e0 !important;
    }

    /* Footer credit */
    .app-footer {
        text-align: center;
        padding: 18px 10px 30px 10px;
        color: #90a4ae;
        font-size: 0.85rem;
    }
    .app-footer span {
        color: #ffd200;
        font-weight: 600;
    }
 
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------
if "bill_items" not in st.session_state:
    st.session_state.bill_items = []  # list of dicts: name, qty, price

# ----------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------
st.markdown(
    f"""
    <div class="bill-header">
        <h1>🧾 Usmani Billing</h1>
        <p>{datetime.now().strftime('%A, %d %B %Y &nbsp;|&nbsp; %I:%M %p')}</p>
        <p class="maker-tag">Made by Mohd Faizan Usmani</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# ADD ITEM FORM
# ----------------------------------------------------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### ➕ Add New Item")

with st.form("add_item_form", clear_on_submit=True):
    c1, c2, c3, c4 = st.columns([3, 1.2, 1.5, 1])
    with c1:
        name = st.text_input("Item name", placeholder="e.g. Coffee")
    with c2:
        qty = st.number_input("Qty", min_value=1, value=1, step=1)
    with c3:
        price = st.number_input("Price (₹)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    with c4:
        st.write("")
        st.write("")
        submitted = st.form_submit_button("＋ Add")

    if submitted:
        if name.strip() == "":
            st.warning("Please enter an item name.")
        elif price <= 0:
            st.warning("Please enter a valid price.")
        else:
            st.session_state.bill_items.append({"name": name.strip(), "qty": int(qty), "price": float(price)})
            st.success(f"Added '{name.strip()}' to the bill.")

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# ITEM LIST
# ----------------------------------------------------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 🧺 Bill Items")

if len(st.session_state.bill_items) == 0:
    st.info("No items added yet. Add your first item above.")
else:
    for idx, item in enumerate(st.session_state.bill_items):
        line_total = item["qty"] * item["price"]
        row_col, del_col = st.columns([6, 1])
        with row_col:
            st.markdown(
                f"""
                <div class="item-row">
                    <div>
                        <div class="item-name">{item['name']}</div>
                        <div class="item-sub">{item['qty']} × ₹{item['price']:.2f}</div>
                    </div>
                    <div class="item-price">₹{line_total:.2f}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with del_col:
            st.markdown('<div class="delete-btn">', unsafe_allow_html=True)
            if st.button("✕", key=f"del_{idx}"):
                st.session_state.bill_items.pop(idx)
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# GRAND TOTAL
# ----------------------------------------------------------------------
grand_total = sum(item["qty"] * item["price"] for item in st.session_state.bill_items)

st.markdown(
    f"""
    <div class="grand-total">
        Grand Total: <span>₹{grand_total:.2f}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# CLEAR ALL BUTTON
# ----------------------------------------------------------------------
if st.session_state.bill_items:
    st.write("")
    if st.button("🗑️ Clear All Items"):
        st.session_state.bill_items = []
        st.rerun()

# ----------------------------------------------------------------------
# APP FOOTER
# ----------------------------------------------------------------------
st.markdown(
    """
    <div class="app-footer">
        Usmani Billing &nbsp;•&nbsp; Crafted by <span>Mohd Faizan Usmani</span>
    </div>
    """,
    unsafe_allow_html=True,
)