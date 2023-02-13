def calculate_energy(mass):
    return mass * square(300000000)


def square(n):
    return n * n


def main():
    mass = int(input("What is the mass of this object in kilograms? "))
    energy = calculate_energy(mass)
    print(f"Its energy is {energy}joules")


main()
