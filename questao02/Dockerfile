# syntax=docker/dockerfile:1

FROM ros:humble

RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    build-essential  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws

COPY ./src ./src

SHELL ["/bin/bash", "-c"]

RUN . /opt/ros/humble/setup.sh && \
    colcon build 

ENTRYPOINT ["/bin/bash", "-c", "source /ros2_ws/install/setup.bash && ros2 run pacote01 memory"]
