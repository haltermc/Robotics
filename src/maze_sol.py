#! /usr/bin/env python 

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
    print msg.ranges[355]

    print msg.ranges[365]
    
    if msg.ranges[355]>1 and msg.ranges[365]>1:
        move.linear.x = .25
        move.angular.z = 0
    
    elif (msg.ranges[315]<msg.ranges[405]) and (msg.ranges[270]<msg.ranges[450]):
        move.linear.x = 0
        move.angular.z = 4.5
    elif (msg.ranges[405]<msg.ranges[315]) and (msg.ranges[450]<msg.ranges[270]):
        move.linear.x = 0
        move.angular.z = -4.5
        
    pub.publish(move)
   
rospy.init_node('exam')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1) 
move = Twist()

rospy.spin()
