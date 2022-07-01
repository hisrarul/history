## Jump statements in Python (break, continue and pass)

* Using for loops and while loops in Python allow to automate and repeat tasks in an efficient manner.

#### Break statement
* In Python, the break statement provides the opportunity to exit out of a loop when an external condition is triggered.
* The break statement causes a program to break out of a loop.

```python
number = 0
for number in range(10):
    if number == 7:
        break
    
    print('Number is' + str(number))

print('Out of loop')
```

**Problem Statement:**
* In the following example, user will enter the password which is set to be data.
* If the password matches, it will print `Welcome to the Python Course!!` else print `Wrong Password!!` and user will re-enter the password.
* In the fourth trial, it will print `One trail left!!`

```python
password = "data"

for trial in range(1, 5):

    if trial == 4:
        print('One trial left!!!')
    enter_password = input('Enter password: ")

    if enter_password == password:
        print("Welcome to python course!!")
        break
    
    else:
        print("Wrong Password!!")
```


#### Continue statement
* The continue statement gives you the option to skip over the part of a loop where an external condition is triggered, but to go on to complete the rest of the loop.
* That is, the current iteration of the loop will be disrupted, but the program will return to the top of the loop.
* The continue statement will be within the block of code under the loop statement usually after a conditional `if` statement.
* The continue statement causes a program to skip certain 

```python
number = 0
for number in range(10):
    if number == 5:
        continue

    print('Number is ' + str(number))
print('Out of loop')
```

#### Problem statement
* In the following example, user will enter the password which is set to be `1232`
* If the OTP matches, it will ask user to provide details like `Enter Your Name:` and `Enter Your City:` and user will re-enter the OTP.
* In the fourth trial, it will print *One Trail left!!!`

```python
OTP = "1243"

for trial in range(1, 5):

    if trial == 4:
        print('One trial left!!!')

    enter_otp = input("Enter OTP: ")

    if enter_otp != OTP:
        print("Try Again!!")
        continue

    else:
        name = input("Enter Your name: ")
        city_name = input("Enter Your City: ")
        break
```

#### pass statement
* pass is a null operation - when it is executed nothing happens.
* It is useful as a placeholder when a statement is required syntactically but no code needs to be executed.
* The pass statement tells the program to disregard that condition and continue to run the program as usual.

```python
number = 0

for number in range(10):
    if number == 5:
        pass
    
    print('Number is ' + str(number))
print('Out of the loop')
```

#### Question: Output of the code

```python
number = 10

while number > 3:

    if number % 2 == 0:
        number = number - 1
        continue
    
    else:
        print(number, end=' ')
        number = number - 1
```