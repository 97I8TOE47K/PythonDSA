#the entire theroy part of Radix Sort is covered in the attached RadixSort.pdf
#the same example is dry runned in hand, for a better understading of the sorting mechanism
def countingSort(arr, exp1):

    n = len(arr)

    output = [0] * (n)
    count = [0] * (10)

    for i in range(n):
        index = arr[i] // exp1
        count[index%10] = count[index%10] + 1

    for i in range(1,10):
        count[i] = count[i] + count[i-1]

    i =  n - 1
    while i>=0:
        index = arr[i] // exp1
        output[count[index%10] - 1] = arr[i]
        count[index % 10 ] = count[index % 10] - 1
        i = i - 1

    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    print("\nInitiating Radix Sort.")

    #Finding the max value in the provided array
    max_val = max(arr) 

    #exp_track helps in controlling the total number of iterations
    exp_track,count = 1,1

    #the iteration will run a total of length of the max value
    #this is done by dividing the max value by 10^i (i=0,1,2,3,..) till max_val/exp_tracl becomes 1
    while max_val/exp_track >= 1:
        countingSort(arr,exp_track)
        print("After Pass ",count," -->> ",arr)
        count = count + 1
        exp_track *= 10

if __name__ == "__main__": 
    arr = []

    while True:
        temp = int(input("Enter Value : "))
        arr.append(temp)
        choice = input("Enter Y/y to continue or N/n to exit : ")
        if choice not in ['Y', 'y']:
            break

    print("\nEntered array : ",arr)

    radixSort(arr)

    print("\n\nSorted Array : ",arr)
