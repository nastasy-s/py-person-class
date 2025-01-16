class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_dict in people:
        name = person_dict['name']
        age = person_dict['age']
        person = Person(name, age)

        if 'wife' in person_dict and person_dict['wife']:
            if person_dict['wife'] in Person.people:
                person.wife = Person.people[person_dict['wife']]
            else:
                print(f"Warning: Spouse '{person_dict['wife']}' not found for {person.name}")

        elif 'husband' in person_dict and person_dict['husband']:
            if person_dict['husband'] in Person.people:
                person.husband = Person.people[person_dict['husband']]
            else:
                print(f"Warning: Spouse '{person_dict['husband']}' not found for {person.name}")
            person_instances.append(person)
    return person_instances





