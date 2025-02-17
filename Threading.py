import threading
import numpy as np

# Function to sum two vectors
def sum_vectors(v1, v2, result, index):
    result[index] = v1[index] + v2[index]

# Function to multiply a vector by a matrix
def multiply_vector_matrix(vector, matrix, result, index):
    result[index] = np.dot(matrix[index], vector)

# Main function
def main():
    # Define vectors and matrix
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Initialize result vectors
    sum_result = np.zeros(len(vector1))
    mult_result = np.zeros(len(vector1))

    # Create threads for vector summation
    sum_threads = []
    for i in range(len(vector1)):
        thread = threading.Thread(target=sum_vectors, args=(vector1, vector2, sum_result, i))
        sum_threads.append(thread)
        thread.start()

    # Wait for all summation threads to finish
    for thread in sum_threads:
        thread.join()

    # Create threads for vector-matrix multiplication
    mult_threads = []
    for i in range(len(vector1)):
        thread = threading.Thread(target=multiply_vector_matrix, args=(sum_result, matrix, mult_result, i))
        mult_threads.append(thread)
        thread.start()

    # Wait for all multiplication threads to finish
    for thread in mult_threads:
        thread.join()

    # Print results
    print("Sum of vectors:", sum_result)
    print("Multiplication result:", mult_result)

if __name__ == "__main__":
    main()