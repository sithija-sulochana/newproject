shouldworkHour = 8

def totalsal():
    employees = [
        {"name": "Alice", "hoursworked": 12},
        {"name": "Bob", "hoursworked": 8},
        {"name": "Carol", "hoursworked": 6}
    ]

    for em in employees:
        worktime = em["hoursworked"]

        # Calculate normal salary
        if worktime > shouldworkHour:
            normal_salary = shouldworkHour * 10
        elif worktime == shouldworkHour:
            normal_salary = (shouldworkHour * 10)+5
        else:
            normal_salary = worktime * 10

        # Calculate overtime salary
        if worktime > shouldworkHour:
            overtime_hours = worktime - shouldworkHour
            overtime_salary = overtime_hours * 20
        else:
            overtime_salary = 0

        # Calculate bonus
        if worktime >shouldworkHour:
            bonus = 12
        else:
            bonus = 0

        # Calculate total salary
        total_salary = normal_salary + overtime_salary + bonus

        # Print the total salary for each employee
        print(f"{em['name']}'s total salary is: {total_salary}")

totalsal()
