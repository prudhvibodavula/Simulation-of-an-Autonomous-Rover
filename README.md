# SER515-Spring22-Team-5
Simulation of a autonomous based Rover

Steps for installation of required software for rover simulation:

Virtual Machine and Ubuntu installation:

Install Oracle VM
RAM size - 8192MB
Chose option to create a virtual hard drive.
Hard Drive file type - VDI(VirtualBox Disk Image)
Storage on physical hard drive - Fixed size.
Virtual hard drive size - 50- 100Gb
Create virtaul machine and wait until creation is accomplished.
Load ubuntu 20.0.4 .iso image.
Ubuntu->setting->Controller: IDE->CD/DVD drive-> IDE Secondary Master.
Ubuntu->setting->System->Processor-> CPU-> 4
Ubuntu->setting->System->Execution Cap-> 100
Ubuntu-Power ON -> Install Ubuntu
Configure language and username and password. 
Ready to explore ubuntu!

ROS2 foxy-Debian:

Set Locale:
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

Setup sources:
sudo apt update && sudo apt install curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

Ros2 packages:
sudo apt update
sudo apt install ros-foxy-desktop
sudo apt install ros-foxy-ros-base

Gazebo :
sudo apt update
sudo apt install gazebo

Reference:

Installation:
https://brb.nci.nih.gov/seqtools/installUbuntu.html
https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html
https://navigation.ros.org/tutorials/docs/navigation2_with_slam.html
http://gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros

Commands to start autonomous Rover

Please clone the project to Desktop:

Add the below line to the .bashrc:
source ~/Desktop/SER515-Spring22-Team-5/project/install/setup.bash

Open new terminal 
Go to the ~/Desktop/SER515-Spring22-Team-5/project folder:
Build the package:
colcon build 

Launch the gazebo world by giving the following command in a new terminal

python3 roverGUI.py

Launch the controller package in the new terminal by giving the following command

ros2 launch maze_rover_controller_pkg controller_estimator.launch.py



