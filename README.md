# Object Detection using YOLOv8

Welcome to our GitHub project for Object Detection using YOLOv8! This project utilizes the YOLO (You Only Look Once) algorithm for real-time object detection. In addition, it integrates with a Django backend to provide a web interface for three services: Object Detection using webcam, People Counter, and Car Counter in real-time.

## YOLOv8

YOLOv8 is a state-of-the-art object detection model that offers fast and accurate detection of objects in images and videos. Version 8 incorporates several improvements over previous versions, enhancing both speed and accuracy.

## Django Backend

The Django backend serves as the foundation for our web interface. It provides the necessary infrastructure to handle requests, process data, and communicate with the YOLOv8 model for object detection.

## Real-time Services

### 1. Object Detection using Webcam
This service allows users to perform real-time object detection using their webcam. Simply access the provided URL, grant access to your webcam, and you'll be able to detect objects in the live video stream.

### 2. People Counter
The People Counter service is designed to count the number of people in a given area in real-time. It utilizes the YOLOv8 model to detect human figures and provides a count of the detected individuals.

### 3. Car Counter
Similar to the People Counter, the Car Counter service detects and counts cars in real-time. It's useful for monitoring traffic flow or parking lot occupancy.

### Also the project has feedback page, complaint page and all are working .
## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies for both Django and YOLOv8.
3. Run the Django server to start the web interface.
4. Access the provided URLs to utilize the different services.

## Usage

Once the project is set up and running, you can use the web interface to access the following services:

- **Object Detection using Webcam:** Navigate to the provided URL and grant access to your webcam to start detecting objects in real-time.
- **People Counter:** Access the designated URL to begin counting the number of people in the given area.
- **Car Counter:** Similar to the People Counter, navigate to the specified URL to count cars in real-time.



## Contributions

We welcome contributions from the community to improve this project. Whether it's bug fixes, feature enhancements, or documentation improvements, your contributions are greatly appreciated!

## License

This project is licensed under the [MIT License](LICENSE), which means you're free to use, modify, and distribute the code for both personal and commercial purposes.

## Acknowledgements

We'd like to extend our gratitude to the creators of YOLOv8 and Django for providing the tools and frameworks that made this project possible.
