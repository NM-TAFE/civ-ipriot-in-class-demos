# Readme

The aim here is to write nice unit tests.

1. Write a function that calculates the sum of two numbers
> Call it `add` or similar, not `sum` (that is a built-in function)
> Include a docstring!

2. Write the unit tests that check:
- that correct values are calculated for integer, floating point, and complex numbers (e.g., 2 – 1i is complex)
- that a TypeError is raised if any of the arguments is not a valid type

# Running your tests from the CLI:
This tells Python where the source directory is (setting PYTHONPATH), and where the **unittest m**odule should try to **s**tart discovering tests.
```bash
PYTHONPATH=src python -m unittest discover -s tests
```
# Here are some common pitfalls while running your unittests:
- [ ] Are modules importing correctly? If not:
	- [ ] Did you set your PYTHONPATH?
	- [ ] Are you running your project from the correct directory?
	- [ ] Does each subdirectory contain a `__init__.py` file? (This only affects some people)

- [ ] Are you running your tests using the unittest module correctly?
	- [ ] There are 2 ways -- letting the unittest module 'discover' tests (my preference), or running each test file as a script:
```python
if __name__ == "__main__":
    unittest.main()
```
		or

```bash
python -m unittest discover
```
- [ ] Did you name each test method starting with the word `test`? (I know 🙄, it's a little ridiculous)
- [ ] Does your unittest class inherit from unittest.TestCase?
- [ ] Are your assertions being called from 'self'? (eg: self.assertEquals)
- [ ] Do your test class names match the name of their file? Ie, if you have `TestBlog`, your file should be called `test_blog.py`
