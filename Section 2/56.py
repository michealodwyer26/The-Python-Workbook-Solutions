minutes = int(input("Enter the number of minutes: "))
text_messages = int(input("Enter the number of text messages: "))

base_charge = 15.00
additional_text_messages_charge = (text_messages - 50) * 0.15
additional_minutes_charge = (minutes - 50) * 0.25
call_centre_charge = 0.44

subtotal = base_charge + additional_text_messages_charge + additional_minutes_charge + call_centre_charge

tax = subtotal / 100 * 5
total = subtotal + tax 

print()
print("Base charge = ${}".format(round(base_charge, 2)))

if additional_minutes_charge > 0:
	print("Additional minutes charge = ${}".format(round(additional_minutes_charge, 2)))
elif additional_text_messages_charge > 0:
	print("Additional text messages charge = ${}".format(round(additional_text_messages_charge, 2)))

print("Call centre charge = ${}".format(round(call_centre_charge, 2)))
print("Tax = ${}".format(round(tax, 2)))
print()
print("Grand Total = ${}".format(round(total, 2)))