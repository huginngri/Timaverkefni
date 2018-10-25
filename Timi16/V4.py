class Clock:
    def __init__(self, hours = "00", minutes = "00", seconds = "00"):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self, the_str):
        list_of_numbers = the_str.split(':')
        self.hours = list_of_numbers[0]
        self.minutes = list_of_numbers[1]
        self.seconds = list_of_numbers[2]
    
    def add_clocks(self, the_other_clock):
        hours = int(self.hours) + int(the_other_clock.hours)
        minutes = int(self.minutes) + int(the_other_clock.minutes)
        seconds = int(self.seconds) + int(the_other_clock.seconds)
        if seconds >= 60:
            minutes +=1
            seconds -= 60
        if minutes >= 60:
            hours += 1
            minutes -= 60
        if hours >= 24:
            hours -= 24
        the_thrid_clock_str = "{} hours, {} minutes and {} seconds".format(hours,minutes,seconds)
        return the_thrid_clock_str

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(int(self.hours), int(self.minutes), int(self.seconds))

def main():
    clock1 = Clock()
    clock2 = Clock()
    print(clock1)
    print(clock2)
    clock1.str_update("03:21:34")
    clock2.str_update("05:45:52")
    print(clock1)
    print(clock2)
    clock3 = clock1.add_clocks(clock2)
    print(clock3)   
main()