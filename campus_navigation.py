import heapq

# Campus map represented as a weighted graph
graph = {
    "Gate 1": {
        "Auditorium": 10,
        "Playground": 100
    },

    "Auditorium": {
        "Gate 1": 10,
        "Cafeteria": 15,
        "Gate 2": 100
    },

    "Cafeteria": {
        "Auditorium": 15,
        "Library": 10
    },

    "Library": {
        "Cafeteria": 10,
        "CSE Block": 5,
        "Playground": 15
    },

    "CSE Block": {
        "Library": 5,
        "Sports Hall": 10
    },

    "Playground": {
        "Gate 1": 100,
        "Library": 15,
        "Girls Hostel": 5,
        "Boys Hostel": 5
    },

    "Gate 2": {
        "Auditorium": 100,
        "Sports Hall": 50
    },

    "Sports Hall": {
        "Gate 2": 50,
        "CSE Block": 10,
        "Boys Hostel": 10
    },

    "Girls Hostel": {
        "Playground": 5,
        "Gate 3": 20
    },

    "Boys Hostel": {
        "Playground": 5,
        "Sports Hall": 10
    },

    "Gate 3": {
        "Girls Hostel": 20
    }
}


def dijkstra(graph, start, destination):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == destination:
            break

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                previous[neighbour] = current_node
                heapq.heappush(priority_queue, (distance, neighbour))

    # Build shortest path
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if distances[destination] == float("inf"):
        return None, float("inf")

    return path, distances[destination]


print("=== CAMPUS NAVIGATION SYSTEM ===")

print("\nAvailable locations:")
for location in graph:
    print("-", location)

source = input("\nEnter starting location: ")
destination = input("Enter destination: ")

if source not in graph or destination not in graph:
    print("\nInvalid location!")
else:
    path, distance = dijkstra(graph, source, destination)

    if path is None:
        print("\nNo route found.")
    else:
        print("\nShortest route:")
        print(" -> ".join(path))
        print("Total distance:", distance, "m")
