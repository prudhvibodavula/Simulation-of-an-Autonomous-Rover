import tkinter as tk
import startLaunch

gui = tk.Tk()

gui.title("Autonomous Rover Project")

gui.geometry("500x300")

nWheels = tk.StringVar()


# defining a function that will
# launch the gazebo world
# by calling startLaunch files
def launchGazebo():
	wheels = nWheels.get()
	maze = selectMaze.get()
	txt.config(text = "launching gazebo")
	nWheels.set("")
	startLaunch.launchWorld(wheels, maze)
	
	
wheels_label = tk.Label(gui, text = 'Enter number of wheels for Rover:', font=('calibre',10, 'bold'))

wheels_entry = tk.Entry(gui,textvariable = nWheels, font=('calibre',10,'normal'))

mazes_label = tk.Label(gui, text = 'select a maze:', font=('calibre',10, 'bold'))
selectMaze = tk.StringVar()
selectMaze.set("Maze_1") # default value

dropList = tk.OptionMenu(gui, selectMaze, "Maze_1", "Maze_2", "Maze_3", "Maze_4", "Maze_5")

launch_btn=tk.Button(gui,text = 'launchGazebo', command = launchGazebo)

wheels_label.grid(row=0,column=1)
wheels_entry.grid(row=0,column=2)
launch_btn.grid(row=3,column=2)
dropList.grid(row=1, column=2)
mazes_label.grid(row=1, column=1)

txt = tk.Label(gui, text = "")
txt.grid(row=7,column=2)

gui.mainloop()

