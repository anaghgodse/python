def read_file(Sample):
    try:
        with open(filename, 'r') as file:
            print("this is new file:\n")
            print("It has multiple lines:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{Sample}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
filename = "Sample.txt"
read_file(filename)