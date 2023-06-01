from vpython import sphere, vector, rate, color, arrow, scene, label, button
G = 1

scene.title = "N-Body Simulation"
scene.background = color.black
scene.width = 1200
scene.height = 700
class Body:
    def __init__(self, position, velocity, mass, c, l="N/A"):
        self.visible = True;
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.force = vector(0, 0, 0)
        self.sphere = sphere(pos=self.position, radius=0.1, color=c, make_trail=True, trail_radius=0.01)
        self.momentum_arrow = arrow(pos=self.position, axis=self.velocity, color=color.green, shaftwidth=0.05)
        self.force_arrow = arrow(pos=self.position, axis=self.force, color=color.red, shaftwidth=0.05)
        self.label = label(pos=self.position, text=f'{l}', space=self.sphere.radius, height=10, border=6, font='sans')
        self.toggle_label()
        self.toggle_visible()

    def update(self, time_step):
        self.velocity += 0.5 * self.force / self.mass * time_step
        self.position += self.velocity * time_step
        self.sphere.pos = self.position
        self.momentum_arrow.pos = self.position
        self.momentum_arrow.axis = self.velocity.norm()/4
        self.force_arrow.pos = self.position
        self.force_arrow.axis = self.force.norm()/4
        self.label.pos = self.position

    def toggle_label(self):
        if self.visible:
            self.label.visible = not self.label.visible
    def toggle_visible(self):
        self.sphere.visible = not self.sphere.visible
        self.momentum_arrow.visible = not self.momentum_arrow.visible
        self.force_arrow.visible = not self.force_arrow.visible
        self.visible = not self.visible

def run_simulation(bodies, other_bodies, time_step = 0.001, max_steps = 20000):
    for step in range(max_steps):
        rate(1000)

        for body in bodies:
            body.update(time_step)
        
        for i in range(len(bodies)):
            for j in range(i+1, len(bodies)):
                dist = bodies[j].position - bodies[i].position
                force = G * bodies[i].mass * bodies[j].mass * dist.norm() / dist.mag**2
                bodies[i].force = force
                bodies[j].force = -force

        for body in bodies:
            body.velocity += 0.5 * body.force / body.mass * time_step
        

        for body in other_bodies:
            body.update(time_step)
        
        for i in range(len(other_bodies)):
            for j in range(i+1, len(other_bodies)):
                dist = other_bodies[j].position - other_bodies[i].position
                force = G * other_bodies[i].mass * other_bodies[j].mass * dist.norm() / dist.mag**2
                other_bodies[i].force = force
                other_bodies[j].force = -force

        for body in other_bodies:
            body.velocity += 0.5 * body.force / body.mass * time_step

# Base initial conditions
initial_conditions_1 = [
    Body(vector(0, 1, 0), vector(0, 0, 1), 1, color.red, "Base"),
    Body(vector(1, 1, 0), vector(0, 1, 0), 2, color.red, "Base"),
    Body(vector(0, 0, 1), vector(-1, 1, 0), 2, color.red, "Base"),
    Body(vector(-1, 0, 1), vector(0, -1, 0), 2, color.red, "Base"),
]

initial_conditions_2 = [
    Body(vector(0, 1, 0), vector(-0.01, 0, 1), 1, color.green, "Different Velocity"),
    Body(vector(1, 1, 0), vector(0.01, 1, 0), 2, color.green, "Different Velocity"),
    Body(vector(0, 0, 1), vector(-1, 1.01, 0), 2, color.green, "Different Velocity"),
    Body(vector(-1, 0, 1), vector(0, -1, 0.01), 2, color.green, "Different Velocity"),  # Slightly different initial velocity here
]

initial_conditions_3 = [
    Body(vector(0, 1, -1), vector(0, 0, 1), 1, color.blue, "Base"),
    Body(vector(1, 0, 0), vector(0, 1, 0), 2, color.blue, "Base"),
    Body(vector(0, 1, 0), vector(0, 1, 0), 2, color.blue, "Base"),
    Body(vector(0, 0, -1), vector(0, -1, 0), 2, color.blue, "Base"),
]

initial_conditions_4 = [
    Body(vector(0, 1.01, -1), vector(0, 0, 1), 1.01, color.magenta, "Different Mass"),
    Body(vector(1, 0, 0), vector(0, 1, 0), 2.01, color.magenta, "Different Mass"),
    Body(vector(0, 1.01, 0), vector(0, 1, 0), 2.01, color.magenta, "Different Mass"),
    Body(vector(-0.01, 0, -1), vector(0, -1, 0), 1.99, color.magenta, "Different Mass"),
]
initial_conditions_5 = [
    Body(vector(0, 0, 0), vector(0, 0, 1), 1, color.purple, "Base"), 
    Body(vector(1, 0, 0), vector(0, 1, 0), 2, color.purple, "Base"),
]
initial_conditions_6 = [
    Body(vector(0, 0, 0), vector(0, 0.01, 1), 1, color.orange, "Different Velocity"),
    Body(vector(1, 0, 0), vector(0, 1, 0.01), 2, color.orange, "Different Velocity"),
]
initial_conditions_7 = [
    Body(vector(0, 0, 0), vector(0, 0, 1), 1, color.cyan, "Base"),
    Body(vector(1, 0, 0), vector(0, 1, -1), 2, color.cyan, "Base"),
    Body(vector(0, 1, 0), vector(0, 1, 0), 2, color.cyan, "Base"),
]
initial_condition_8 = [
    Body(vector(0, 0, 0), vector(0, 0, 1.01), 1, color.white, "Different Velocity"),
    Body(vector(1, 0, 0), vector(0, 1, -1.01), 2, color.white, "Different Velocity"),
    Body(vector(0, 1, 0), vector(0, 1, 0.01), 2, color.white, "Different Velocity"),
]
def toggle_labels(bodies):
    for body in bodies:
        body.toggle_label()

toggle_button = button(text="Toggle Labels", pos=scene.title_anchor, bind=lambda: toggle_labels(initial_conditions_1 + initial_conditions_2 + initial_conditions_3 + initial_conditions_4 + initial_conditions_5 + initial_conditions_6 + initial_conditions_7 + initial_condition_8))

def run_pair(con_one, con_two):
    scene.pause()

    for body in con_one+con_two:
        body.toggle_visible()
    
    run_simulation(con_one, con_two)
    scene.pause()
    for body in con_one+con_two:
        body.toggle_visible()

run_pair(initial_conditions_5, initial_conditions_6)
run_pair(initial_conditions_7, initial_condition_8)
run_pair(initial_conditions_3, initial_conditions_4)
run_pair(initial_conditions_1, initial_conditions_2)


def euler_step(x, v, a, dt):
    x_next = x + v * dt
    v_next = v + a * dt
    return x_next, v_next

def verlet_step(x, x_prev, a, dt):
    x_next = 2*x - x_prev + a * dt**2
    return x_next

def runge_kutta_step(t, y, f, dt):
    # Runge-Kutta 4th order
    # t is current time
    # y is the current value
    # f is the function to be integrated
    # dt is the time step
    k1 = dt * f(t, y)
    k2 = dt * f(t + dt/2, y + k1/2)
    k3 = dt * f(t + dt/2, y + k2/2)
    k4 = dt * f(t + dt, y + k3)
    y_next = y + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    return y_next

