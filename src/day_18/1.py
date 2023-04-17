# Open the input file
with open("./src/day_18/input.txt", "r") as f:
    # Read the positions of the cubes from the file
    positions = [tuple(map(int, line.strip().split(","))) for line in f]

# Initialize a set to store the positions of the cubes
cubes = set(positions)

# Initialize a counter for the surface area
surface_area = 0

# Iterate over the positions of the cubes
for x, y, z in positions:
    # Check if the cube at (x+1, y, z) is not in the set of cubes
    if (x+1, y, z) not in cubes:
        # If it is not in the set, then the side of the cube at (x, y, z) facing in the positive x direction is exposed
        surface_area += 1
    # Repeat the process for the sides facing in the negative x, positive y, negative y, positive z, and negative z directions
    if (x-1, y, z) not in cubes:
        surface_area += 1
    if (x, y+1, z) not in cubes:
        surface_area += 1
    if (x, y-1, z) not in cubes:
        surface_area += 1
    if (x, y, z+1) not in cubes:
        surface_area += 1
    if (x, y, z-1) not in cubes:
        surface_area += 1
    if (x, y, z) not in cubes:
        surface_area += 1

# Print the surface area
print(surface_area)