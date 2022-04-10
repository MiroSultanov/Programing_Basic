period = int(input())

number_doctors = 7
daily_treated_p = 0
daily_untreated_p = 0
total_t_patients = 0
total_unt_patients = 0

for i in range(1, period + 1):
    number_patients = int(input())
    if number_patients <= number_doctors:
        daily_treated_p = number_patients
        daily_untreated_p = 0
    else:
        if i % 3 == 0:
            if total_unt_patients > total_t_patients:
                number_doctors += 1
        daily_treated_p = number_doctors
        daily_untreated_p = number_patients - daily_treated_p
    total_t_patients += daily_treated_p
    total_unt_patients += daily_untreated_p
print(f"Treated patients: {total_t_patients}.")
print(f"Untreated patients: {total_unt_patients}.")