import numpy as np


# ============================================================
# PR. 8 - NUMPY ANALYZER
# ============================================================

#=============================================================
# HITESH  CHAUDHARY
#=============================================================

class DataAnalytics:
    """
    NumPy Analyzer using Object-Oriented Programming.
    """


    def __init__(self, array=None):
        """
        Constructor to initialize the array.
        """

        if array is None:
            self.array = np.array([])
        else:
            self.array = np.array(array)

    def __validate_array(self):
        """
        Private method to validate array.
        """

        if self.array.size == 0:
            raise ValueError("Array is empty.")


    def __display_array(self, title="Array"):
        """
        Private method to display array.
        """

        print(f"\n{title}:")
        print(self.array)


    @classmethod
    def from_list(cls, values):
        """
        Class method to create object from list.
        """

        return cls(np.array(values))


    @staticmethod
    def get_numpy_version():
        """
        Static method to display NumPy version.
        """

        return np.__version__

    def create_array(self, dimension):
        """
        Create 1D, 2D or 3D NumPy array.
        """


        if dimension == 1:

            try:

                n = int(
                    input("Enter the number of elements: ")
                )

                values = input(
                    "Enter elements separated by spaces: "
                ).split()

                if len(values) != n:

                    print(
                        f"Please enter exactly {n} elements."
                    )

                    return False

                self.array = np.array(
                    [int(x) for x in values]
                )

                print("\nArray created successfully!")
                print(self.array)

                return True

            except ValueError:

                print(
                    "Please enter valid numbers."
                )

                return False


        elif dimension == 2:

            try:

                rows = int(
                    input("Enter the number of rows: ")
                )

                columns = int(
                    input("Enter the number of columns: ")
                )

                print(
                    f"Enter {rows * columns} values "
                    f"for the array:"
                )

                values = input().split()

                if len(values) != rows * columns:

                    print(
                        f"Please enter exactly "
                        f"{rows * columns} values."
                    )

                    return False

                values = [
                    int(x)
                    for x in values
                ]

                self.array = np.array(
                    values
                ).reshape(
                    rows,
                    columns
                )

                print("\nArray created successfully!")
                print(self.array)

                return True

            except ValueError:

                print(
                    "Please enter valid numbers."
                )

                return False


        elif dimension == 3:

            try:

                depth = int(
                    input("Enter depth: ")
                )

                rows = int(
                    input("Enter number of rows: ")
                )

                columns = int(
                    input("Enter number of columns: ")
                )

                total = (
                    depth *
                    rows *
                    columns
                )

                print(
                    f"Enter {total} values:"
                )

                values = input().split()

                if len(values) != total:

                    print(
                        f"Please enter exactly "
                        f"{total} values."
                    )

                    return False

                values = [
                    int(x)
                    for x in values
                ]

                self.array = np.array(
                    values
                ).reshape(
                    depth,
                    rows,
                    columns
                )

                print("\nArray created successfully!")
                print(self.array)

                return True

            except ValueError:

                print(
                    "Please enter valid numbers."
                )

                return False

        else:

            print("Invalid dimension.")

            return False

    def array_management(self):

        while True:

            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.__validate_array()

                try:

                    if self.array.ndim == 1:

                        index = int(
                            input(
                                "Enter index: "
                            )
                        )

                        print(
                            "Element:",
                            self.array[index]
                        )

                    elif self.array.ndim == 2:

                        row = int(
                            input(
                                "Enter row index: "
                            )
                        )

                        column = int(
                            input(
                                "Enter column index: "
                            )
                        )

                        print(
                            "Element:",
                            self.array[
                                row,
                                column
                            ]
                        )

                    elif self.array.ndim == 3:

                        depth = int(
                            input(
                                "Enter depth index: "
                            )
                        )

                        row = int(
                            input(
                                "Enter row index: "
                            )
                        )

                        column = int(
                            input(
                                "Enter column index: "
                            )
                        )

                        print(
                            "Element:",
                            self.array[
                                depth,
                                row,
                                column
                            ]
                        )

                except IndexError:

                    print(
                        "Index out of range."
                    )

                except ValueError:

                    print(
                        "Please enter valid indices."
                    )

            elif choice == "2":

                self.__validate_array()

                try:

                    if self.array.ndim == 1:

                        start = int(
                            input(
                                "Enter start index: "
                            )
                        )

                        end = int(
                            input(
                                "Enter end index: "
                            )
                        )

                        print(
                            "Sliced Array:"
                        )

                        print(
                            self.array[
                                start:end
                            ]
                        )

                    elif self.array.ndim == 2:

                        print(
                            "Example: 0:2, 1:3"
                        )

                        row_range = input(
                            "Enter the row range "
                            "(start:end): "
                        )

                        column_range = input(
                            "Enter the column range "
                            "(start:end): "
                        )

                        r_start, r_end = map(
                            int,
                            row_range.split(":")
                        )

                        c_start, c_end = map(
                            int,
                            column_range.split(":")
                        )

                        print(
                            "Sliced Array:"
                        )

                        print(
                            self.array[
                                r_start:r_end,
                                c_start:c_end
                            ]
                        )

                    else:

                        print(
                            "Slicing for 3D array:"
                        )

                        print(
                            self.array[
                                :,
                                :,
                                :
                            ]
                        )

                except ValueError:

                    print(
                        "Invalid slicing input."
                    )


            elif choice == "3":

                break

            else:

                print(
                    "Invalid choice."
                )

    def mathematical_operations(self):

        self.__validate_array()

        if self.array.ndim != 1:

            print(
                "\nFor this menu, use a 1D array."
            )

            return

        try:

            print("\nChoose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot Product")
            print("6. Matrix Multiplication")

            choice = input(
                "Enter your choice: "
            )

            n = len(self.array)

            values = input(
                f"Enter the second array "
                f"({n} elements separated by spaces): "
            ).split()

            if len(values) != n:

                print(
                    f"Please enter exactly {n} elements."
                )

                return

            second_array = np.array(
                [int(x) for x in values]
            )

            print("\nOriginal Array:")
            print(self.array)

            print("\nSecond Array:")
            print(second_array)

            if choice == "1":

                result = (
                    self.array +
                    second_array
                )

                print("\nResult of Addition:")
                print(result)

            elif choice == "2":

                result = (
                    self.array -
                    second_array
                )

                print("\nResult of Subtraction:")
                print(result)

            elif choice == "3":

                result = (
                    self.array *
                    second_array
                )

                print(
                    "\nResult of Multiplication:"
                )

                print(result)


            elif choice == "4":

                if np.any(second_array == 0):

                    print(
                        "Division by zero is not allowed."
                    )

                    return

                result = (
                    self.array /
                    second_array
                )

                print(
                    "\nResult of Division:"
                )

                print(result)


            elif choice == "5":

                result = np.dot(
                    self.array,
                    second_array
                )

                print(
                    "\nDot Product:"
                )

                print(result)

            elif choice == "6":

                print(
                    "\nMatrix multiplication "
                    "requires 2D arrays."
                )

                print(
                    "Convert arrays to matrices "
                    "before using this operation."
                )

            else:

                print(
                    "Invalid choice."
                )

        except ValueError:

            print(
                "Please enter valid numbers."
            )


    def combine_split(self):

        while True:

            print("\nChoose an operation:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            choice = input(
                "Enter your choice: "
            )


            if choice == "1":

                try:

                    print(
                        "\nEnter the elements "
                        "of first array:"
                    )

                    first = np.array(
                        [
                            int(x)
                            for x in input().split()
                        ]
                    )

                    print(
                        "Enter the elements "
                        "of second array:"
                    )

                    second = np.array(
                        [
                            int(x)
                            for x in input().split()
                        ]
                    )

                    print("\nFirst Array:")
                    print(first)

                    print("\nSecond Array:")
                    print(second)

                    combined = np.vstack(
                        (
                            first,
                            second
                        )
                    )

                    print(
                        "\nCombined Array "
                        "(Vertical Stack):"
                    )

                    print(combined)

                except ValueError:

                    print(
                        "Please enter valid numbers."
                    )

            elif choice == "2":

                try:

                    self.__validate_array()

                    parts = int(
                        input(
                            "Enter number of parts: "
                        )
                    )

                    result = np.array_split(
                        self.array,
                        parts
                    )

                    print(
                        "\nSplit Arrays:"
                    )

                    for i, part in enumerate(
                        result,
                        start=1
                    ):

                        print(
                            f"Array {i}:"
                        )

                        print(part)

                except ValueError:

                    print(
                        "Please enter a valid number."
                    )

            elif choice == "3":

                break

            else:

                print(
                    "Invalid choice."
                )

    def search_sort_filter(self):

        self.__validate_array()

        while True:

            print("\nChoose an operation:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")

            choice = input(
                "Enter your choice: "
            )


            if choice == "1":

                try:

                    value = int(
                        input(
                            "Enter value to search: "
                        )
                    )

                    positions = np.where(
                        self.array == value
                    )

                    if len(positions[0]) > 0:

                        print(
                            "Value found at index:",
                            positions
                        )

                    else:

                        print(
                            "Value not found."
                        )

                except ValueError:

                    print(
                        "Please enter a valid number."
                    )

            elif choice == "2":

                print(
                    "\n1. Ascending"
                )

                print(
                    "2. Descending"
                )

                order = input(
                    "Enter your choice: "
                )

                if order == "1":

                    sorted_array = np.sort(
                        self.array,
                        axis=None
                    )

                    print(
                        "Sorted Array:"
                    )

                    print(
                        sorted_array
                    )

                elif order == "2":

                    sorted_array = np.sort(
                        self.array,
                        axis=None
                    )[::-1]

                    print(
                        "Sorted Array:"
                    )

                    print(
                        sorted_array
                    )

                else:

                    print(
                        "Invalid choice."
                    )

            elif choice == "3":

                try:

                    condition = input(
                        "Enter filter condition "
                        "(example: > 30): "
                    )

                    if condition.startswith(">"):

                        value = float(
                            condition[1:]
                        )

                        result = (
                            self.array[
                                self.array > value
                            ]
                        )

                    elif condition.startswith("<"):

                        value = float(
                            condition[1:]
                        )

                        result = (
                            self.array[
                                self.array < value
                            ]
                        )

                    elif condition.startswith(">="):

                        value = float(
                            condition[2:]
                        )

                        result = (
                            self.array[
                                self.array >= value
                            ]
                        )

                    elif condition.startswith("<="):

                        value = float(
                            condition[2:]
                        )

                        result = (
                            self.array[
                                self.array <= value
                            ]
                        )

                    else:

                        print(
                            "Use >, <, >= or <=."
                        )

                        continue

                    print(
                        "Filtered Array:"
                    )

                    print(result)

                except ValueError:

                    print(
                        "Invalid condition."
                    )

            elif choice == "4":

                break

            else:

                print(
                    "Invalid choice."
                )


    def aggregates_statistics(self):

        self.__validate_array()

        while True:

            print(
                "\nChoose an aggregate/statistical operation:"
            )

            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentiles")
            print("9. Correlation Coefficient")
            print("10. Go Back")

            choice = input(
                "Enter your choice: "
            )

            if choice == "1":

                print(
                    "Sum:",
                    np.sum(self.array)
                )

            elif choice == "2":

                print(
                    "Mean:",
                    np.mean(self.array)
                )


            elif choice == "3":

                print(
                    "Median:",
                    np.median(self.array)
                )

            elif choice == "4":

                print(
                    "Standard Deviation:",
                    np.std(self.array)
                )


            elif choice == "5":

                print(
                    "Variance:",
                    np.var(self.array)
                )

            elif choice == "6":

                print(
                    "Minimum:",
                    np.min(self.array)
                )


            elif choice == "7":

                print(
                    "Maximum:",
                    np.max(self.array)
                )

            elif choice == "8":

                try:

                    percentile = float(
                        input(
                            "Enter percentile "
                            "(0-100): "
                        )
                    )

                    if (
                        percentile < 0
                        or percentile > 100
                    ):

                        print(
                            "Percentile must be "
                            "between 0 and 100."
                        )

                    else:

                        result = np.percentile(
                            self.array,
                            percentile
                        )

                        print(
                            f"{percentile}th Percentile:",
                            result
                        )

                except ValueError:

                    print(
                        "Please enter a valid number."
                    )

            elif choice == "9":

                try:

                    print(
                        "Enter second array "
                        "with same number of elements:"
                    )

                    values = input().split()

                    if len(values) != self.array.size:

                        print(
                            "Both arrays must have "
                            "the same number of elements."
                        )

                        continue

                    second = np.array(
                        [
                            float(x)
                            for x in values
                        ]
                    )

                    first_flat = self.array.flatten()

                    correlation = np.corrcoef(
                        first_flat,
                        second
                    )[0, 1]

                    print(
                        "Correlation Coefficient:",
                        correlation
                    )

                except ValueError:

                    print(
                        "Please enter valid numbers."
                    )

            elif choice == "10":

                break

            else:

                print(
                    "Invalid choice."
                )


