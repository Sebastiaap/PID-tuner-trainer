from pid_controller import PIDController

import matplotlib.pyplot as plt

setpoint = 100.0

controller = PIDController(Kp=2, Ki=0.1, Kd=0.05, setpoint=setpoint)
current_value = 0.0
dt = 0.1

time = []
values = []
outputs = []
setpoints = []

for i in range(200):
    output = controller.update(current_value, dt)
    current_value += output * 0.1
    print(f"Iteration {i}: value={current_value:.2f}, output={output:.2f}")

    time.append(i * dt)
    values.append(current_value)
    outputs.append(output)
    setpoints.append(setpoint)

plt.figure(figsize=(10, 6))
plt.plot(time, values, label='System Value')
plt.plot(time, setpoints, '--', label='Setpoint')
plt.plot(time, outputs, ':', label='Control Output')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('PID Controller Response')
plt.legend()
plt.grid(True)
plt.show()
