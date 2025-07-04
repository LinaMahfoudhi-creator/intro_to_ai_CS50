import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory. aka the set of dictionaries
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data("small")
    print("Data loaded.")
    # Initialize Frontier
    #source and target are ids of the people
    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    # the goal
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

def shortest_path(source, target):

    #Initialize the frontier with the source node
    frontier= QueueFrontier()
    frontier.add(Node(state=source, parent=None, action=None))

    #keep track of the number of states explored
    frontier.num_explored = 0

    #Initialize the explored set
    frontier.explored = set()
    frontier.explored.add(source)

    #Loop until we find the target or the frontier is empty
    while True:
        if frontier.empty():
            return None

        # Choose a node from the frontier
        node = frontier.remove()
        frontier.num_explored += 1 #we explored the first node aka source

        # If node is the goal, then we have a solution
        if node.state == target:
            # Reconstruct the path from the source to the target
            path = []
            while node.parent is not None:
                #recursively add the action and state to the path
                path.append((node.action, node.state))
                node = node.parent
            return path[::-1]  # Return reversed path

        frontier.explored.add(node)
        # Expand the node and add its neighbors to the frontier
        for movie_id, person_id in neighbors_for_person(node.state):
            if not frontier.contains_state(person_id) and person_id not in frontier.explored:
                # Add the neighbor to the frontier
                frontier.add(Node(state=person_id, parent=node, action=movie_id))
                # Mark the neighbor as explored
                frontier.explored.add(person_id)


# This function should return the IMDB id for a person's name,
def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else: # Only one person with that name
        return person_ids[0]

#Returns all costars of a given person
def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
            # returns the action (movie_id) and the state (person_id)
    return neighbors


if __name__ == "__main__":
    main()
