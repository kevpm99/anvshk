#!/usr/bin/env python
import rospy,roslib,math,tf
from turtlesim.msg import Pose
from nav_msgs.msg import Odometry
roslib.load_manifest('learning_tf')

def listener():
	rospy.init_node('odo',anonymous=True)
	rospy.Subscriber('/turtle1/pose',Pose,odo)
	rospy.spin()
def odo(pose):
	pub=rospy.Publisher('odom',Odometry,queue_size=1)
	odom= Odometry()
	odom.header.stamp=rospy.Time.now()
	odom.header.frame_id='turtle1'
	odom.child_frame_id='turtle1'
	odom.twist.twist.linear.x=pose.linear_velocity
	odom.twist.twist.angular.z=pose.angular_velocity
	odom.twist.twist.linear.y=0
	odom.twist.twist.linear.z=0
	odom.twist.twist.angular.x=0
	odom.twist.twist.angular.y=0
	ang=pose.theta
	odom.pose.pose.position.x=pose.x
	odom.pose.pose.position.y=pose.y
	odom.pose.pose.orientation.x=0.0
	odom.pose.pose.orientation.y=0.0
	odom.pose.pose.orientation.z=math.sin(ang/2)
	odom.pose.pose.orientation.w=math.cos(ang/2)
	#odom.pose.pose.orientation=tf.tranformations.quaternion_from_euler(0,0,ang)
	pub.publish(odom)

if __name__=='__main__':
	listener()

