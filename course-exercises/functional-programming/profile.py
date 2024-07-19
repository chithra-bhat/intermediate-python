"""Write a function that prints a profile, given values."""


def create_profile(given_name, *surnames, **details):
    name = given_name
    for surname in surnames:
        name += " " + surname
    print("\n" + name)
    for key, info in details.items():
        print(f"{key}: {info}")


if __name__ == '__main__':
    create_profile("Sam")
    create_profile('Sam', role='Instructor')
    create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1968)
    create_profile("Sebastian", "Thrun",
                   cofounded="Udacity", experience="Stanford Professor")
