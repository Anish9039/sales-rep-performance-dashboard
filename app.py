import streamlit as st
import pandas as pd

# 1. Setup the Page (Mobile Friendly)
st.set_page_config(page_title="Sales Performance", layout="centered")

# 2. Fake Data (The "Google Sheet")
data = {
    'Rep': ['Alice', 'Bob', 'Charlie'],
    'Sales': [12500, 8400, 15000],
    'Goal': [15000, 15000, 15000],
    'Status': ['Active', 'Warning', 'Top Performer']
}
df = pd.DataFrame(data)

# 3. The Sidebar (Simulating the Login)
st.sidebar.header("Rep Access")
selected_rep = st.sidebar.selectbox("Select Your Name", df['Rep'])

# 4. FILTER THE DATA (The Critical Step you missed)
# This ensures Alice ONLY sees Alice's data
rep_data = df[df['Rep'] == selected_rep].iloc[0]

# 5. The Dashboard UI
st.title(f"👋 Hi, {selected_rep}")
st.write("Here is your month-to-date performance.")

st.divider()

# KPIs in Columns (Looks professional)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Sales", value=f"${rep_data['Sales']:,}")

with col2:
    # Calculate the gap
    gap = rep_data['Goal'] - rep_data['Sales']
    st.metric(label="Remaining to Goal", value=f"${gap:,}", delta_color="normal")

with col3:
    st.metric(label="Current Status", value=rep_data['Status'])

st.divider()

# 6. The Progress Bar (Client requested "Progress toward standard")
progress = rep_data['Sales'] / rep_data['Goal']
st.write(f"**Monthly Goal Progress: {int(progress*100)}%**")
st.progress(progress)
    
# 7. Recent Transactions (Fake table filtered for just this rep)
st.subheader("Your Recent Deals")
# Creating a dummy table just for visual
deals = pd.DataFrame({
    'Client': ['Tech Corp', 'Local Biz', 'Startup Inc'],
    'Amount': [5000, 2000, 1500],
    'Date': ['2023-10-01', '2023-10-05', '2023-10-10'],
    'Status': ['Closed', 'Pending', 'Negotiating']
})
st.dataframe(deals, use_container_width=True, hide_index=True)