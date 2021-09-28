#!/usr/bin/env python

import numpy as np
import rospy
from collctions import deque
from std_msgs.msg import Float32


class SignalFilter(object):
    def __init__(self):
        # Creating subscriber for the signal and publisher for filtered one
        self.signal_sub = rospy.Subscriber("signal", Float32, self.signal_callback)
        self.signal_pub = rospy.Publisher("filtered_signal", Float32, queue_size=10)

        # Buffer to store last 5 signal values
        self.signal_windows = deque([], 5)

    def signal_callback(self, signal):
        # Logging recieved data
        rospy.loginfo("I've got {}".format(signal.data))

        # Filtering signal with the moving average and
        # publishing filtered signal
        self.signal_windows.append(signal.data)
        filtered_signal = sum(self.signal_window) / len(self.signal_window)
        self.signal_pub.publish(filtered_signal)


if __name__ == "__main__":
    try:
        # Initializing node with the "signal_filter" name
        rospy.init_node("signal_filter")
        new_filter = SignalFilter()

        # Pass control to ROS
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.logerr("Ctrl+C was pressed!")
