#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def send(vel):
	pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=5)
	pub.publish(vel)
	

def receive():
	rospy.init_node('base_controller')
	rospy.Subscriber('cmd_vel',Twist,send)
	rospy.spin()

if __name__=='__main__':
	receive()
	
