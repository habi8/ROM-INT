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

def main():
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    integer = [1, 5, 10, 50, 100, 500, 1000]

    
    for numr,numi in zip(roman,integer):
        print(f" {numr} = {numi} ")
   

    while(True):
        s = input("Enter a Roman numeral: ").upper()
        if not all(c in roman for c in s):
            print("Invalid Roman numeral. Please try again.")
            continue
        result = romanToInt(s)
        print(f"The integer value of {s} is {result}")

main()