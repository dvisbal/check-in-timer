import time

class CheckInTimer:
    """
    Timer to periodically check-in to see how long it's been
    """

    def __init__(self, seconds = 600):
        self.stop_time = time.time() + seconds
        self.check_ins = [] # save each time there's a check_in
    
    def check_in(self):
        """
        Check how long is left in the timer
        @return (hours, minutes, seconds)
        """
        seconds_left = self.stop_time - time.time()
        if seconds_left > 0:
            hours, seconds_remaining_in_the_hour = divmod(seconds_left, 3600)
            minutes, seconds = divmod(seconds_remaining_in_the_hour, 60)
            time_left_message = ""
            if (hours > 0):
                time_left_message += f"{int(hours)}:"
            if (minutes > 0):
                time_left_message += f"{int(minutes)}:"
            time_left_message += f"{int(seconds)}"
            self.check_ins.append(time_left_message)
        elif self.check_ins[-1] != "done":
            self.check_ins.append("done")
        return self.check_ins