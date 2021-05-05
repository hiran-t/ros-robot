#!/usr/bin/env python3
import sys, yaml
import rospy,math

import roslib; roslib.load_manifest('motoman_driver')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang import Builder



from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Bool
from std_msgs.msg import Int32

from move_to_joint import main,get_cur_pos,build_traj


# print(JointState)

class FloatLayout(Screen):
    myslider = ObjectProperty()



class myApp(App):


    def build(self):       
        self.load_kv("/home/ros/catkin_ws/src/motoman/gui_python/beta_gui.kv")
        tb = FloatLayout()

        return tb
        

    def AguPub(self,j):
        # print(j)    
        Agru = ['['+str(j[0])+','+str(j[1])+','+str(j[2])+','+str(j[3])+','+str(j[4])+','+str(j[5])+']', '5']
        # Agru = map(str, Agru)

        position = main(Agru)

    def slider_function_link1(self,slider_value):   
        positioning = positionMain[1].positions
      

        if slider_value[0] == 0:
            positioning[0] = math.radians(slider_value[1])
        elif slider_value[0] == 1:
            positioning[1] = math.radians(slider_value[1])
        elif slider_value[0] == 2:
            positioning[2] = math.radians(slider_value[1])
        elif slider_value[0] == 3:
            positioning[3] = math.radians(slider_value[1])
        elif slider_value[0] == 4:
            positioning[4] = math.radians(slider_value[1])
        elif slider_value[0] == 5:
            positioning[5] = math.radians(slider_value[1])

        
        self.AguPub(positioning)

  
if __name__ == '__main__':
    InitHOME = ['[0,0,1.5708,0,-1.5708,0]', '3.5']

    positionMain = main(InitHOME)
    myApp().run()


