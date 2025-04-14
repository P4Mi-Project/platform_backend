# A backend for p4mi community platform.

## How to run this project
At first you have create a virtual environment. To do that use the following commands.
```
pip install virtualenv
```
```
python -m virtualenv env
```
Each  time you want to use the env you have to use type this command before you start your work.
### Command for windows
```
.\env\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the project
```
python -m fastapi dev main.py
```

### For testing
Make sure your remote bracet '[]'
```
python -m unittest  .\tests\[your_test_file_name].py
```

# Make sure you do this
* Paste the google_service_account.json to the project root, which is been given to you.
* Make sure you don't push anything sensitive to the repository. If in case you make this kind of mistake try to let the maintainer know as soon as possible.

# Coding guidelines
* Make sure to cover tests for as much compoents as possible.
* Make  sure you have forked the project and have your own copy on your repository.
* Update your local repository before each changes.
* You will always push code to your local repository.
* You should make a pull request so that the maintainer of the project can merge your changes to the main p4mi project.

# Resources
[Fast api documentation](https://fastapi.tiangolo.com/#example)