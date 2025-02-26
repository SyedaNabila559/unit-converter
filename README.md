# unit-converter

🧮 Unit Converter Web App 🌐
Welcome to the Unit Converter Web App built with Streamlit! This app allows you to easily convert between different units of measurement, including length, temperature, and weight. Whether you're converting kilometers to miles or Celsius to Fahrenheit, this app makes the process quick and simple! 😎

📦 Features ✨

Length Conversion: Convert between meters, kilometers, inches, feet, miles, and more! 🏃‍♂️📏

Temperature Conversion: Convert between Celsius, Fahrenheit, and Kelvin 🌡️🔥❄️

Weight Conversion: Convert between kilograms, grams, pounds, ounces, and more! ⚖️💪
🚀 How to Use 🧑‍💻

Run the App:

After cloning the repo, open your terminal, navigate to the project directory, and run the following command:
bash
Copy
streamlit run unit_converter.py
Select Conversion Type:

Choose between Length, Temperature, and Weight conversions from the dropdown menu. 🔽
Input the Value:

Enter the value you wish to convert (e.g., 100). 🔢
Select Units:

Choose the from and to units for conversion (e.g., from Kilometers to Miles). 🌍➡️🌍
Get the Result:

See the converted value displayed instantly! 🎉
💻 Technologies Used 🛠️
Streamlit: A powerful framework to build interactive web apps with Python 🚀
Python: The backend programming language to handle the logic behind the conversions 🐍
📝 How the Conversion Works 🔄
1. Length Conversion 📏:
Converts between various units such as meters, kilometers, inches, miles, etc.
Formula: Convert to meters first, then to the desired unit.
2. Temperature Conversion 🌡️:
Converts between Celsius, Fahrenheit, and Kelvin.
Formula: Uses the standard temperature conversion formulas like:
Celsius to Fahrenheit: F = (C * 9/5) + 32
Celsius to Kelvin: K = C + 273.15
3. Weight Conversion ⚖️:
Converts between kilograms, grams, pounds, ounces, etc.
Formula: Convert to kilograms first, then to the desired unit.
📂 File Structure 📁
bash
Copy
unit_converter/
│
├── unit_converter.py        # Main Python script
└── requirements.txt         # Python dependencies
requirements.txt
text
Copy
streamlit==1.10.0
You can install the required dependencies by running:

bash
Copy
pip install -r requirements.txt
👨‍💻 Run Locally 🏠
Clone this repository:

bash
Copy
git clone https://github.com/SyedaNabila559/unit-converter/
Navigate to the project directory:

bash
Copy
cd unit_converter
Install the dependencies:

bash
Copy
pip install -r requirements.txt
Run the app:

bash
Copy
streamlit run unit_converter.py
🎨 Screenshots 📸
💬 Feedback & Contributions 🤝
Feel free to fork, star, and contribute to this project! You can open an issue or submit a pull request if you'd like to suggest improvements or fix bugs. 😊
