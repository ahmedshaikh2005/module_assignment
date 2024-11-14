def sleep_tracker(hours):
 return f'{hours} hours sleep is better for health '
hours = int(input("Enter your sleeping hours: "))


if hours < 8:
    print("You are ruining your health  .")
else:
    print("You are doing great.")

