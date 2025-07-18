def romanToInt(s):
    map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    roman = list(s)
    prev = "qwerty"
    result = 0
    num = 0
    for ch in s:
        if(prev!="qwerty" and map.get(ch)>map.get(prev) ):
            result+=map.get(ch)-2*map.get(prev)
        else:
            result+=map.get(ch)
        prev = ch
        
    return result

def intToRoman(num):
    map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
    result = ""
    for value, symbol in map:
        while num >= value:
            result += symbol
            num -= value
    return result

def main():
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    integer = [1, 5, 10, 50, 100, 500, 1000]

    
    for numr,numi in zip(roman,integer):
        print(f" {numr} = {numi} ")
   

    while(True):
        print("1.Roman to Integer")
        print("2.Integer to Roman")
        type = int(input("Enter what you want to do: "))
        if(type == 1):
            while(True):
                s = input("Enter a Roman numeral: ").upper()
                if not all(c in roman for c in s):
                    print("Invalid Roman numeral. Please try again.")
                    continue
                result = romanToInt(s)
                print(f"The integer value of {s} is {result}")

        if(type == 2):
            while(True):
                s= int(input("Enter an integer(1-3999): "))
                if(s<1 or s>3999):
                    print("Please enter within range.")
                    continue
                result = intToRoman(s)
                print(f"The roman value of {s} is {result}")


main()