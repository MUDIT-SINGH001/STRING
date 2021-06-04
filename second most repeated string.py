from collections import Counter 
    
def secondFrequent(input): 
    
    
    dict = Counter(input) 
    
    
    value = sorted(dict.values(), reverse=True) 
    print(value)
    secondLarge = value[1] 
    

    for (key, val) in dict.items(): 
        if val == secondLarge: 
            print (key) 
        
    
# Driver program 
if __name__ == "__main__": 
    input = ['aaa','bbb','ccc','bbb','aaa','aaa','aaa','ccc','ccc'] 
    secondFrequent(input)
