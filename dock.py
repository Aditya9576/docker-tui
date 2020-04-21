import os
#function
def wr():
	print("wrong input")

#-------------------------Credit--------------------------------
def credit():
	print("#############################################################################",end="\n")
	print("""This project is made as a final submission project for an online live session Docker Traning in 2020 on
	YouTube , presented by Vimal Daga Sir.
	[Here i made a Docker TUI Manager , to save lots of time of the developers/users .So that they can mostly
	focus on development insted of typing code.]""")
	print("********************************************************************************",end="\n")
	print("""Project Name:- Docker TUI manager
Language used:- Python3
Prerequisite:- Python 3 , systemctl enabled
Development Status: Beta (still efficient , but may updates in future like : some command or GUI integrated)
Creator:- Aditya Raj
Year:-2020
Thanks to: Vimal Sir""")

	print("#############################################################################",end="\n")
#-------------------------Install Docker ------------------------
def docker_install():
	print("*************************************************************************",end="\n")
	print("Before downloading Docker make sure to create this repo file in your yum.repos.d , this may help to download the docker additional files.")
	print("#########################################################################",end="\n")
	print("""[dock]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck = 0 """)
	print("###########################################################################",end="\n")
	print("NOTE:[This process for creating repo is Valid with Centos and RedHat Linux")
	print("Other OS users should create repo according to their respective] OS")
	print("**************************************************************************",end="\n")
#-----------Image Remove module-----------
def image_remove():
	os.system("clear")
	print("---------Remove IMAGE---------",end="\n")
	print("""1.Remove All
2.Select""")
	opt = int(input("opt: "))
	if opt == 1:
		conf = input("Are you sure y/n: ")
		if conf == 'y':
			os.system("docker rmi $(docker image ls -q)")
		elif conf == 'n':
			return()
		else:
			wr()
	elif opt == 2:
		os.system("docker image ls")
		i_name = input("enter image name: ")
		os.system("docker rmi inspect {}".format(i_name))

#--------------------Image Push Module-----------------------------
def i_push():
	while (True):
		os.system("clear")
		print("--------------Push Image------------------")
		print("""1.Docker Login
2.Push
3.Back""")
		opt = int(input("opt: "))
		if opt == 1:
			os.system("docker login")
		elif opt == 2:
			i_name = input("Ener image name : ")
			os.system("docker push {}".format(i_name))
		elif opt == 3:
			return
		else:
			wr()
		input("click to continue.......")
	

#-----------image main module----------
def image():
	
	img= True
	while(img != False):
		os.system("clear")
		print("----------------Image------------------")
		print("""1.Download Image
2.Image list
3.Rename(tag) Image
4.Remove Image
5.Inspect
6.Push Image
0.Home""")
		img = int(input("opt: "))
		if img == 1:
			i_name = input("Enter Image Name: ")
			i_ver_name =input("Enter Version: ")
			os.system("docker pull {}:{}".format(i_name,i_ver_name))
		elif img == 2:
			os.system("docker image ls")
		elif img == 3:
			os.system("clear")
			print("---------Rename(tag) IMAGE---------")
			os.system("docker image ls")
			i_name = input("enter image name: ")
			t_name = input("enter new name: ")
			os.system("docker tag {} {}".format(i_name,t_name))
		elif img == 4:
			image_remove()
		elif img == 5:
			os.system("clear")
			print("---------INSPECT IMAGE---------")
			os.system("docker image ls")
			i_name = input("enter image name: ")
			os.system("docker image inspect {}".format(i_name))
		elif img == 6:
			i_push()
		elif img == 0:
			return
		else:
			wr()
		input("click to continue.........")
#-----------container----------
#------------------------container launch module-------------------------
def launch_container():
	c_name = input("Provide container a Name:")
	i_name = input("Enter Image Name: ")
	while (True):
		os.system("clear")
		print("""1.Attach a Network
2.Attach a Volume
3.Run only Command
4.Run in Background
5.Get Conatiner Shell
6.BAck""")
		s_name = "it"
		opt = int(input("opt: "))
		if opt == 1:
			os.system("docker network ls")
			n_name = input("Network name: ")
		elif opt == 2:
			os.system("docker volume ls")
			v_name = input("Volume name: ")
		elif opt == 3:
			cmd = input("command: ")
			os.system("docker run -{} --name {} -v {} --network {} {} {}".format(s_name,c_name,v_name,n_name,i_name,cmd))
		elif opt == 4:
			s_name = "itd"
			os.system("docker run -{} --name {} -v {} --network {} {}".format(s_name,c_name,v_name,n_name,i_name))
		elif opt == 5:
			os.system("docker run -{} --name {} -v {} --network {} {}".format(s_name,c_name,v_name,n_name,i_name))
		elif opt == 6:
			return
		else:
			wr()
		#doc_run_cmd = ("docker run -{} --name {} -v {} --network {} {}".format(s_name,c_name,v_name,n_name,i_name))
		input("click to continue.......")

