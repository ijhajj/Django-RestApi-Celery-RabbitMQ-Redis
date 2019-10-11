class salaryError(Exception):
    pass


while True:
    try:
        #salary = int(input("Enter your Salary"))
        salary = input("Enter your Salary")
        if not salary.isdigit():
            raise salaryError()
        print(salary)
        break
    #except ValueError:
    except salaryError:
        print("Enter a valid Salary amount, try again...")
    finally:
        print("Releasing all the resources")
