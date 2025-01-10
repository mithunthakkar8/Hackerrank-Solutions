import operator  # Importing the operator module (not used in this code but can be useful in similar scenarios)

# A decorator function to process and sort a list of people
def person_lister(f):
    def inner(people):
        # Sort the list of people by age (3rd element in each sublist, converted to integer)
        people = sorted(people, key=lambda x: int(x[2]))
        
        # Use a generator to apply the decorated function `f` to each person in the sorted list
        for person in people:
            yield f(person)
    return inner

# Function to format a person's name based on gender
@person_lister
def name_format(person):
    # Determine title based on gender and return formatted name
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # Input a list of people
    # Each person has details: [First Name, Last Name, Age, Gender]
    people = [input().split() for i in range(int(input()))]

    # Apply the name_format function to the sorted list of people and print the results
    # Each name will be printed on a new line
    print(*name_format(people), sep='\n')
