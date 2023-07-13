# My expenses

This is a step by step on how to retrieve data from
my banks and generate a report with it.

## Retrieving the data

1. Go to https://mybrazilianbank.br and download data from the last month
2. Go to https://mygermanbank.de and download data from the last month

## Parse the data

- Get a quote from **BRL** to **EUR**
- Run the script that puts everything in one format
- The data generated in the previous step should be moved to `~/workspace/my-expenses`

## Generate the report

From a Jupyter Notebook you'll be able to see a report.
Just run:

```bash
jupyter notebook
```

Well done!
