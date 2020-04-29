default energy_MAX = 50
default day_counter = 0


init python:

    def time_of_day(hours, morning=0, day=1, evening=2, night=3):
        res = "night"
        if (hours >= morning) and (hours < day):
            res = "morning"
        if (hours >= day) and (hours < evening):
            res = "day"
        if (hours >= evening) and (hours < night):
            res = "evening"
        return res

    class _Character:
        def __init__(self):
            self.energy = 25
            self.money = 350


    class _Variables:
        def __init__(self):
            #Расход энергии на действия
            self.work_energy_drain = 5
            self.webcam_energy_drain = 3
            #Заработок
            self.work_money_earn = 3
            self.webcam_money_earn = 3
            #Энергия
            self.sleep_energy_gain = 7
            self.work_energy_drain = 5
            self.webcam_energy_drain = 2

    class _Actions:
        def __init__(self):
            self.action_limit = len(time_labels)
            self.counter = 0

        def sleep(self, energy_value, energy_gain):
            if energy_MAX - energy_gain > energy_value:
                energy_value += energy_gain
            else:
                energy_value = energy_MAX
            return energy_value

        def energy_drainer(self, energy_value, energy_drain):
            energy_value -= energy_drain
            self.counter += 1
            return energy_value

        def day_stage(self):
            return self.counter
