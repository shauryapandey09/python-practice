# logical operators = evaluate multiple conditions (or, and, not)
#       or = at least one condition must be true(if anyone is true, then whole statement is true)
#       and = both conditions must be true
#       not = inverts the condition (not False, Not True)

#temp = 25
#is_raining = True
#is_sunny = True
#if temp > 35 or temp < 0 or is_raining :
  #  print("The outdoor event is cancelled")
#else:
  #  print("The outdoor event is still scheduled")

temp = 50
is_sunny = True
if temp >= 28 and is_sunny :
    print("It is HOT outside🥵")         #emoji with windows + semi-colon
    print("It is sunny outside☀️")
elif temp <= 0 and is_sunny :
    print("It is COLD outside🥶")
    print("It is SUNNY☀️")
elif temp < 28 and temp > 0 and is_sunny :
    print("It is WARM outside")
    print("It is sunny outside☀️")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is cloudy")
elif temp > 28 and not is_sunny:
    print("It is HOT outside")
    print("It is cloudy")
elif temp < 0 and not is_sunny:
    print("It is COLD outside")
    print("It is cloudy")

