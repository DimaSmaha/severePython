employees = [
    {"name": "Oleksandr Petrenko", "experience": 5, "position": "Developer"},
    {"name": "Maria Kovalenko", "experience": 2, "position": "Designer"},
    {"name": "Ivan Sydorenko", "experience": 7, "position": "Project Manager"},
    {"name": "Anna Melnyk", "experience": 1, "position": "Tester"},
    {"name": "Serhii Bondarenko", "experience": 4, "position": "Analyst"},
    {"name": "Kateryna Shevchenko", "experience": 6, "position": "Architect"},
    {"name": "Oleksandr Hrytsenko", "experience": 3, "position": "DevOps Engineer"},
]

# Create a function that takes array above and return unique first names for employees work 3 and more years


def three_years_employees(employees_list: list) -> list:
    filtered_arr = set()

    for el in employees_list:
        if el["experience"] >= 3:
            el["name"] = (el["name"]).split(' ')[0]
            filtered_arr.add(el.get('name'))

    return list(filtered_arr)


print(three_years_employees(employees))


def three_years_employees_remove_dublicates(employees_list: list) -> list:
    filtered_arr = dict()

    count = 0
    for el in employees_list:
        if el["experience"] >= 3:
            el["name"] = (el["name"]).split(' ')[0]
            if (el["name"] not in str(filtered_arr.values())):
                filtered_arr[count] = (el.get('name'))
                count += 1

    return list(filtered_arr.values())


print(three_years_employees_remove_dublicates(employees))
