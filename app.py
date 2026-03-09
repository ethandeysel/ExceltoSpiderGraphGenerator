import streamlit as st
from src.engine import process_wheel_data
from src.visualizations import create_control_wheel

st.set_page_config(page_title="Control Wheel Dashboard", layout="wide")
st.title("Security Control Status Wheels")

uploaded_file = st.file_uploader("Upload Control Assessment (XLSX)", type="xlsx")

if uploaded_file:
    df = process_wheel_data(uploaded_file)
    
    # Get unique groups for the sidebar
    available_groups = sorted(df['Group'].unique())
    selected_group = st.sidebar.selectbox("Select Control Group", available_groups)
    
    # Filter and Generate
    group_df = df[df['Group'] == selected_group].copy()
    
    if not group_df.empty:
        fig = create_control_wheel(group_df, selected_group)
        
        # Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("View Raw Data for this Group"):
            st.dataframe(group_df[['Variable', 'Control_Name', 'Status', 'Score/5']])