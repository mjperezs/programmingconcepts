

speed = input(f"Enter the plane's take off speed in m/s: ")
acceleration = input(f"Enter the plane's take off speed in m/s**2: ")
length = (float(speed)**2)/(2*float(acceleration))
print("The minimum runway length needed for this airplane is" , format(length, '4f'), "meters")




