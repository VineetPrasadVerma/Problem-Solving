def getMinOperations(data):
    # Write your code here
    def make_palindrome(data):
      left_pointer = 0
      right_pointer = len(data) - 1
      
      total_operations = 0
      
      while left_pointer < right_pointer:
        if data[left_pointer] != data[right_pointer]:
          if data.count(data[left_pointer]) < data.count(data[right_pointer]):
            target = data[right_pointer]
            old = data[left_pointer]
          else:
            target = data[left_pointer]
            old = data[right_pointer]
            
          for i in range(len(data)):
            if data[i] == old:
              data[i] = target
          
          total_operations += 1
            
        left_pointer += 1
        right_pointer -= 1 
      
      return total_operations

    return make_palindrome(data)
    
    
print(getMinOperations([1,2,3,3,1,4]))