#3.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)  
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

print(f"Slope: {slope}, Distance: {distance}")

#4. Comparing Slopes
slope1 = 2
slope2 = 2.0
print(slope1 == slope2) 

