# Define a decorator function to preprocess and format phone numbers
def wrapper(f):
    def fun(l):
        # Extract the last 10 digits from each phone number in the input list
        l = [int(i[-10:]) for i in l]
        
        # Format each phone number into the desired pattern "+91 XXXXX XXXXX"
        l = ["+91 " + str(i)[:5] + " " + str(i)[-5:] for i in l]
        
        # Call the original function with the formatted phone numbers
        sp = f(l)
        return sp
    
    # Return the wrapper function
    return fun

# Decorate the sort_phone function with the wrapper to enable preprocessing
@wrapper
def sort_phone(l):
    # Print the sorted phone numbers, each on a new line
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    # Take the number of inputs (phone numbers) as an integer
    l = [input() for _ in range(int(input()))]
    
    # Call the decorated sort_phone function with the input list
    sort_phone(l)
