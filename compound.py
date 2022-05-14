# initialisation

principal = int(input("Initial amount: "))
increment = int(input("Invest amount every year: "))
duration = int(input("Duration: "))
rate = int(input("Rate of interest in %: "))
initial = principal
years = duration
interest = None

# Main calculation

for duration in range(1, duration + 1):
    interest = principal + (principal * rate / 100)

    print("year", duration, "-", "{:.1f}".format(principal), "\t",
          "{:.1f}".format(interest), "\t",
          "gained", "{:.1f}".format(interest - principal), "+", increment, "=", "{:.1f}".format(interest + increment))

    principal = interest + increment
    duration = duration + 1


# Outputs

print()
print("total amount invested: ", initial + (increment * years))
print("total amount at the end of", years, "year:", "{:.1f}".format(interest + increment))

benefit = (interest + increment) - (initial + (increment * years))
print("total benefit of interest after", duration - 1, "years is:", "{:.1f}".format(benefit))
