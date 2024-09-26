GST_RATE = 0.10
tax_amount = 0
item_price = float(input("Price: $"))
gst_status = input("Does it have GST (Y/N)").upper()
if gst_status == 'Y':
    tax_amount = item_price * GST_RATE
    final_price = item_price + tax_amount
else:
    final_price = item_price
print(f"Your final price is: ${final_price:.2f}")
