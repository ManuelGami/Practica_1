#!/usr/bin/env python3
import rclpy
from rclpy import Node
from robot_kinematics.kinematics import Robot

class PublicadorTrayectoria(Node):
  def __init__(self):
    super().__init__("nodo_publicador")
    self.robot = Robot()
    self.robot.def_tray()
    self.robot.imp_tray()
    self.robot.th_m[0,0]
  pass

def main():
  try:
    rclpy.init()
    publicador = PublicadorTrayectoria()
    rclpy.spin(publicador)
    rclpy.shutdown()
  except KeyboardInterrupt as e:
    print(e) 
if __name__ == "__main__":
  main()
