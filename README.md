# [Project details](https://sudarshanasrao.github.io/portfolio/portfolio-6/) | [Paper publication](https://www.ijamtes.org/VOL-11-ISSUE-7-2021/)

# Smart Burglar Alarm 

![allouts](https://github.com/SudarshanaSRao/Python-and-its-applications-in-ML/assets/87690830/667892df-90a4-4587-8606-28a2f0032453)

This repository contains a machine learning model designed for a burglar alarm system. The system operates without requiring any datasets for training, making it a self-contained solution. Additionally, the Arduino code for the burglar alarm is provided in the file **Burglar_alarm.ino**.

## Introduction
This project integrates machine learning for intelligent burglar alarm detection without relying on traditional datasets. The model can be used to monitor environments for potential intruders and trigger the alarm accordingly.

## Machine Learning Model

![vid](https://github.com/SudarshanaSRao/Python-and-its-applications-in-ML/assets/87690830/668b97ba-88f2-4001-8a6c-a2eaa6fe86ab)

The ML model (OpenCV2 + Histogram of Oriented Gradients or HOG + Support Vector Machine or SVM) is designed to detect patterns in real-time sensor data (such as motion or sound) and make decisions on whether a security breach has occurred. 

### Key Features:
- **No dataset required**: The model learns from live inputs rather than requiring pre-collected datasets.
- **Real-time decision-making**: It can analyze sensor data in real-time and trigger alerts for potential intrusions.
- **Self-contained**: All necessary logic and machine learning algorithms are embedded directly within the model, simplifying setup and usage.

## Arduino Code
The Arduino code for this project is located in the file **Burglar_alarm.ino**. This code allows the system to interface with sensors (such as PIR sensors for motion detection) and take actions such as activating a buzzer when suspicious activity is detected.

To view or modify the Arduino code:
1. Download the **Burglar_alarm.ino** file.
2. Open it in the [Arduino IDE](https://www.arduino.cc/en/software).
3. Upload it to your Arduino device.

## How It Works
1. **Sensor Integration**: The system uses a PIR sensor to monitor for any abnormal activity in the monitored area.
2. **ML Model Processing**: The sensor data is fed into the ML model that analyzes the patterns and determines whether the input corresponds to a legitimate threat.
3. **Trigger Alarm**: If a breach is detected, the model signals the Arduino to activate the alarm, typically by sounding a buzzer or notifying via other means.

## System Setup
### Required Components:
- **Arduino Uno** (or compatible board)
- **PIR Sensor** (for motion detection)
- **Buzzer** (for the alarm)
- **Power Supply**
- **Connecting Wires**

### Setting Up:
1. Connect the PIR sensor to the Arduino (following the pinout defined in the **Burglar_alarm.ino** code).
2. Connect the buzzer to the appropriate output pin on the Arduino.
3. Load the **Burglar_alarm.ino** code into your Arduino IDE and upload it to the Arduino board.
4. Power the system and it will begin monitoring the environment for potential intrusions.



