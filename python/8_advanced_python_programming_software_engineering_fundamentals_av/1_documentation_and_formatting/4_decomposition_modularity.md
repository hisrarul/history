## Decomposition and Modularity

#### Modularity
Effective decomposition requires smaller pieces of code in form of functions where each function only performs a singular task.
* Modularity promotes bite-size code.
* Avoid complex nested constructs if possible (loops, if-else)
* Each block should performs at-most one action
* Improves reability
* Easier to resolve errors
* Easier to test and debug code

#### Modular code
* Complex function

    `params -> very complex code -> return`

* Split the very complex code into few functions

    `func_1, func_2, func_3, func_4 <-> params -> main function -> return`


