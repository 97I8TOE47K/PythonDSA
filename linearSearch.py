def linearSearch(lst, key):
    return next((i for i in range(len(lst)) if lst[i] == key), -1)

if __name__ == "__main__":
    #we are using list comprehension to get the input for the list from user. here we are using the input statement to get the string input from the user
    #then we are splitting it based on the whitespaces which creates an list of strings which are then converted to integer and stored in the lst variable
    lst = [int(x) for x in input("\nEnter the Array upon which linear search is to be applied: ").split()]
    key = int(input("\nEnter the key to be searched: "))    #taking input for the key to be searched
    pos = linearSearch(lst=lst, key=key)    #executing linear search on the list and supplied search value
    if pos == -1:   #if the key is not found in the supplied list we print that no such entry is detected
        print(f"\nThe key ({key}) is not found in the list.\n")
    else:   #if the key is found we print out its position in the list (starting at 0)
        print(f"\nThe key ({key}) is found at position: {pos} in the list.\n")
