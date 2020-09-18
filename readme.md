<p align="center"><img src="doc/img/realsense.png" width="70%" /><br><br></p>

-----------------

## Overview
**Intel® RealSense™ SDK 2.0** is a cross-platform library for Intel® RealSense™ depth cameras (D400 series and the SR300) and the [T265 tracking camera](./doc/t265.md).

> :pushpin: For other Intel® RealSense™ devices (F200, R200, LR200 and ZR300), please refer to the [latest legacy release](https://github.com/IntelRealSense/librealsense/tree/v1.12.1).

The SDK allows depth and color streaming, and provides intrinsic and extrinsic calibration information.
The library also offers synthetic streams (pointcloud, depth aligned to color and vise-versa), and a built-in support for [record and playback](./src/media/readme.md) of streaming sessions.

Developer kits containing the necessary hardware to use this library are available for purchase at [store.intelrealsense.com](https://store.intelrealsense.com/products.html).
Information about the Intel® RealSense™ technology at [www.intelrealsense.com](https://www.intelrealsense.com/)

> :open_file_folder: Don't have access to a RealSense camera? Check-out [sample data](./doc/sample-data.md)

## Building librealsense - Using conda

You can download and install librealsense and pylibrealsense in conda with:
```shell
        sudo apt-get install libusb-1.0-0-dev pkg-config libgtk-3-dev
        sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev
        python setup.py
```

## What’s included in the SDK:
| What | Description | Download link|
| ------- | ------- | ------- |
| **[Intel® RealSense™ Viewer](./tools/realsense-viewer)** | With this application, you can quickly access your Intel® RealSense™ Depth Camera to view the depth stream, visualize point clouds, record and playback streams, configure your camera settings, modify advanced controls, enable depth visualization and post processing  and much more. | [**Intel.RealSense.Viewer.exe**](https://github.com/IntelRealSense/librealsense/releases) |
| **[Depth Quality Tool](./tools/depth-quality)** | This application allows you to test the camera’s depth quality, including: standard deviation from plane fit, normalized RMS – the subpixel accuracy, distance accuracy and fill rate. You should be able to easily get and interpret several of the depth quality metrics and record and save the data for offline analysis. |[**Depth.Quality.Tool.exe**](https://github.com/IntelRealSense/librealsense/releases) |
| **[Debug Tools](./tools/)** | Device enumeration, FW logger, etc as can be seen at the tools directory | Included in [**Intel.RealSense.SDK.exe**](https://github.com/IntelRealSense/librealsense/releases)|
| **[Code Samples](./examples)** |These simple examples demonstrate how to easily use the SDK to include code snippets that access the camera into your applications. Check some of the [**C++ examples**](./examples) including capture, pointcloud and more and basic [**C examples**](./examples/C) | Included in [**Intel.RealSense.SDK.exe**](https://github.com/IntelRealSense/librealsense/releases) |
| **[Wrappers](https://github.com/IntelRealSense/librealsense/tree/development/wrappers)** | [Python](./wrappers/python), [C#/.NET](./wrappers/csharp), [Node.js](./wrappers/nodejs) API, as well as integration with the following 3rd-party technologies: [ROS](https://github.com/intel-ros/realsense/releases), [ROS2](https://github.com/intel/ros2_intel_realsense), [LabVIEW](./wrappers/labview), [OpenCV](./wrappers/opencv), [PCL](./wrappers/pcl), [Unity](./wrappers/unity), [Matlab](./wrappers/matlab), [OpenNI](./wrappers/openni2), [UnrealEngine4](./wrappers/unrealengine4) and more to come. | |


## Ready to Hack!

Our library offers a high level API for using Intel RealSense depth cameras (in addition to lower level ones).
The following snippet shows how to start streaming frames with BGR-D imformation, before you run please confirm that you hava already install opencv-python.

```python
import pyrealsense2 as rs
import numpy as np
import cv2

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

try:
    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Stack both images horizontally
        images = np.hstack((color_image, depth_colormap))

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        cv2.waitKey(1)

finally:

    # Stop streaming
    pipeline.stop()
```
For more information on the library, please follow our [examples](./wrappers/python/examples), and read the [documentation](./doc) to learn more.

## Contributing
In order to contribute to Intel RealSense SDK, please follow our [contribution guidelines](CONTRIBUTING.md).

## License
This project is licensed under the [Apache License, Version 2.0](LICENSE).
Copyright 2018 Intel Corporation
