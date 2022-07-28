# Level One
class BrokenPipe:
    def __init__(self):
        self.data = None
        self.result = []
        self.read_input()

    # Open the file and read into a list
    def read_input(self):
        file_name = input("Please enter the input text file name (including extension eg:- input.txt) ")
        try:
            with open(file_name) as f:
                self.data = [list(map(int, line.strip().split(' '))) for line in f]
        except FileNotFoundError:
            print("File does not exist")
            return

        self.find_leaking_floor()

    # Find the leaking floor using the list read
    def find_leaking_floor(self):
        # loop through the array of input
        j = 1
        while j < len(self.data):
            p = (self.data[j])[0]  # Pressure of the leak
            f = (self.data[j])[1]  # Floor where the leak was reported
            g = (self.data[j])[2]  # Ground floor pressure
            i = (self.data[j])[3]  # Insulation of the building
            # If the Leak started from that floor (obvious case)
            if g - p == f:
                self.result.insert(j - 1, f)
                j += 1
            # All remaining conditions
            else:
                counter = 1
                checked_floors = list(range(f, 201))
                while (g - checked_floors[counter]) - (i * (checked_floors[counter] - f)) - i > p:
                    counter += 1
                res = f + counter
                self.result.insert(j - 1, res)
                j += 1
        self.write_output()

    # Write the output a text file on the same directory
    def write_output(self):
        file1 = open("output.txt", "w")

        for index, value in enumerate(self.result):
            output = f"Case #{index + 1}: {value}\n"
            file1.write(output)
        file1.close()
        print('Output written to output.txt')


# Call the Initializer
BrokenPipe()
