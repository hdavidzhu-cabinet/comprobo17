#!/usr/bin/env python

""" Exploring basics of creating messages inside of a ROS node """

from geometry_msgs.msg import PointStamped, Point
from std_msgs.msg import Header
import rospy

def process_point(msg):
    print msg.point.y

rospy.init_node('my_subscriber')
rospy.Subscriber('/cool_point', PointStamped, process_point)

r = rospy.Rate(2)
while not rospy.is_shutdown():
    r.sleep()

print "Node is finished!"
