class Airport:
    def __init__(self, runways, gates, fuel_levels, flight_schedule):
        self.runways = runways
        self.gates = gates
        self.fuel_levels = fuel_levels
        self.flight_schedule = flight_schedule

    def check_runway(self):
        ask_clearance = input('Check Runway ("check"): ').lower()
        if ask_clearance == 'check':
            for runway, status in self.runways.items():
                print(f'{runway} is {status}')
        else:
            raise ValueError("Invalid option")

    def check_gate(self):
        check_gates = input('Check Gates ("Check Gates"): ').lower()
        if check_gates == 'check gates':
            for gate, status in self.gates.items():
                print(f'{gate} is {status}')
        else:
            raise ValueError("Invalid option")

    def check_fuel(self):
        check_plane_fuel = input("Check fuel (check fuel): ").lower()
        if check_plane_fuel == 'check fuel':
            for plane, fuel in self.fuel_levels.items():
                if fuel <= '60%':
                    print(f'Fuel low for {plane}')
                else:
                    print('Planes full')
        else:
            raise ValueError("Invalid option")

    def check_schedule(self):
        check_time = input('Check time (check time): ').upper()
        if check_time == 'CHECK TIME':
            print('Airport schedule')
            for date, time in self.flight_schedule.items():
                print(f'{date}: {time}')
        else:
            raise ValueError("Invalid option")


if __name__ == '__main__':
    runways = {
        'Runway One': 'Open',
        'Runway Two': 'Closed',
        'Runway Three': 'Closed',
        'Runway Four': 'Open',
        'Runway Five': 'Open'
    }

    gates = {
        'Gate One': 'Open',
        'Gate Two': 'Closed',
        'Gate Three': 'Closed',
        'Gate Four': 'Open',
        'Gate Five': 'Open'
    }

    fuel_levels = {
        'Plane One': 'Fuel: 80%',
        'Plane Two': 'Fuel: 67%',
        'Plane Three': 'Fuel: 84%',
        'Plane Four': 'Fuel: 30%',
        'Plane Five': 'Fuel: 20%'
    }

    flight_schedule = {
        'January 12th': '9:00PM',
        'January 17th': '2:30AM',
        'January 26th': '12:30PM',
        'January 29th': '6:00AM',
        'January 31st': '8:30AM'
    }

    airport = Airport(runways, gates, fuel_levels, flight_schedule)
    airport.check_runway()
    airport.check_gate()
    airport.check_fuel()
    airport.check_schedule()
