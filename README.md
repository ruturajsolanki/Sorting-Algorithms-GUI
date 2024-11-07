# Sorting Algorithm Visualizer

This Python application is a graphical tool that visualizes and analyzes various sorting algorithms. It is designed with a user-friendly interface built using Tkinter and ttkthemes, enabling users to load data, select sorting algorithms, view performance metrics, and save results.

## Features

- **Sorting Algorithm Selection**: Choose from a range of popular sorting algorithms:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort
  - Merge Sort
  - Heap Sort
  - Radix Sort
  - Counting Sort
  - Shell Sort
  - Bucket Sort
- **Data Input**: Load numbers from a text file for easy analysis of large datasets.
- **Performance Metrics**: View time taken, number of shifts/comparisons, and complexity for each algorithm.
- **Save Results**: Export sorted data and analysis to a text file.
- **Code Viewer**: View Python code for each algorithm in a dedicated window.

## Screenshots

### Main Interface
![Main Interface](path/to/main_interface_screenshot.png)

### Algorithm Code Viewer
![Algorithm Code Viewer](path/to/code_viewer_screenshot.png)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sorting-algorithm-visualizer.git
   ```

2. **Install required packages**:
   ```bash
   pip install ttkthemes
   ```
   *Note: Tkinter is included with Python, so no additional installation is required for it.*

3. **Run the application**:
   ```bash
   python Improved_sorting.py
   ```

## Usage

1. **Load Input Data**: Click on "Load File" to select a text file with numbers to be sorted.
2. **Select Sorting Algorithm**: Choose an algorithm from the dropdown menu.
3. **Start Sorting**: Press "Start Sorting" to visualize the process and see the results.
4. **Save Results**: Once sorting is completed, you can save the sorted list and metrics to a file.

## Project Structure

- `main.py`: Main file to launch the application.
- `algorithms.py`: Contains implementations of sorting algorithms.
- `ui.py`: Code related to the graphical user interface.
- `utils.py`: Utility functions for file handling and data processing.

## Sorting Algorithms Implemented

Each sorting algorithm is implemented with a focus on providing real-time visualization and performance metrics.

- **Bubble Sort**: Simple comparison-based algorithm.
- **Selection Sort**: Iteratively selects the minimum element.
- **Insertion Sort**: Efficient for small data or partially sorted lists.
- **Quick Sort**: Efficient, recursive, divide-and-conquer approach.
- **Merge Sort**: Recursive sorting with guaranteed O(n log n) complexity.
- **Heap Sort**: Builds a heap to efficiently sort elements.
- **Radix Sort**: Efficient non-comparative sorting for integers.
- **Counting Sort**: Non-comparative sorting with counting array.
- **Shell Sort**: Generalized insertion sort with gap sorting.
- **Bucket Sort**: Distributes elements into buckets and sorts individually.

## Performance Analysis

The application provides insights into the following metrics for each sorting operation:

- **Time Complexity**: Runtime complexity notation (e.g., O(n^2), O(n log n)).
- **Execution Time**: Time taken for the algorithm to complete.
- **Shift/Comparison Counts**: Number of data shifts or comparisons made by the algorithm.

## Example Data File Format

The application expects a plain text file with numbers separated by spaces, commas, or new lines, like so:

```
10, 24, 76, 34, 89, 12
```

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.


## Contact

For any inquiries, feel free to reach out via:

- Email: ruturajsolanki43@gmail.com
- GitHub: @ruturajsolanki

Enjoy using the Sorting Algorithm Visualizer for educational purposes and feel free to suggest new features or algorithms!
