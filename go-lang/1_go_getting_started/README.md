#### Initialize the prgram 

```bash
go mod init github.com/pluralsight/webservice

go run github.com/pluralsight/webservice

go run main.go
```

#### Declaring variable with primitive data types
```go
package main

import (
	"fmt"
)

func main() {
	var i int
	i = 3
	fmt.Println(i)

	var f float32 = 3.64
	fmt.Println(f)

	firstname := "israrul haque"
	fmt.Println(firstname)

	b := true
	fmt.Println(b)

	c := complex(3, 4)
	fmt.Println(c)

	r, im := real(c), imag(c)
	fmt.Println(r, im)
}
```

#### Working with Pointers
```go
package main

import "fmt"

func main() {
	var firstname *string = new(string)

	// Dereference operation
	*firstname = "arthur"
	fmt.Println(*firstname)

	lastname := "haque"
	fmt.Println(lastname)

	// pointer to its operand
	ptr := &lastname
	fmt.Println(ptr, *ptr)

	lastname = "shaikh"
	fmt.Println(ptr, *ptr)
}
```

#### Creating Constants
```go
package main

import "fmt"

func main() {
	const c int = 3
	fmt.Println(c + 3)

	// Again
	fmt.Println(float32(c) + 1.43)
}
```

#### Using Iota and Constant Expressions
```go
package main

import "fmt"

const (
	first  = iota
	second = iota
)

const (
	third = iota
	fourth
)

func main() {
	fmt.Println(first, second, third, fourth)
}
```

#### Working with Collections
```go
// array
package main

import "fmt"

func main() {
	var arr [3]int
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3
	fmt.Println(arr)
}

// Use short form of array using initialization
package main

import "fmt"

func main() {
	arr := [3]int{1, 2, 3}
	fmt.Println(arr)
}

// working with slice
package main

import "fmt"

func main() {
	slice := []int{1, 2, 3}
	slice := arr[:]
	arr[1] = 42
	slice[2] = 27
	fmt.Println(arr)
}

// Append slice
package main

import "fmt"

func main() {

	slice := []int{1, 2, 3}

	fmt.Println(slice)

	slice = append(slice, 4, 3, 45)
	fmt.Println(slice)
}

// print sliced array using slice
package main

import "fmt"

func main() {

	slice := []int{1, 2, 3}

	fmt.Println(slice)

	slice = append(slice, 4, 3, 45)

	s2 := slice[1:]
	s3 := slice[:2]
	s4 := slice[1:2]

	fmt.Println(s2, s3, s4)
}

// map data type
package main

import "fmt"

func main() {

	m := map[string]int{"foo": 42}
	fmt.Println(m)
	fmt.Println(m["foo"])

	m["foo"] = 27
	fmt.Println(m["foo"])

	delete(m, "foo")
	fmt.Println(m)
}

// Structs, it allow to associate disparate data types together
package main

import "fmt"

func main() {
	type user struct {
		ID        int
		FirstName string
		LastName  string
	}
	var u user
	u.ID = 1
	u.FirstName = "Arthur"
	u.LastName = "Haque"
	fmt.Println(u)
	fmt.Println(u.FirstName)

	u2 := user{ID: 1, FirstName: "Arthur", LastName: "Haque"}
	fmt.Println(u2)
}

// models form
cat > models/user.go << EOF
package models

type User struct {
	ID        int
	FirstName string
	LastName  string
}

var (
	users  []*User
	nextID = 1
)
EOF

// cat main.go
package main

import (
	"fmt"

	"github.com/pluralsight/webservice/models"
)

func main() {
	u := models.User{
		ID:        2,
		FirstName: "Arthur",
		LastName:  "Haque",
	}
	fmt.Println(u)
}

// Build the prog
go run github.com/pluralsight/webservice
go build
./webservice
```


