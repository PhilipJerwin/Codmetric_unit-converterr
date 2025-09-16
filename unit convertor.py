# Codmetric Internship – Task 4: Unit Converter
# Submitted by: Pranesh

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

conversion_map = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°C", "°F"),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "°F", "°C"),
    "3": ("Kilometers to Miles", kilometers_to_miles, "km", "mi"),
    "4": ("Miles to Kilometers", miles_to_kilometers, "mi", "km"),
    "5": ("Kilograms to Pounds", kilograms_to_pounds, "kg", "lb"),
    "6": ("Pounds to Kilograms", pounds_to_kilograms, "lb", "kg")
}

while True:
    print("\n📏 Unit Converter Menu:")
    for key, (label, _, _, _) in conversion_map.items():
        print(f"{key}. {label}")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Exiting Unit Converter. Goodbye!")
        break

    if choice in conversion_map:
        try:
            value = float(input(f"Enter value in {conversion_map[choice][2]}: "))
            result = conversion_map[choice][1](value)
            print(f"✅ {value} {conversion_map[choice][2]} = {result:.2f} {conversion_map[choice][3]}")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")
    else:
        print("⚠️ Invalid choice. Please select a valid option.")
