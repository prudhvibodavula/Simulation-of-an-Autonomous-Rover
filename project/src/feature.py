import os
import math
import time

from time import sleep
from controller_estimator import generate_launch_description
def main():
	secondscount1 = time.time()
	generate_launch_description()
	secondscount2 = time.time()
	print(secondscount2-secondscount1)

if __name__ =='__main__':
	main()
