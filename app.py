import streamlit as st

# Title of the app
st.title("3D Printing Cost Calculator - Z2H Design Studio")

# Centered logo using HTML
st.markdown("""
    <div style="text-align: center;">
        <img src="logo.png" width="100" />
    </div>
""", unsafe_allow_html=True)

# Explanation of how the app works
st.markdown("""
    **Welcome to Z2H Design Studio's 3D Printing Cost Calculator!**

    Use this tool to calculate the total cost of 3D printing based on material weight, print hours, and quantity.
    """)

# Input fields for material cost, weight, quantity, and print hours
material_cost_per_kg = st.number_input("Material Cost per Kg (Rs):", min_value=0.0, step=0.1, format="%.2f")
weight = st.number_input("Weight (grams):", min_value=0.0, step=0.1, format="%.2f")
quantity = st.number_input("Quantity:", min_value=1, step=1)
print_hours = st.number_input("Print Hours:", min_value=0.0, step=0.1, format="%.2f")

# Fixed costs
electricity_cost_per_hour = 3
marketing_cost_per_quantity = 15
machine_cost_per_hour = 20

# Calculate the total cost when the user clicks the "Calculate" button
if st.button("Calculate"):
    try:
        # Calculate material cost per gram and total material cost
        material_cost_per_gram = material_cost_per_kg / 1000
        material_cost = weight * material_cost_per_gram * quantity

        # Calculate electricity, machine, and marketing costs
        electricity_cost = electricity_cost_per_hour * print_hours
        machine_cost = machine_cost_per_hour * print_hours
        marketing_cost = marketing_cost_per_quantity * quantity

        # Calculate total cost
        total_cost = (material_cost + electricity_cost + machine_cost + marketing_cost) * 2.5

        # Display the total price
        st.success(f"**Total Price: {total_cost:.2f} Rs**")

    except ValueError:
        st.error("Please enter valid numerical inputs.")

# Footer message
st.markdown("---")
st.markdown("**Thank you for choosing Z2H Design Studio!**")
st.markdown("---")
st.markdown("**Designed by Z2H Team**")
