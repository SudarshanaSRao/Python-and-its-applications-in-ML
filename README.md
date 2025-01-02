# [Paper publication](https://link.springer.com/chapter/10.1007/978-981-16-9605-3_34)

# Automatic Dent Detection in Automobile Using IR Sensor
This repository contains the code and documentation related to the paper I published on detecting surface dents on automobiles using an IR sensor. The project demonstrates a practical approach to identifying surface imperfections on vehicle exteriors using infrared (IR) technology. The system employs an IR sensor to detect dents and irregularities in the surface, which can be useful in quality control, vehicle inspection, and repair processes.

## Introduction
The goal of this project was to explore and implement a solution for automated dent detection on automobile surfaces. Traditional methods of dent detection involve manual inspection, which is time-consuming and error-prone. By using an IR sensor, this approach offers a more efficient, accurate, and automated solution for identifying surface defects.

## Project Overview
In this project, an IR sensor is used to scan the surface of a vehicle to detect dents and imperfections. The sensor emits infrared light and measures the reflection. When the surface is flat, the reflected signal is consistent; however, when there is a dent or irregularity, the reflection differs. The system analyzes these differences to detect and map surface imperfections.

Key features of this system:
- **Non-Destructive Testing**: The IR sensor method allows for non-contact detection of surface dents, ensuring the integrity of the vehicle is not compromised.
- **Automation**: It can be used in automated vehicle inspection systems, speeding up quality control processes in manufacturing or service centers.

## System Components
- **IR Sensor**: A high-sensitivity infrared sensor used for measuring surface reflection and detecting surface dents.
- **Microcontroller**: A microcontroller (Arduino Uno) processes the data from the IR sensor.
- **Software**: Arduino IDE was used to implement the dent detection algorithm.

## How It Works
1. The IR sensor is calibrated and positioned to scan the surface of the automobile.
2. The sensor emits infrared light, which reflects back from the surface.
3. The microcontroller processes the reflected light signals and compares the results against a baseline (flat surface).
4. Variations in reflection are analyzed to detect any surface dents or imperfections.
