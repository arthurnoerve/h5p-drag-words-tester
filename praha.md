# Praha
An automated web interface testing service with fronted dashboard




##Usage
On the backend everything is exposed via the praha cli application. Using this, one can add, list and run tests. Adding results in putting a python file in the tests folder. Running simply uses said file to run the procedure within, on completion screenshots, logs and a gif is placed in a data store. The frontend simply calls an API that exposes this bin tool with a REST interface. 






## Structure
* Node API
* JS Frontend
* Python unit-test framework based on Selenium for web tests

### Folders (incomplete)
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
	/
	/:test
	/:test/:run
```






## API
Calls the praha cli program to list and run tests

```
/test 			GET		Get all tests done
/test/:id		GET		Get a particular test with id of :id
/test/:id		POST	Run a test


```
## Frontend
* Show a list of available tests
* Open to show overview for each test; name, runs, latest status, graphs, gifs
* 

## Python Tester
* Main python file to run program
* CLI apps in bin to run interactively
* Available tests in class files in ‘tests’ folder


### Test files
The test files are class files containing sublasses of a given "PrahaTest" class. This superclass takes care of supplying a webdriver, logging functions, screenshot functions, completion cleanup/transfer to store/gif generation.





