class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def update(self, measured_value, dt):
        error = self.setpoint - measured_value

        P = self.Kp * error
        I = self.Ki * self.integral
        D = self.Kd * (error - self.prev_error) / dt

        self.prev_error = error
        self.integral += error * dt

        return P + I + D