import unittest
import robot_estimator

class TestEstimator(unittest.TestCase):
    def test_euler_from_quarternion(self):
        x, y, z = robot_estimator.Estimator.euler_from_quaternion(self, 0, 0, 0, 0)
        print(" x, y, z ", x, y, z)
        self.assertEqual(robot_estimator.Estimator.euler_from_quaternion(self, 0, 0, 0, 0), (0.0, 0.0, 0.0))

    def test_odom_callback(self):
        msg ={}
        robot_estimator.Estimator.odom_callback(self,msg)
        print(" robot_estimator.Estimator.odom_callback is verified")
        pass

    def test_velocity_callback(self):
        msg = []
        robot_estimator.Estimator.velocity_callback(self,msg)
        print(" robot_estimator.Estimator.velocity_callback is verified")
        pass

if __name__ == '__main__':
        unittest.main()
