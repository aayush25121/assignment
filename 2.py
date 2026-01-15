# ALGORITHM: Arrange Clothes in a Luggage Bag

# Step 1: Start the program
start_program = True

# Step 2: Open the suitcase on a flat surface
suitcase_status = "open and placed flat"

# Step 3: List all clothes and items required for the trip
items = [
    "shirts", "t-shirts", "pants", "jeans",
    "innerwear", "socks", "shoes",
    "towel", "accessories", "toiletries", "charger"
]

# Step 4: Separate items into categories
heavy_items = ["shoes", "jeans", "jackets"]
light_items = ["t-shirts", "shirts", "shorts"]
small_items = ["socks", "innerwear", "belts", "charger"]
delicate_items = ["formal shirts", "dresses", "fragile accessories"]

# Step 5: Fold or roll clothes properly
for cloth in light_items:
    fold_style = "roll to save space"

for cloth in delicate_items:
    fold_style = "fold neatly to avoid wrinkles"

# Step 6: Place heavy items at the bottom of the suitcase
bottom_layer = heavy_items   # forms a stable base

# Step 7: Place medium-weight clothes above heavy items
middle_layer = ["shirts", "pants", "lower wear"]

# Step 8: Place delicate clothes on the top layer
top_layer = delicate_items   # prevents crushing

# Step 9: Use small items to fill empty spaces
for item in small_items:
    if item == "socks":
        place_location = "inside shoes"
    elif item == "innerwear":
        place_location = "side gaps"
    else:
        place_location = "along edges"

# Step 10: Keep frequently used items easily accessible
easy_access_items = ["jacket", "toiletries pouch", "charger", "one pair of clothes"]

# Step 11: Handle toiletries and liquids safely
toiletries = "separate pouch placed on top or side"

# Step 12: Check if suitcase closes without force
if suitcase_status == "overfilled":
    rearrange_items = True
else:
    suitcase_ready = True

# Step 13: Close and zip the suitcase properly
suitcase_status = "closed and zipped"

# Step 14: End the program
end_program = True