#### Creating Functions
```go
// Adding parameters to functions
package main

import "fmt"

func main() {
	fmt.Println("Hello, playground!")
	port := 3000
	numberOfRetries := 2
	startWebServer(port, numberOfRetries)
}

func startWebServer(port int, numberOfRetries int) {
	fmt.Println("Starting server ..")
	fmt.Println("Server started on port", port)
	fmt.Println("Number of retries", numberOfRetries)
}

// Returning Data from functions
package main

import "fmt"

func main() {
	port := 3000
	isStarted := startWebServer(port)
	fmt.Println(isStarted)

}

func startWebServer(port int) error {
	fmt.Println("Starting server ..")
	fmt.Println("Server started on port", port)
	return true
}

// Return an error
cat main.go

package main

import (
	"errors"
	"fmt"
)

func main() {
	port := 3000
	err := startWebServer(port)
	fmt.Println(err)

}

func startWebServer(port int) error {
	fmt.Println("Starting server ..")
	fmt.Println("Server started on port", port)
	return errors.New("Something went wrong")
}

// Write only variable
cat main.go

package main

import (
	"fmt"
)

func main() {
	port := 3000
	_, err := startWebServer(port)
	fmt.Println(err)

}

func startWebServer(port int) (int, error) {
	fmt.Println("Starting server ..")
	fmt.Println("Server started on port", port)
	return port, nil
}

// Using Methods to Add behaviors to a Type
cat models/user.go
package models

type User struct {
	ID        int
	FirstName string
	LastName  string
}

var (
	users  []*User
	nextID = 1
)

func GetUsers() []*User {
	return users
}

func AddUser(u, User) (User, error) {
	u.ID = nextID
	nextID++
	users = append(users, &u)
	return u, nil
}


// Adding functions to the webservice and creating methods
cat controllers/user.go

package controllers

import (
	"net/http"
	"regexp"
)

type userController struct {
	userIDPattern *regexp.Regexp
}

func (uc userController) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello from User controller!"))
}

func newUserController() *userController {
	return &userController{
		userIDPattern: regexp.MustCompile(`^/users/(\d+)/?`),
	}
}


// Implementing interface
cat controllers/front.go

package controllers

import "net/http"

func RegisterControllers() {
	uc := newUserController()

	http.Handle("/users", *uc)
	http.Handle("/users/", *uc)
}


// Starting the webservice
cat main.go

package main

import (
	"net/http"

	"github.com/pluralsight/webservice/controllers"
)

func main() {
	controllers.RegisterControllers()
	http.ListenAndServe(":3000", nil)

}

go build
./webservice
curl http://localhost:3000/users
curl http://localhost:3000/users/44
```

## Contolling Program Flow

#### for loops

* Loop till condition
* Loop till condition with post clause
* Infinite loops
* Loop over collections

#### Creating loops that Terminate based on a Condition

```go
package main

func main() {
	var i int
	for i < 5 {
		println(i)
		i++
	}
}

// break statement
package main

func main() {
	var i int
	for i < 5 {
		println(i)
		i++
		if i == 3 {
			break
		}
	}
}

// Use continue to break in 1 iteration
package main

func main() {
	var i int
	for i < 5 {
		println(i)
		i++
		if i == 3 {
			continue
		}
		println("Continue..")
	}
}

// Initialize within for loop
package main

func main() {
	for i := 0; i < 5; i++ {
		println(i)
	}
}

// ugly syntax
package main

func main() {
	var i int
	for ; ; {
		if i == 5 {
			break
		}
		println(i)
		i++
	}
}

// Looping with collections method 1
package main

func main() {
	slice := []int{1, 2, 3}
	for i := 0; i < len(slice); i++ {
		println(slice[i])
	}
}

// Looping with collections method 2
package main

func main() {
	slice := []int{1, 2, 3}
	for i, v := range slice {
		println(i, v)
	}
}

// map
package main

func main() {
	wellknownPorts := map[string]int{"http": 80, "https": 443}
	for k, v := range wellknownPorts {
		println(k, v)
	}
}

// ignore a value using _
package main

func main() {
	wellknownPorts := map[string]int{"http": 80, "https": 443}
	for _, v := range wellknownPorts {
		println(v)
	}
}

// Working with panic functions
package main

func main() {
	println("Stating a webserver")

	panic("Something bad just happened")

	println("Web server started")
}
```

#### Creating if statements

```go
package main

type User struct {
	ID        int
	FirstName string
	LastName  string
}

func main() {
	u1 := User{
		ID:        1,
		FirstName: "Arthur",
		LastName:  "Dent",
	}
	u2 := User{
		ID:        2,
		FirstName: "Ford",
		LastName:  "Perfect",
	}
	if u1.ID == u2.ID {
		println("Same User!")
	} else {
		println("Different User!")
	}
}

// elseif
package main

type User struct {
	ID        int
	FirstName string
	LastName  string
}

func main() {
	u1 := User{
		ID:        1,
		FirstName: "Arthur",
		LastName:  "Dent",
	}
	u2 := User{
		ID:        2,
		FirstName: "Arthur",
		LastName:  "Perfect",
	}
	if u1 == u2 {
		println("Same User!")
	} else if u1.FirstName == u2.FirstName {
		println("Similar User!")
	}
}
```

#### Switching Statement
```go
package main

type HTTPRequest struct {
	Method string
}

func main() {
	r := HTTPRequest{Method: "GET"}

	switch r.Method {
	case "GET":
		println("Get request")
		break
	case "DELETE":
		println("Delete request")
	case "POST":
		println("POST request")
	case "PUT":
		println("PUT request")
	}
}
```

#### Test using curl
```bash
# Run the program
go run main.go

# Post request
curl --location --request POST 'http://localhost:3000/users' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "FirstName": "Ford",
    "LastName": "Perfect"
}'

# Get request
curl --location --request GET 'http://localhost:3000/users' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"description": "I am gonna summit my salah"
	}'
```


#### Refer
[Go: Getting Started By Mike Van Sickle](https://www.pluralsight.com/courses/getting-started-with-go)

[GitHub source](https://github.com/cemdrk/go-getting-started)