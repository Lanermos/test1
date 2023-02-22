import time
import RPi.GPIO as GPIO
import math

# Define GPIO pins for motor control
motor1a = 2
motor1b = 3
motor2a = 4
motor2b = 5

# Initialize GPIO pins for motor control
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motor1a, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)
GPIO.setup(motor2a, GPIO.OUT)
GPIO.setup(motor2b, GPIO.OUT)

# Set up five random coordinates
coords = [(2, 4), (6, 8), (10, 12), (3, 1), (7, 5)]

# Calculate shortest distance to each coordinate
distances = []
for coord in coords:
    distance = math.sqrt((coord[0]**2) + (coord[1]**2))
    distances.append(distance)

# Determine the closest coordinate
closest_index = distances.index(min(distances))
closest_coord = coords[closest_index]

# Move the robot to the closest coordinate
x = closest_coord[0]
y = closest_coord[1]
print(f"Moving to coordinate ({x}, {y})")
time.sleep(1)

# Calculate distance to move forward
dist_to_move = math.sqrt((x**2) + (y**2))

# Move the robot forward
GPIO.output(motor1a, GPIO.HIGH)
GPIO.output(motor1b, GPIO.LOW)
GPIO.output(motor2a, GPIO.HIGH)
GPIO.output(motor2b, GPIO.LOW)

# Wait for some time to move the robot forward
time.sleep(dist_to_move)

# Stop the robot
GPIO.output(motor1a, GPIO.LOW)
GPIO.output(motor1b, GPIO.LOW)
GPIO.output(motor2a, GPIO.LOW)
GPIO.output(motor2b, GPIO.LOW)

# Clean up GPIO pins
GPIO.cleanup()
