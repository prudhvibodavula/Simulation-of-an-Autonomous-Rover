import unittest
import robot_controller

class TestController(unittest.TestCase):

    def test_scan_callback(self):
        msg ={}
        msg.ranges = {"180" : "1.8" , "135" : "1.8" , "90" : "1.8" , "45" : "1.8", "0" : "0"}
        robot_controller.Controller.scan_callback(self, msg)
        print(" robot_controller.Controller.scan_callback is verified")
        pass

    def test_state_estimate_callback(self):
        msg ={}
        robot_controller.Controller.state_estimate_callback(self,msg)
        print(" robot_controller.Controller.state_estimate_callback is verified")
        pass

    def test_follow_wall(self):
        msg = [0,0]
        robot_controller.Controller.follow_wall(self)
        print(" robot_controller.Controller.follow_wall is verified")
        pass

if __name__ == '__main__':
        unittest.main()
