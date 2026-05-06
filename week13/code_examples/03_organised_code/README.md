# Readme

This is the readme!

It should contain information about your project, such as:
- Why your code exists!
- How to run the code
- Any data fixtures that need setting up to run your code
- How to run the automated tests


## Why this code exists
This project exists to show off code organisation to CIV students 😉.

It is a little bit unnecessarily fragmented for such a simple script, so that I can get some of the point across.

## Running the code

The entry point is in `src/main.py`

You may run it from your shell with `python src/main.py`


## Running the tests

To run tests, you should run `python -m unittest discover -s tests`, which will auto-discover the tests.
However, to handle relative requires, you should first export the PYTHONPATH env variable as 'src', so that unittest knows where your source code lives.

You may either run tests each time as:
`PYTHONPATH=src python -m unittest discover -s tests`

OR

Export PYTHONPATH in your bashrc or zshrc
`export PYTHONPATH=src`

which will allow `python -m unittest discover -s tests` to work without further fuss.


## Exercise

Phone Contact & Email Contact don't have any tests (oh no!).

Write some tests for email contact, considering the behaviour that it has on its setter.

You might also expand PhoneContact to have extra behaviours and corresponding tests. You wouldn't want to find yourself trying to dial the number "1230-", for example!


### Advanced, for no reason: not assessed, not expected
If you get sick of typing all of that, you could find out how 'aliases' are set for your operating system, and make 'a shortcut' to run those tests.

Using bash under Windows, I might run
`start ~/.bashrc`

and add this to the end of the file:

```bash
alias pythontests='PYTHONPATH=src python -m unittest discover -s tests'
```

Then, after ensuring that my settings are sourced (`source ~/.bashrc` or `. ~/.bashrc`), I could run `pythontests` instead.