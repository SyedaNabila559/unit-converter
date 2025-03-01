import streamlit as st

# Title of the app with emoji
st.title("🌍 Unit Converter Web App 🌍")

# Dropdown for choosing conversion type with emoji
conversion_type = st.selectbox(
    "Select the type of conversion:",
    ("📏 Length", "🌡️ Temperature", "⚖️ Weight")
)

# Functions to perform conversions
def convert_length(value, from_unit, to_unit):
    units_in_meters = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Miles": 1609.34
    }
    # Convert the value to meters first, then to the target unit
    value_in_meters = value * units_in_meters[from_unit]
    return value_in_meters / units_in_meters[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

def convert_weight(value, from_unit, to_unit):
    units_in_kilograms = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Milligrams": 1e-6,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }
    # Convert the value to kilograms first, then to the target unit
    value_in_kg = value * units_in_kilograms[from_unit]
    return value_in_kg / units_in_kilograms[to_unit]

# Input fields for the value to convert
value = st.number_input("Enter the value to convert:", value=1.0)

# Conversion logic based on the type selected
if conversion_type == "📏 Length":
    from_unit = st.selectbox("From unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Miles"])
    to_unit = st.selectbox("To unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Miles"])
    result = convert_length(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} = {result:.4f} {to_unit} 🌟")  # Rounded to 4 decimal places

elif conversion_type == "🌡️ Temperature":
    from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} = {result:.2f} {to_unit} 🌡️")  # Rounded to 2 decimal places

elif conversion_type == "⚖️ Weight":
    from_unit = st.selectbox("From unit", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To unit", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    result = convert_weight(value, from_unit, to_unit)
    st.write(f"{value} {from_unit} = {result:.4f} {to_unit} ⚖️")  # Rounded to 4 decimal places




