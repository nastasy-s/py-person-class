class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f"Person(name=\\\"{self.name}\\\", age={self.age})"


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    result: list[Person] = []
    for data in people:
        result.append(Person(data["name"], data["age"]))
    for data in people:
        person = Person.people[data["name"]]
        for key in ("wife", "husband"):
            spouse_name = data.get(key)
            if spouse_name is not None:
                try:
                    setattr(person, key, Person.people[spouse_name])
                except KeyError:
                    raise ValueError(
                        f"Spouse \\\"{spouse_name}\\\" for \\\"{person.name}\\\" not found in people list"
                    )
    return result






