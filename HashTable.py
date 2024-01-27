# Hashtable
def hash(a):
    vowels = ["A","E","I","O","U"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    
    hashtable = []
    for i in range(0, 9):
        hashtable = hashtable + [0]
    
    for i in a:
        consonants = 0
        sumD = 0
        for j in i: 
            if j not in numbers and j not in vowels:
                consonants += 1
            if j not in vowels and j in numbers:
                sumD += int(j)
        hash_func = (consonants * 24 + sumD) % 9
        
        if hashtable[hash_func] == 0:
            hashtable[hash_func] = i 
        else:
            index = (hash_func + 1) % len(hashtable)
            while hashtable[index] != 0:
                index += 1
            hashtable[index] = i
    print(hashtable)
    
a = hash(["ST1E89B8A32"])
