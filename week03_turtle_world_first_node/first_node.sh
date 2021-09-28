# Start in your virtual machine or docker container with ros
sudo apt install build-essential ros-melodic-desktop-full
source /opt/ros/melodic/setup.bash

# Create dir for project
mkdir first_workspace
cd first_workspace
mkdir src

# First invocation of this command creates infrastructure for your ROS project
catkin_make  # juicy output

# Add your workspace infrastructure to environment and note difference
env | grep ROS
source devel/setup.bash
env | grep ROS

# Create package in workspace
cd src
catkin_create_pkg first_package rospy std_msgs  # juicy output
# inspect contents
ls first_package
less first_package/package.xml

# Open file wiht some editor e.g. VSCode
code . --user-data-dir=/vscode
