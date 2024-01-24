def search(arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            print("the element is found")
            return true
        print("the element in not found")
        return false
    
arr = [1,4,3,5,3]
key= int(input("enter the elem"))
search(arr,key)