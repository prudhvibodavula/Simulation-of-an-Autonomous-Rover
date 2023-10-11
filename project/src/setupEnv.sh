#!/bin/bash
#Installation of RoS2 and Gazebo to provide automated environment

set_locale(){

echo "Setting locale"
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

}

set_Sources(){

echo "Setting Sources"
sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

}

install_RosPackages(){

echo " Installing Ros2 Packages"
sudo apt update
sudo apt install ros-foxy-desktop
sudo apt install ros-foxy-ros-base

}

install_gazebo(){

echo " Installing Gazebo "
sudo apt-get update
sudo apt-get install gazebo11

}

install_slam(){

echo " Installing SLAM tool"
sudo apt install ros-foxy-slam-toolbox

}

install_MiscPackages{

echo " Installing all Misc packages - ros2 bag, colcon"
sudo apt install python3-colcon-common-extensions
sudo apt install ros-foxy-robot-steering
sudo apt install ros-galactic-rosbag2
ros2 pkg create --build-type ament_python bag_recorder_nodes_py --dependencies rclpy rosbag2_py example_interfaces std_msgs

}

echo " Starting Installation of required software "
echo "  "

set_Locale
set_Sources
install_RosPackages
install_gazebo
install_slam
install_MiscPackages

echo " Installation is successful"
echo "  "