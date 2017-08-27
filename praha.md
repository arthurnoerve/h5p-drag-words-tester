# Praha
An automated web interface testing service with fronted dashboard


## Structure
* Node API
* JS Frontend
* Python unit-test framework based on Selenium

### Folders
```
tester
	|- tests
	|- bin
		|- praha
	|- main.py
	|-	 
api
	|- 
front
	|- 
```

### URI
```
/api
	/test
/store
	/test1
		/run1
		...
	...
/front
	...
```

## API
* Calls the praha cli program to run a test 

```
/test 			GET		Get all tests done
/test/:id		GET		Get a particular test with id of :id
/test/:id		POST	Make a run of a test


```
## Frontend
* Show list of available tests
* Open to show overview for each test; name, runs, latest status, graphs, gifs
* 

## Python Tester
* Main python file to run program
* CLI apps in bin to run interactively
* Available tests in class files in ‘tests’ folder
* 





