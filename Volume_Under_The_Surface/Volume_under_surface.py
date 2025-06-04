# Numerical integration using double sum
def calculate_volume(n=1000):
    dx = 1.0 / n
    dy = 1.0 / n
    volume = 0
    
    for i in range(n):
        for j in range(n):
            x = i * dx
            y = j * dy
            z = x**2 + y**2
            volume += z * dx * dy
    
    return volume

# Calculate volume
vol = calculate_volume()
print(f"Volume (numerical): {vol:.6f}")

# Analytical solution: integral of (x^2 + y^2) from 0 to 1 for both x and y
# = integral of x^2 dx * integral of 1 dy + integral of 1 dx * integral of y^2 dy
# = (1/3) * 1 + 1 * (1/3) = 2/3
analytical = 2/3
print(f"Volume (analytical): {analytical:.6f}")
print(f"Error: {abs(vol - analytical):.6f}")