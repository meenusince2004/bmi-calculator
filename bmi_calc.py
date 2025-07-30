def get_user_input():
    weight_unit = input("Choose weight unit (kg/lbs): ").lower()
    height_unit = input("Choose height unit (cm/inches): ").lower()

    weight_prompt = "Enter weight in {}:".format(weight_unit)
    height_prompt = "Enter height in {}:".format(height_unit)

    weight = float(input(weight_prompt))
    height = float(input(height_prompt))

    return weight, height, weight_unit, height_unit

def BMI(height, weight, weight_unit, height_unit):
    if weight_unit == "kg":
        weight_lb = weight * 2.20462  
    else:
        weight_lb = weight

    if height_unit == "cm":
        height_in = height * 0.393701  
    else:
        height_in = height

    bmi = weight_lb / (height_in ** 2) * 703

    if bmi < 16:
        return 'severely underweight', bmi
    elif 16 <= bmi < 18.5:
        return 'Underweight', bmi
    elif 18.5 <= bmi < 25:
        return 'Healthy', bmi
    elif 25 <= bmi < 30:
        return 'Overweight', bmi
    elif bmi >= 30:
        return 'Obese', bmi

weight, height, weight_unit, height_unit = get_user_input()
quote, bmi = BMI(height, weight, weight_unit, height_unit)
print('Your BMI is: {:.2f} and you are: {}'.format(bmi, quote))
