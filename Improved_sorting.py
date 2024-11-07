import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import time
from ttkthemes import ThemedTk
import sys

sys.setrecursionlimit(1500)

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry("900x700")
        
        # Set theme
        self.root.set_theme("equilux")
        
        # Variables
        self.numbers = []
        self.algorithm = tk.StringVar()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill="both", expand=True)
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Title with custom styling
        title_frame = ttk.Frame(self.main_frame)
        title_frame.pack(fill="x", pady=(0, 20))
        
        title = ttk.Label(title_frame, 
                         text="Sorting Algorithm Analyzer",
                         font=("Helvetica", 24, "bold"))
        title.pack()
        
        subtitle = ttk.Label(title_frame,
                           text="Analyze and compare different sorting algorithms",
                           font=("Helvetica", 12))
        subtitle.pack()
        
        # Control Panel
        control_frame = ttk.LabelFrame(self.main_frame, text="Control Panel", padding="10")
        control_frame.pack(fill="x", pady=(0, 20))
        
        # File selection
        file_frame = ttk.Frame(control_frame)
        file_frame.pack(fill="x", pady=5)
        
        select_btn = ttk.Button(file_frame, 
                              text="Select Input File",
                              command=self.select_file)
        select_btn.pack(side="left", padx=5)
        
        self.file_label = ttk.Label(file_frame, text="No file selected")
        self.file_label.pack(side="left", padx=5)
        
        # Algorithm selection
        algo_frame = ttk.Frame(control_frame)
        algo_frame.pack(fill="x", pady=5)
        
        algo_label = ttk.Label(algo_frame, text="Select Algorithm:")
        algo_label.pack(side="left", padx=5)
        
        algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 
                     'Quick Sort', 'Merge Sort', 'Heap Sort', 'Radix Sort', 
                     'Counting Sort', 'Shell Sort', 'Bucket Sort']
        self.algo_dropdown = ttk.Combobox(algo_frame, 
                                        textvariable=self.algorithm,
                                        values=algorithms,
                                        state="readonly",
                                        width=30)
        self.algo_dropdown.pack(side="left", padx=5)
        self.algo_dropdown.set(algorithms[0])
        self.algo_dropdown.bind('<<ComboboxSelected>>', self.show_algorithm_code)
        # Button frame for Sort and Save buttons
        button_frame = ttk.Frame(control_frame)
        button_frame.pack(pady=10)
        
        # Sort button
        sort_btn = ttk.Button(button_frame,
                            text="Start Sorting",
                            command=self.sort_numbers)
        sort_btn.pack(side="left", padx=5)
        
        # Save button
        self.save_btn = ttk.Button(button_frame,
                                text="Save Output",
                                command=self.save_output,
                                state="enable")  # Initially disabled
        self.save_btn.pack(side="left", padx=5)
        
        
        # Results frame
        self.result_frame = ttk.LabelFrame(self.main_frame, text="Results", padding="10")
        self.result_frame.pack(fill="x", pady=10)
        
        self.time_label = ttk.Label(self.result_frame,
                                  text="Time taken: -",
                                  font=("Helvetica", 11))
        self.time_label.pack(pady=5)
        
        self.shifts_label = ttk.Label(self.result_frame,
                                    text="Shifts/Comparisons: -",
                                    font=("Helvetica", 11))
        self.shifts_label.pack(pady=5)
        
        self.cost_label = ttk.Label(self.result_frame,
                                  text="Computational cost: -",
                                  font=("Helvetica", 11))
        self.cost_label.pack(pady=5)
        
        # Status bar
        self.status_bar = ttk.Label(self.main_frame,
                                  text="Ready",
                                  relief="sunken",
                                  anchor="w")
        self.status_bar.pack(fill="x", side="bottom", pady=(10, 0))

    def save_output(self):
        if not self.numbers:
            messagebox.showerror("Error", "No sorted data to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Sorted Numbers"
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    # Write sorted numbers
                    file.write("Sorted Numbers:\n")
                    file.write(" ".join(map(str, self.numbers)))
                    file.write("\n\n")
                    
                    # Write analysis results
                    file.write("Analysis Results:\n")
                    file.write(f"Algorithm: {self.algorithm.get()}\n")
                    file.write(f"{self.time_label['text']}\n")
                    file.write(f"{self.shifts_label['text']}\n")
                    file.write(f"{self.cost_label['text']}\n")
                
                self.status_bar.config(text=f"Results saved to {os.path.basename(file_path)}")
                messagebox.showinfo("Success", "Results saved successfully!")
            except Exception as e:
                self.status_bar.config(text="Error saving results")
                messagebox.showerror("Error", f"Failed to save results: {str(e)}")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.numbers = [int(num) for num in file.read().split()]
                self.file_label.config(text=os.path.basename(file_path))
                self.status_bar.config(text=f"Loaded {len(self.numbers)} numbers successfully")
                messagebox.showinfo("Success", "File loaded successfully!")
            except Exception as e:
                self.status_bar.config(text="Error loading file")
                messagebox.showerror("Error", f"Invalid file format! {str(e)}")

    def show_algorithm_code(self, event=None):
        algorithm = self.algorithm.get()
        codes = {
        'Bubble Sort': '''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr''',
        
        'Selection Sort': '''def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr''',
        
        'Insertion Sort': '''def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr''',
        
        'Quick Sort': '''def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)''',
        
        'Merge Sort': '''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result''',
        
        'Heap Sort': '''def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr''',
        
        'Radix Sort': '''def radix_sort(arr):
    def counting_sort_radix(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        for i in range(n):
            arr[i] = output[i]
    
    if not arr:
        return arr
        
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    
    return arr''',
        
        'Counting Sort': '''def counting_sort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    count = [0] * range_val
    output = [0] * len(arr)
    
    for i in arr:
        count[i - min_val] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr''',
        
        'Shell Sort': '''def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr''',
        
        'Bucket Sort': '''def bucket_sort(arr):
    if not arr:
        return arr
        
    # Find minimum and maximum values
    max_val = max(arr)
    min_val = min(arr)
    
    # Number of buckets, using sqrt(n) as optimal
    n = len(arr)
    bucket_count = int(n ** 0.5)
    
    # Create buckets
    buckets = [[] for _ in range(bucket_count)]
    
    # Range of each bucket
    bucket_range = (max_val - min_val) / bucket_count + 1
    
    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        # Handle edge case for maximum value
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
    
    # Sort individual buckets
    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])
    
    # Concatenate all buckets into final result
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    # Copy result back to original array
    for i in range(len(arr)):
        arr[i] = result[i]
    
    return arr'''
    }   
        code_window = tk.Toplevel(self.root)
        code_window.title(f"{algorithm} Implementation")
        code_window.geometry("600x400")
        
        code_text = tk.Text(code_window, font=("Courier", 12), wrap=tk.NONE)
        code_text.pack(fill=tk.BOTH, expand=True)
        
        y_scrollbar = ttk.Scrollbar(code_window, orient=tk.VERTICAL, command=code_text.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        x_scrollbar = ttk.Scrollbar(code_window, orient=tk.HORIZONTAL, command=code_text.xview)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        code_text.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        code_text.insert(tk.END, codes[algorithm])
        code_text.config(state=tk.DISABLED)

    def sort_numbers(self):
        if not self.numbers:
            self.status_bar.config(text="Error: No input file selected")
            messagebox.showerror("Error", "Please select a file first!")
            return
        
        self.shifts = 0  # Reset shifts counter
        algorithm = self.algorithm.get()
        self.status_bar.config(text="Sorting in progress...")
        
        start_time = time.time()
        
        # Sorting algorithms
        sorting_methods = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort,
            "Quick Sort": self.quick_sort,
            "Merge Sort": self.merge_sort,
            "Heap Sort": self.heap_sort,
            "Radix Sort": self.radix_sort,
            "Counting Sort": self.counting_sort,
            "Shell Sort": self.shell_sort,
            "Bucket Sort": self.bucket_sort
        }
        
        # Create a copy of numbers to sort
        numbers_to_sort = self.numbers.copy()
        if algorithm in sorting_methods:
            sorted_numbers = sorting_methods[algorithm](numbers_to_sort)
            self.numbers = sorted_numbers
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Update results
        self.time_label.config(text=f"Time taken: {time_taken:.6f} seconds")
        self.shifts_label.config(text=f"Shifts/Comparisons: {self.shifts}")
        
        # Calculate computational cost
        costs = {
            "Bubble Sort": "O(n²)",
            "Selection Sort": "O(n²)",
            "Insertion Sort": "O(n²)",
            "Quick Sort": "O(n log n)",
            "Merge Sort": "O(n log n)",
            "Heap Sort": "O(n log n)",
            "Radix Sort": "O(nk)",
            "Counting Sort": "O(n+k)",
            "Shell Sort": "O(n log² n)",
            "Bucket Sort": "O(n+k)"
        }
        
        self.cost_label.config(text=f"Computational cost: {costs.get(algorithm, 'Unknown')}")
        self.status_bar.config(text="Sorting completed!")

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                self.shifts += 1
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                self.shifts += 1
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                self.shifts += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        self.shifts += len(arr) - 1
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            self.shifts += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def heap_sort(self, arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
                
            if largest != i:
                self.shifts += 1
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        
        return arr

    def counting_sort(self, arr):
        if not arr:
            return arr
            
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        count = [0] * range_val
        output = [0] * len(arr)
        
        for i in arr:
            count[i - min_val] += 1
            self.shifts += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
            self.shifts += 1
        
        for i in range(len(arr)):
            arr[i] = output[i]
        
        return arr

    def radix_sort(self, arr):
        def counting_sort_radix(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1
                self.shifts += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1
                self.shifts += 1
            
            for i in range(n):
                arr[i] = output[i]
        
        if not arr:
            return arr
            
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            counting_sort_radix(arr, exp)
            exp *= 10
        
        return arr

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                
                while j >= gap and arr[j - gap] > temp:
                    self.shifts += 1
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        
        return arr

    def bucket_sort(self, arr):
        if not arr:
            return arr
            
        # Find minimum and maximum values
        max_val = max(arr)
        min_val = min(arr)
        
        # Number of buckets, using sqrt(n) as it's typically optimal
        n = len(arr)
        bucket_count = int(n ** 0.5)
        
        # Create buckets
        buckets = [[] for _ in range(bucket_count)]
        
        # Range of each bucket
        bucket_range = (max_val - min_val) / bucket_count + 1
        
        # Distribute elements into buckets
        for num in arr:
            index = int((num - min_val) / bucket_range)
            # Handle edge case for maximum value
            if index == bucket_count:
                index -= 1
            buckets[index].append(num)
            self.shifts += 1
        
        # Sort individual buckets using insertion sort
        for i in range(bucket_count):
            buckets[i] = self.insertion_sort(buckets[i])
        
        # Concatenate all buckets into final result
        result = []
        for bucket in buckets:
            result.extend(bucket)
            self.shifts += len(bucket)
        
        # Copy result back to original array
        for i in range(len(arr)):
            arr[i] = result[i]
        
        return arr

def main():
    root = ThemedTk(theme="equilux")
    app = SortingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()