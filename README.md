# step
The first step to automate things; from a Markdown into a CLI

[![PyPI version](https://badge.fury.io/py/step.svg)](https://badge.fury.io/py/step)
[![Tests](https://github.com/anapaulagomes/step/actions/workflows/tests.yml/badge.svg)](https://github.com/anapaulagomes/step/actions/workflows/tests.yml)

## The rationale behind this

There are so many manual tasks out there, most of them made of innumerous steps.
Whenever someone thinks about automating them or even proposing this to their team,
it sounds like a Herculean task.

What if we turn a checklist into a CLI and turn a gigantic process into something
more feasible?

## How to use it

```bash
step path-to/YOUR-MARKDOWN.md
```

Your markdown checklist will turn into a functioning CLI.
There you will also find the `Step` object. You can add to it
a callback function and smoothly migrate from a manual to automated approach.

A functional example will come soon.

## Development

First, you're going to need Python 3.10+. Then, [poetry](https://python-poetry.org/) installed.

This project is in its alpha version, so there is more documentation to come.
