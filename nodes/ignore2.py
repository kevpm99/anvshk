#!/usr/bin/env python
import rospy,tf,roslib,math
roslib.load_manifest('learning_tf')
if __name__=='__main__':
	rospy.init_node('dynamic_frame')
	br=tf.TransformBroadcaster()
	rate=rospy.Rate(10.0)
	while not rospy.is_shutdown():
		time=rospy.Time.now().to_sec()*math.pi
		br.sendTransform((2.0*math.cos(time),2.0*math.sin(time),0.0),(0.0,0.0,0.0,1.0),rospy.Time.now(),"carrot1","turtle1")
		rate.sleep()

