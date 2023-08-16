import torch

class SimpleKeyboardCommands:
    """
    Keeps track of the state of the keyboard commands into the viewer when playing.
    """

    def __init__(self, device="cuda:0"):
        self.x_cmd = 0
        self.y_cmd = 0
        self.yaw_cmd = 0

        self.yaw_step = 0.25
        self.x_step = 0.25
        self.y_step = 0.25

        self.command_range = {
            "x": [-2.0, 2.0],
            "y": [-2.0, 2.0],
            "yaw": [-3.14, 3.14]
        }

        self.device = device

        # self.keyboard_events = {
        #     "FORWARD": torch.tensor([[1.0, 0., 0.]], device=self.device),
        #     "BACKWARD": torch.tensor([[-1.0, 0., 0.]], device=self.device),
        #     "LEFT": torch.tensor([[0., -1.0., 0.]], device=self.device),
        #     "RIGHT": torch.tensor([[0., 1.0, 0.]], device=self.device),
        #     "YAW_LEFT": torch.tensor([[0., 0., 1.]], device=self.device),
        #     "YAW_RIGHT": torch.tensor([[0., 0., -1.]], device=self.device),
        # }

    def update_command(self, event):
        if event=="FORWARD":
            self.x_cmd += self.x_step
            self.x_cmd = min(self.x_cmd, self.command_range["x"][1])
        elif event=="BACKWARD":
            self.x_cmd -= self.x_step
            self.x_cmd = max(self.x_cmd, self.command_range["x"][0])
        elif event=="RIGHT":
            self.y_cmd += self.y_step
            self.y_cmd = min(self.y_cmd, self.command_range["y"][1])
        elif event=="LEFT":
            self.y_cmd -= self.y_step
            self.y_cmd = max(self.y_cmd, self.command_range["y"][0])
        elif event=="YAW_LEFT":
            self.yaw_cmd += self.yaw_step
            self.yaw_cmd = min(self.yaw_cmd, self.command_range["yaw"][1])
        elif event=="YAW_RIGHT":
            self.yaw_cmd -= self.yaw_step
            self.yaw_cmd = max(self.yaw_cmd, self.command_range["yaw"][0])

    @property
    def command_state(self):
        return torch.tensor([[self.x_cmd, self.y_cmd, self.yaw_cmd]])
        
        

            

    
