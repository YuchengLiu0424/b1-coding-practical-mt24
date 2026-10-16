class PDController:
    # Initialize the controller object
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    # Enable calling the object as a function
    def __call__(self, error):
        # Core controlling functions
        action = (
            self.kp * error
            + self.kd * (error - self.previous_error)
        )
        # Updating current error to previous error
        self.previous_error = error
        return action

    # Resetting the previous error of controller
    # Calling at the start of each simulation
    def reset(self):
        self.previous_error = 0.0