#------------container_stop module (container sub module)-------------
def c_stop():
	while (True):
				os.system("clear")
			
				print("""1.Stop All
2.Select
3.Back""")
				con2 = int(input("opt: "))
				if con2 == 1:
					os.system("docker stop $(docker ps -qa)")
				elif con2 == 2:
					os.system("docker ps")
					c_name = input("Enter name: ")
					os.system("docker stop {}".format(c_name))
				elif con2 == 3:
					return
				else:
					wr()
				input("click to continue...........")

#------------container_remove module (container sub module)-------------
def c_remove():
	while (True):
				os.system("clear")
			
				print("""1.Remove All
2.Select
3.Back""")
				con2 = int(input("opt: "))
				if con2 == 1:
					os.system("docker rm $(docker ps -qa)")
				elif con2 == 2:
					os.system("docker ps -a")
					c_name = input("Enter name: ")
					os.system("docker rm {}".format(c_name))
				elif con2 == 3:
					return
				else:
					wr()
				input("click to continue...........")
	
#-------------container main module------------------------
def container():
	con = True
	while (con != False):
		os.system("clear")
		print("----------------Conatiner------------------")
		print("""1.Launch Container
2.Stop Container
3.Remove Container
4.Running Containers
5.Stopped Containers
6.Inspect Container
7.Start container
8.Attach Container
9.Commit Container
0.Home""")
		con = int(input("opt: "))
		if con == 1:
			launch_container()
		elif con == 2:
			c_stop()
				#c_name = input("enter container name: ")
				#os.system("docker stop {}",format(c_name))
		elif con == 3:
			c_remove()
			#c_name = input("enter container name: ")
			#os.system("docker rm {}",format(c_name))
		elif con == 4:
			os.system("docker ps")
		elif con == 5:
			os.system("docker ps -a")
		elif con == 6:
			c_name = input("enter container name: ")
			os.system("docker inspect {}".format(c_name))
		elif con == 7:
			os.system("docker container pa -a")
			c_name = input("Enter container name: ")
			os.system("docker container start {}".format(c_name))
		elif con == 8:
			c_name = ("Enter container name: ")
			os.system("docker conatiner attach {}".format(c_name))
		elif con == 9:
			c_name = input("enter container name: ")
			c_new_name = input("enter new name: ")
			os.system("docker commit {} {}".format(c_name,c_new_name))
		elif con == 0:
			return
		else:
			wr()
		input("click to continue.......")

#-----------volume----------
def volume():
	vol = True
	while (vol != False):
		os.system("clear")
		print("----------------Volume------------------")
		print("""1.create Volume
2.Volume List
3.Remove Volume
4.Inspect Volume
5.Attach Volume
0.Home""")
		vol = int(input("opt: "))
		if vol == 1:
			v_name = input("Enter volume name: ")
			os.system("docker volume create --name {}".format(v_name))
		elif vol == 2:
			os.system("docker volume ls")
		elif vol == 3:
			os.system("docker volume ls")
			v_name = input(("Enter volume name: "))
			os.system("docker volume rm {}".format(v_name))
		elif vol == 4:
			os.system("docker volume ls")
			v_name = input(("Enter volume name: "))
			os.system("docker volume inspect {}".format(v_name))
		elif vol == 5:
			launch_container()
		elif vol == 0:
			return
		else:
			wr()
		input("click to continue.......")
		
#-----------Network----------
def network():
	net = True
	while (net != False):
		os.system("clear")
		print("----------------Network------------------")
		print("""1.Create Network
2.Network list
3.Remove Network
4.Inspect Network
5.Attach Network
0.HOME""")
		net = int(input("opt: "))
		if net == 1:
			n_name = input("Enter network name: ")
			n_driver_name = input("Enter driver name: ")
			os.system("docker network create --driver {} {}".format(n_driver_name,n_name))
		elif net == 2:
			os.system("docker network ls")
		elif net == 3:
			os.system("docker network ls")
			n_name = input("Enter name: ")
			os.system("docker network rm {}".format(n_name))
		elif net == 4:
			n_name = input("Enter name: ")
			os.system("docker network inspect {}".format(n_name))
		elif net == 5:
			launch_container()
		elif net == 0:
			return
		else:
			wr()
		input("click to continue........")
		

	
		

	
#--------------------------main program----------------------------------
while(True):
	os.system("clear")
	print("------------------------Docker TUI Manager------------------------",end="\n")
	print("""	1.Install Docker
	2.Start Docker
	3.Image
	4.Container
	5.Volume
	6.Network
	7.Credits
	8.Exit""")
	opt1 = int(input("opt: "))
	if opt1 == 1:
		docker_install()
		opt_1=input("Are you sure y/n: ")
		if opt_1 == "y":
			os.system("dnf install docker-ce --nobest")
		elif opt_1 == "n":
			print("cancelled")
		else:
			print("wrong input")
			
	elif opt1 == 2:
		os.system("systemctl start docker")
	elif opt1 == 3:
		image()
	elif opt1 == 4:
		container()
	elif opt1 == 5:
		volume()
	elif opt1 == 6:
		network()
	elif opt1 == 7:
		credit()
	elif opt1 == 8:
		opt_1 = input("Are you sure y/n: ")
		if opt_1 == 'y':
			exit()
		elif opt_1 == 'n':
			print(" ")

		else:
			wr()	
	else:
		print("wrong input");
	input("click to continue......")
 

