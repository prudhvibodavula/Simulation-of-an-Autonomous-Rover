import os
from glob import glob
from setuptools import setup

package_name = 'maze_rover_spawner_pkg'

cur_directory_path = os.path.abspath(os.path.dirname(__file__))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Path to the launch file      
        (os.path.join('share', package_name,'launch'), glob('launch/*.launch.py')),

        # Path to the world file
        (os.path.join('share', package_name,'worlds/'), glob('./worlds/*')),

        # Path to the house maze sdf file
        (os.path.join('share', package_name,'models/house_maze/'), glob('./models/house_maze/*')),

        # Path to the rover sdf file
        (os.path.join('share', package_name,'models/Rover/'), glob('./models/Rover/*')),
        
        # Path to the world file (i.e. house maze + rover)
        (os.path.join('share', package_name,'models/'), glob('./worlds/*')),        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rvrrser515',
    maintainer_email='rvrrser515@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'spawn_demo = maze_rover_spawner_pkg.spawn_demo:main'
        ],
    },
)
