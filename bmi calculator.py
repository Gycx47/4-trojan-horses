import time


def type_text(text, delay=0.03, end="\n"):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print(end, end="")



#BMI CALCULATION 

def calc_bmi(unit, height, weight):
    if height <= 0 or weight <= 0:
        return None, None

    if unit == "metric":
        bmi = weight / (height * height)
    elif unit == "imperial":
        bmi = 703 * weight / (height * height)
    else:
        return None, None

   
    if bmi <= 16:
        category = "Severe Thinness"
    elif 16 < bmi <= 17:
        category = "Moderate Thinness"
    elif 17 < bmi <= 18.5:
        category = "Mild Thinness"
    elif 18.5 < bmi <= 25:
        category = "Normal"
    elif 25 < bmi <= 30:
        category = "Overweight"
    elif 30 < bmi <= 35:
        category = "Obese Class I"
    elif 35 < bmi <= 40:
        category = "Obese Class II"
    else:
        category = "Obese Class III"

    return bmi, category



#MAIN INTERACTION 

def bmi_calculator():
    #Intro
    type_text("👋 Hello! Welcome to your personal BMI Companion.\n", 0.035)
    time.sleep(0.2)
    type_text("Let's take a look at your body stats for today.\n", 0.03)
    time.sleep(0.2)

    #Choose Unit
    type_text("First, tell me which units you'd like to use:", 0.03)
    type_text("  ▶ metric   (meters & kilograms)", 0.02)
    type_text("  ▶ imperial (inches & pounds)\n", 0.02)

    while True:
        unit = input("Your choice: ").strip().lower()
        if unit in ("metric", "imperial"):
            break
        type_text("That's not one of the options. Let's try again 😊\n")

    #Ask for height & weight
    if unit == "metric":
        type_text("\nGreat! We'll use metric units.\n", 0.03)
        height = float(input("Enter your height in meters (e.g. 1.75): "))
        weight = float(input("Enter your weight in kilograms (e.g. 68.2): "))
    else:
        type_text("\nAlright! We'll use imperial units.\n", 0.03)
        height = float(input("Enter your height in inches (e.g. 68): "))
        weight = float(input("Enter your weight in pounds (e.g. 150): "))

    #Calculating animation
    type_text("\nCrunching the numbers for you", 0.04, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

    #Calculate
    bmi, category = calc_bmi(unit, height, weight)

    if bmi is None:
        type_text("\nHmm… something feels off with the numbers that you gave me.", 0.03)
        type_text("Let's make sure height and weight are positive next time.", 0.03)
        return

    #Results
    time.sleep(0.5)
    type_text("\nHere’s what I found:\n", 0.035)

    type_text(f"  • Your BMI is: {bmi:.2f}", 0.03)
    type_text(f"  • Category  : {category}\n", 0.03)
    time.sleep(0.3)

    
    if category in ("Severe Thinness", "Moderate Thinness", "Mild Thinness"):
        type_text("You fall in the underweight range.\n", 0.03)
        type_text("If this is consistent for you, it might be good to check with a ", 0.03)
        type_text("health professional to stay strong and nourished.", 0.03)
    elif category == "Normal":
        type_text("You're in the normal BMI range — well done! 🌿", 0.03)
        type_text("Remember: BMI is just one number, not the whole story.", 0.03)
    elif category == "Overweight":
        type_text("Your BMI is in the overweight range.\n", 0.03)
        type_text("Small and sustainable lifestyle adjustments can help a lot! 💪", 0.03)
    else:
        type_text("Your BMI falls into the obesity range.\n", 0.03)
        type_text("This can be a helpful sign to check in with a health professional.", 0.03)

    #Closing
    type_text("\nThanks for spending a moment with me today 💙", 0.03)
    type_text("Take good care of yourself — you matter.\n", 0.03)



#RUN PROGRAM NORMALLY

if __name__ == "__main__":
    bmi_calculator()
