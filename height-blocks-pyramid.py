

blocks = int(input("Enter number of blocks: "))

for n in range(blocks): 
    if n*(n+1)/2 <= blocks: 
        height = n

print("The height of the pyramid is:",height)
