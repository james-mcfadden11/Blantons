
availability = "Wild Turkey 101 Straight Bourbon 101 Proof: 733 Stores found for Allegheny county"

number_of_stores= int(availability.split(": ")[1][:2].strip())

print(number_of_stores)
print(number_of_stores < 10)
