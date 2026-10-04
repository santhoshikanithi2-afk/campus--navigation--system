# Design Decisions

## 1. Graph Representation

The campus is represented as a weighted graph.

- Each campus location is a node.
- Each road/path between two locations is an edge.
- The distance between locations is stored as the edge weight in metres.

## 2. Algorithm

Dijkstra's shortest path algorithm is used to find the shortest route between two campus locations.

Dijkstra's algorithm is suitable because all distances in the campus map are positive.

## 3. Data Structure

A Python dictionary is used as an adjacency list to represent the campus graph.

A priority queue using Python's `heapq` module is used by Dijkstra's algorithm.

## 4. Campus Locations

The current prototype contains:

- Gate 1
- Gate 2
- Gate 3
- Auditorium
- Cafeteria
- Library
- CSE Block
- Playground
- Girls Hostel
- Boys Hostel
- Sports Hall

## 5. Current Scope

The current version is a command-line prototype.

The user enters a starting location and destination, and the system calculates the shortest route and total distance.

## 6. Future Improvements

Future versions can include:

- Graphical campus map
- Web interface
- Mobile application
- GPS/current-location support
- Search suggestions
- Multiple route options
- Accessibility-friendly routes
