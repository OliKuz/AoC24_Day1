# Find the smallest number in each column
# Find the distance between those 
# get the second smallest 2 and find distance
# find the total distance of the whole input file

def main():
    
    input_file = open("input.txt", "r")
    print(input_file)
    
    # read both columns and sort them
    column1 = []
    column2 = []

    for line in input_file:
        columns = line.split()
        column1.append(int(columns[0]))
        column2.append(int(columns[1]))

    column1.sort()
    column2.sort()

    # calculate the distance between all members
    distance = 0
    for i in range(len(column1)):
        distance += abs(column1[i] - column2[i])

    print("The total distance is: ", distance)

    input_file.close()

if __name__ == "__main__":
    main()


