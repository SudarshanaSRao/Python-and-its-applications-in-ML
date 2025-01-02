# [Project details](https://sudarshanasrao.github.io/portfolio/portfolio-7/) | [Paper publication](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3883931)

# ML Based Traffic Light Detection and IR Sensor Based Proximity Sensing for Autonomous Cars
This project focuses on building an automated system that allows an autonomous car to detect and recognize traffic lights using machine learning and computer vision, with the added functionality of distance measurement for obstacle avoidance.

### Key Components:
- **Traffic Light Detection**: A model trained on images of traffic lights to recognize and classify their colors.
- **Distance Measurement**: An IR sensor interfaced with Arduino Uno for detecting obstacles and maintaining a safe distance.
- **Autonomous Car**: The system enables the autonomous car to recognize traffic lights and avoid nearby obstacles based on the distance measured by the IR sensor.

## Dataset
The images of traffic lights are stored in a folder named **'light'** within the present working directory (PWD) of the Python environment. These images are used to train the machine learning model for traffic light recognition.

## Key Techniques
1. **Traffic Light Recognition Using OpenCV2**:
   - The system uses **OpenCV2** to process traffic light images. In-built OpenCV functions help reduce noise from non-traffic-related objects (such as trees and other lights), improving the accuracy of the model.
   - The images are analyzed to identify the color of the traffic light (Red, Yellow, or Green) to control the car's behavior.

2. **Machine Learning Model**:
   - A machine learning model was trained using the dataset of traffic light images, which can classify the color of the light with high accuracy.
   
3. **Distance Measurement Using IR Sensor**:
   - The **IR sensor** interfaced with an **Arduino Uno** measures the distance between the autonomous car and nearby obstacles, helping it avoid collisions.

4. **Image Noise Reduction**:
   - Several in-built functions of **OpenCV2** are utilized to remove any noise in the image (such as leaves, background objects, or other traffic lights), improving the performance of the model.

## How It Works
1. **Traffic Light Detection**:
   - The traffic light images are processed using OpenCV2 and analyzed by the trained machine learning model.
   - The model classifies the traffic light as **Red**, **Yellow**, or **Green**.

2. **Obstacle Detection**:
   - The IR sensor continuously measures the distance to nearby obstacles. If an obstacle is detected within a critical distance, the car will take action to avoid collision.

3. **Autonomous Car Response**:
   - Based on the classification of the traffic light and the distance measurements, the autonomous car will:
     - **Stop** at a red light.
     - **Proceed with caution** at a yellow light.
     - **Go ahead** if the light is green.
     - **Avoid obstacles** when the IR sensor detects a nearby object.

4. **Python Code**:
   - The Python code is stored in the **"Traffic.py"** file and implements the machine learning algorithm and OpenCV processing for traffic light recognition.
   
5. **Arduino Code**:
   - The Arduino code, stored in **"Distance measurement"**, interfaces the IR sensor with the Arduino Uno and calculates the distance to obstacles.

## Results and Accuracy
- The model was live-tested with a **93% accuracy** rate in detecting and recognizing traffic lights and obstacles.
- The system reliably responded to the signals from traffic lights and avoided nearby obstacles in real-time.
