import streamlit as st
import math

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x > 0:
        return math.log(x)
    else:
        return "Logarithm undefined for non-positive values"

# Streamlit UI
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# Add a title with custom styling
st.markdown("<h1 style='text-align: center; color: white; background-color: #4CAF50; padding: 10px;'>Scientific Calculator 🧮</h1>", unsafe_allow_html=True)

# Add a subtitle
st.markdown("<h4 style='text-align: center;'>A simple and elegant calculator for all your scientific needs!</h4>", unsafe_allow_html=True)

# Organize the layout into two columns
col1, col2 = st.columns(2)

# Choose the operation
operation = col1.selectbox(
    "Select Operation:",
    ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)", "Square Root", "Sin", "Cos", "Tan", "Logarithm"]
)

# Get the input values based on the operation
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
    num1 = col1.number_input("Enter first number", value=0.0)
    num2 = col2.number_input("Enter second number", value=0.0)
elif operation == "Square Root":
    num1 = col1.number_input("Enter number for square root", value=0.0)
elif operation in ["Sin", "Cos", "Tan"]:
    angle = col1.slider("Enter angle in degrees", min_value=0, max_value=360, value=0)
elif operation == "Logarithm":
    num1 = col1.number_input("Enter number for logarithm", value=0.0)

# Add a calculate button with a nice message
if st.button("Calculate", key="calculate"):
    # Perform the operation
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Power (x^y)":
        result = power(num1, num2)
    elif operation == "Square Root":
        result = sqrt(num1)
    elif operation == "Sin":
        result = sin(angle)
    elif operation == "Cos":
        result = cos(angle)
    elif operation == "Tan":
        result = tan(angle)
    elif operation == "Logarithm":
        result = log(num1)

    # Display the result
    st.success(f"Result: {result}")
    st.balloons()  # Add balloons animation to make it interactive and fun!

# Footer with a nice touch
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
