# Sorting Algorithm Visualizer

This Python program visualizes the sorting algorithms: Bubble Sort, Insertion Sort, and Selection Sort. It uses the Pygame library for graphical display.

## Requirements

- Python 3.x
- Pygame library

## Usage

1. Make sure you have Python installed.
2. Install the Pygame library (`pip install pygame`).
3. Run the script.
4. Press keys to interact with the visualizer:
   - **r**: Generate a new random array.
   - **Space**: Start/stop sorting.
   - **a/d**: Toggle between ascending and descending order.
   - **b/i/s**: Switch between Bubble Sort, Insertion Sort, and Selection Sort.

## Features

- Visualizes the sorting process in real-time.
- Allows toggling between ascending and descending order.
- Supports three different sorting algorithms.
- Displays elapsed time during sorting.

## Code Structure

- `SortingVisualizer` class manages the visualization and sorting algorithms.
- Three sorting algorithms are implemented as methods within the class.
- Pygame is used for drawing bars and UI elements.
