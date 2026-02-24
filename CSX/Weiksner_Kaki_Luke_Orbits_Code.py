
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math 

G = 6.67E-11
mhost = 5E+24
Dt = 5
host_radius = 6.98E+5


class Planet:
    def __init__(self, xo, yo, vxo, vyo, mass, color, name,radius):
        self.X = [xo]
        self.Y = [yo]
        self.Vx = vxo
        self.Vy = vyo
        self.mass = mass
        self.color = color
        self.name = name
        self.radius = radius
        self.current = True 

    def acceleration(self, x, y):
        r = (x**2 + y**2)**0.5
        r_cubed = r**3
        ax = -G * mhost * x / r_cubed
        ay = -G * mhost * y / r_cubed
        return ax, ay

    def eccentricity(self):
        x, y = self.X[-1], self.Y[-1]                                                                      
        vx, vy = self.Vx, self.Vy                                                                           
        position_hypotenuse = (x**2 + y**2)**.5                                                             
        velcotiy = (vx**2 + vy**2)                                                                         
        mu = G *mhost                                                                                       
        dot_product= x*vx + y*vy                                                                            
        ex = (velcotiy * x - dot_product* vx) / mu - x/position_hypotenuse                                  
        ey = (velcotiy * y - dot_product * vy) /mu - y/position_hypotenuse                                  
        efinal = (ex**2 + ey**2)**0.5                                                                       
        return efinal


    def semi_major_axis(self):
        mu = G*mhost
        distance = (self.X[-1]**2 + self.Y[-1]**2)**.5
        velcity_squared = self.Vx**2 + self.Vy**2
        sma = (mu*distance)/(2*mu-distance*(velcity_squared))                                               
        return sma

    def speed(self):
        speeds = (self.Vx**2 + self.Vy**2)**.5
        return speeds

    def period(self):
        sma = self.semi_major_axis()
        period = 2* math.pi *(sma**3/(G*mhost))**.5
        return period

    def label(self):
        each_label = (f"{self.name}, e: {self.eccentricity():.4f}, T: {self.period():.1e}s, a: {self.semi_major_axis():.1e}m, v: {self.speed():.1f}m/s, r: {self.radius:.1e}")
        return each_label
    
    def each_frame(self):
        x = self.X[-1]
        y = self.Y[-1]
        ax, ay = self.acceleration(x, y)
        x_new = x + self.Vx*Dt + 0.5*ax*Dt**2
        y_new = y + self.Vy*Dt + 0.5*ay*Dt**2
        ax_new, ay_new = self.acceleration(x_new, y_new)
        self.Vx += 0.5*(ax + ax_new)*Dt
        self.Vy += 0.5*(ay + ay_new)*Dt
        self.X.append(x_new)
        self.Y.append(y_new)


def distance(planet1, planet2):
    return ((planet1.X[-1] - planet2.X[-1])**2 + (planet1.Y[-1] - planet2.Y[-1])**2)**0.5

def distance_to_host(planet):
    dth = (planet.X[-1]**2 + planet.Y[-1]**2)**.5
    return dth

def combine_planets(planet1, planet2,combined_radius):
    mass = planet1.mass + planet2.mass
    planet1.Vx = (planet1.mass * planet1.Vx + planet2.mass * planet2.Vx) / mass
    planet1.Vy = (planet1.mass * planet1.Vy + planet2.mass * planet2.Vy) / mass
    planet1.mass = mass
    planet1.name = (f"{planet1.name}+{planet2.name}")
    planet1.color =("purple")
    planet1.radius = combined_radius
    planet2.current = False 
    collisions.append(f"{planet1.name} merged")

def check_colisions():
    current = []

    for i in planets:
        if i.current:
            current.append(i) 

    for i in range(len(current)):
        for j in range(i+1,len(current)):
            planet1, planet2 = current[i], current[j]
            combined_radius = planet1.radius + planet2.radius
            if distance(planet1, planet2) < (combined_radius):
                combine_planets(planet1, planet2,combined_radius)

    for planetss in current:
        radius_together = planetss.radius + host_radius

        if planetss.current and distance_to_host(planetss) < (radius_together):
            planetss.current = False
            planetss.X=[]
            planetss.Y=[]
            print("Hit")
            collisions.append(f"{planetss.name} fell into the host star")


trail = True
collisions = []

planets = [
    Planet(xo=3E+6, yo=0, vxo=0, vyo=3000, mass=5.97E20, color="red", name="Planet A",radius = 6.371E+4),
    Planet(xo=5E+6, yo=0, vxo=0, vyo=7355, mass=5.97E20, color="blue", name="Planet B",radius = 6.371E+4),
    Planet(xo=3.1E+6, yo=0, vxo=0, vyo=100, mass=5.97E20, color="green", name="Planet C",radius = 6.371E+4)
]


def animate(i):
    plt.cla()

    for planet in planets:
        if planet.current:
            planet.each_frame()

    check_colisions()
    plt.plot(0,0, markersize=12, color="Black", label=(f"e=eccentricity, T:Period, a:Semi-major axis,v:velocity, r:radius, m:mass"))
    for planet in planets:
        if planet.current:
            if trail:
                plt.plot(planet.X, planet.Y, "-", linewidth=1, color=planet.color)
            plt.plot(planet.X[-1], planet.Y[-1], marker="o", markersize=8, color=planet.color, label=planet.label())
    
    plt.plot(0, 0, marker="o", markersize=12, color="yellow", label=(f"Hostplanet, r: {host_radius:.1e}, m:{mhost:.1e}"))

    count = 0 
    ax.text(0.02, .98, "Last three Collisions:",transform=ax.transAxes, fontsize=8, color="black", fontweight = "bold")
    for event in collisions[-3:]:
        ax.text(0.02, .96 - count*0.02, event,transform=ax.transAxes, fontsize=8, color="black")
        count +=1

    plt.title("Orbit Simulation")
    plt.legend(loc="upper right", fontsize=7)
    plt.axis('equal')


fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()
