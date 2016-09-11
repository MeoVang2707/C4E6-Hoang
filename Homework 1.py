w = float(input('Nhap can nang cua ban(kg): '))
h = int(input('Nhap chieu cao cua ban(cm): '))
h=h/100
BMI= w/(h**2)
print('Your BMI: ',BMI)
if BMI<16:
    x = 'Severely underweight (còi xương)'
elif 16<=BMI<18.5:
    x = 'Underweight (Thiếu cân)'
elif 18.5<=BMI<25:
    x='Normal (Bình thường)'
elif 25<=BMI<=30:
    x='Overweight (Thừa cân)'
else:
    x='Obese (Béo phì)'
print('You are',x)
    
