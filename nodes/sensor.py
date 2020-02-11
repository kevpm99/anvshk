#!/usr/bin/env python
import rospy,math
from turtlesim.srv import Spawn
from sensor_msgs.msg import LaserScan
from turtlesim.msg import Pose

def spawner():
	rospy.init_node('sensor')
	rospy.wait_for_service('spawn')
	spawner=rospy.ServiceProxy('spawn',Spawn)
	spawner(7,7,0,'turtle2')
	rospy.Subscriber('/turtle1/pose',Pose,sensor)
	rospy.spin()

def sensor(pose):
	scan=LaserScan()
	nor=100
	pub=rospy.Publisher('sensor_data',LaserScan,queue_size=10)
	scan.header.frame_id='turtle1'
	scan.angle_min=-1.57
	scan.angle_max=1.57
	scan.angle_increment=3.14/nor
	scan.time_increment=0.0
	scan.scan_time=0.0
	scan.range_min=0.0
	scan.range_max=4.0
	scan.ranges=[15.0]*100
	d=math.sqrt((7-pose.x)**2+(7-pose.y)**2)
	if d<4.0:
		phi=math.atan((pose.y-7)/(pose.x-7))
		#frame rotates?-->2 cases
		phi=phi-pose.theta#frame rotates
		phi=math.floor(phi/0.0314)
		i=-10
		while i<11:
			scan.ranges[int(phi)+i]=d
			i=i+1
	pub.publish(scan)
	
if __name__=='__main__':
	spawner()
	