def main():

    # Create object using constructor
    analyzer = DataAnalytics()

    print("\n========================================")
    print("Welcome to the NumPy Analyzer!")
    print("========================================")

    while True:

        print("\nChoose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input(
            "Enter your choice: "
        )
        if choice == "1":

            print("\nArray Creation:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            dimension = input(
                "Enter your choice: "
            )

            if dimension in ["1", "2", "3"]:

                analyzer.create_array(
                    int(dimension)
                )

                while True:

                    print(
                        "\nChoose an operation:"
                    )

                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")

                    operation = input(
                        "Enter your choice: "
                    )

                    if operation == "1":

                        try:

                            analyzer.array_management()

                        except ValueError as e:

                            print(e)

                        break

                    elif operation == "2":

                        try:

                            analyzer.array_management()

                        except ValueError as e:

                            print(e)

                        break

                    elif operation == "3":

                        break

                    else:

                        print(
                            "Invalid choice."
                        )

            else:

                print(
                    "Invalid array type."
                )

        elif choice == "2":

            try:

                analyzer.mathematical_operations()

            except ValueError as e:

                print(
                    "\nError:",
                    e
                )

        elif choice == "3":

            try:

                analyzer.combine_split()

            except ValueError as e:

                print(
                    "\nError:",
                    e
                )

        elif choice == "4":

            try:

                analyzer.search_sort_filter()

            except ValueError as e:

                print(
                    "\nError:",
                    e
                )

        elif choice == "5":

            try:

                analyzer.aggregates_statistics()

            except ValueError as e:

                print(
                    "\nError:",
                    e
                )

        elif choice == "6":

            print("\n========================================")
            print(
                "Thank you for using the NumPy Analyzer!"
            )
            print("Goodbye!")
            print("========================================")

            break

        else:

            print(
                "Invalid choice. Please try again."
            )



if __name__ == "__main__":

    main()