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
	laser_freq=40
	f=0
	pub=rospy.Publisher('sensor_data',LaserScan,queue_size=10)
	scan.header.frame_id='turtle1'
	scan.header.stamp=rospy.Time.now()
	scan.angle_min=-3.14
	scan.angle_max=3.14
	scan.angle_increment=6.28/nor
	scan.time_increment=(1.0/laser_freq)/nor
	scan.scan_time=0.001
	scan.range_min=0.0
	scan.range_max=4.0
	scan.ranges=[15.0]*100
	d=math.sqrt((7-pose.x)**2+(7-pose.y)**2)
	#if ((pose.y-7.0)/(pose.x-7.0))*
	if d<4.0:
		phi=math.atan((pose.y-7)/(pose.x-7))
		if pose.y>=7 and pose.x>7:
			f=3
			phi=-3.14+phi
		elif pose.y>7:
			f=4
		elif pose.x>=7 and not pose.y==7:
			f=2
			phi=3.14-phi
		else:
			f=1
		phi=phi-pose.theta
		if phi<-3.14:phi=6.28+phi
		if phi>3.14:phi=phi-6.28
		phi=phi+3.14
		phi=math.floor(99.0*phi/6.28)
		i=-5
		while i<6:
			if phi+i<100 and phi+i>=0:scan.ranges[int(phi)+i]=d
			i=i+1
	pub.publish(scan)
	
if __name__=='__main__':
	spawner()
	
