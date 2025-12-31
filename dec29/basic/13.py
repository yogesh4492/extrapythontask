# Q 13: Write a function that accepts a number and prints its multiplication table from 1 to 10.

def multiplication_table():
    try:
        num=int(input("Enter Number = "))
        for i in range(1,11):
            print(f"{num:2d}  {i:2d}  {i*num:2d} ")
    except Exception as e:
        print(f"Error : {e}")

if __name__=="__main__":
    multiplication_table()