#modularity

import os

def launchWorld(numOfWheels, selectedMaze):
	if int(numOfWheels) == 2:
		os.system("cp ./modularity/twoWheelRover/model.config ./src/maze_rover_spawner_pkg/models/Rover/model.config")
		os.system("cp ./modularity/twoWheelRover/roverModel.sdf ./src/maze_rover_spawner_pkg/models/Rover/roverModel.sdf")
	elif int(numOfWheels) == 4:
		os.system("cp ./modularity/fourWheelRover/model.config ./src/maze_rover_spawner_pkg/models/Rover/model.config")
		os.system("cp ./modularity/fourWheelRover/roverModel.sdf ./src/maze_rover_spawner_pkg/models/Rover/roverModel.sdf")
	elif int(numOfWheels) == 6:
		os.system("cp ./modularity/sixWheelRover/model.config ./src/maze_rover_spawner_pkg/models/Rover/model.config")
		os.system("cp ./modularity/sixWheelRover/roverModel.sdf ./src/maze_rover_spawner_pkg/models/Rover/roverModel.sdf")
	elif int(numOfWheels) == 8:
		os.system("cp ./modularity/eightWheelRover/model.config ./src/maze_rover_spawner_pkg/models/Rover/model.config")
		os.system("cp ./modularity/eightWheelRover/roverModel.sdf ./src/maze_rover_spawner_pkg/models/Rover/roverModel.sdf")			
	else :
		print("Please Enter different number of wheels")
	
	os.system("cp ./mazes/" + selectedMaze + "/model.config ./src/maze_rover_spawner_pkg/models/house_maze/model.config")
	os.system("cp ./mazes/" + selectedMaze + "/model.sdf ./src/maze_rover_spawner_pkg/models/house_maze/model.sdf")	
	
	#build the package after writing the changes
	os.system("colcon build --packages-select maze_rover_spawner_pkg")

	#launch the world
	os.system("ros2 launch maze_rover_spawner_pkg gazebo_world.launch.py")
	
