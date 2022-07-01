## Recursion


Let's solve a simpler problem first

* What if we had only 2 persons in the room?
e.g A and B
ans. 1 Hand Shake

* What if we had 3 persons in the room?
e.g. A and B and C
ans. 3 Handshakes (A,B) (A,C) (B, C)

* What if we had 4 persons in the room?
e.g. A and B and C and D
ans. 6 Hand Shakes (A,B) (A,C) (A,D) (B,C) (B,D) (C,D)

* What if we had 5 person in the room?
e.g. A and B and C and D and E
ans 10 Hand Shakes

Here, we are using iterative process. We are just simply calculating possible combination.

Look at the results

| A B | F(2) = 1 Hand Shake | 1 |
| A B C | F(3) = 3 Hand Shakes | F(2) + 1 = 3 |
| A B C D | F(4) = 6 Hand Shakes | F(3) + 3 = 6 |
| A B C D E | F(5) = 10 Hand Shakes | F(4) + 4 = 10 |

Hence, we can right the formula `F(N) = F(N-1) + (N-1)`

Flow:
F(5) ---> F(4) + 4 ---> F(3) + 3 ---> F(2) + 2 ---> 1

#### Python Code
```python
# define recursive function to count handshakes

def count_hand_shakes(total_persons_in_room):

    # base condition: when number of person is 2 (one handshake)
    if total_persons_in_room == 2:
        return 1
    
    else:
        # F(N) = F(N-1) + (N-1)
        return count_hand_shakes(total_person_in_room - 1) + (total_person_in_room - 1)
```

#### Iterative approach
```python
def count_hand_shakes_iterative(total_persons_in_room):
    count = 0

    for i in range(1, total_persons_in_room):
        for j in range(i+1, total_persons_in_room + 1):
            print('Hand Shake of ', i, 'and', j)
            count = count + 1
    
    # total handshakes
    print('Total number of handshakes: ', count)
```

#### Advantages of Recursion
* Reduces length of code
* Iteration can be complex sometimes, when we have several possible random cases.


#### Disadvantages of Recursion
* It uses more memory.
* Time complexity is increases, can be slow if not implemented correctly.


#### Looping Constructs (Iterative Solution)
* It depends upon the task.
* For most common programming tasks go for iterative solution.
* For particular tasks a recursive solution is both intuitive/simple to understand and also faster in terms of execution.
