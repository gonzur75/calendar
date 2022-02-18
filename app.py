from datetime import datetime, timedelta


class Event:
    def __init__(self, title, location, start_time, duration, owner, participants):
        self.participants = participants
        self.owner = owner
        self.duration = duration
        self.start_time = start_time
        self.location = location
        self.title = title

    @property  # gettery i settery muszą mieć te same nazwy jak parametr classy
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        if len(str(val)):
            self._title = str(val)  #
        else:
            self._title = 'No title'

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, val):
        if not isinstance(val, str):
            raise ValueError(f'Invalid new date value: {val}')

        try:
            parsed_date = datetime.strptime(val, '%d-%m-%Y %H:%M')
        except ValueError:
            raise ValueError(f'Invalid date format, use DD-MM-YYYY HH:MM, {val}')

        if parsed_date < datetime.now() + timedelta(minutes=15):
            raise ValueError(f'Try use date in future: {parsed_date}')

        self._start_time = parsed_date

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError(f'Invalid duration value, use minutes: {val}')
        if not (10 < val < 600):
            raise ValueError(f"Too short or to long: {val}")
        self._duration = timedelta(minutes=val)

    def __str__(self):
        total_seconds = (self.start_time - datetime.now())
        hours, rest = total_seconds.seconds // (60 * 60), total_seconds.seconds % (60 * 60)
        minuts, seconds = rest // 60, rest % 60
        return f'{self.title}, time to event:{total_seconds.days} days {hours}:{minuts}:{seconds}'

    def __repr__(self):
        return f"{type(self).__name__}('{self.title}', '{self.location}', '{self.start_time}', " \
               f"'{self.duration}', '{self.owner}', '{self.participants}')"


event = Event("Piwo", "Wwa", "18-05-2022 22:15", 63, "Ala", ["Ela", "Ola"])

print(event.duration)
print(event)

# event.title = ""
# print(repr(event))
# print(dir(event))
# print(event.title)
# print(event._title)
# event_title = "Python fun"
# print(event.title)
