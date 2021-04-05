## Program structure

- command_parser.py - parser file
- converter.py - source code file
- data - directory with .csv and .parquet files

## Dependencies

- pyarrow 3.0.0
- pandas 1.1.4
- argparse 1.1

## Execution
Program runs on the command line with parameters.
### Parameters
To get this message use the command from the working directory:
```
python converter.py -h
```
```
usage: converter.py [-h] (-tocsv | -toprq | -s) -i INFILE [-o OUTFILE] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -tocsv, --prq_to_csv  convert .parquet file to .csv file
  -toprq, --csv_to_prq  convert .csv file to .parquet file
  -s, --schema          print .parquet file schema
  -i INFILE, --infile INFILE
                        input file path
  -o OUTFILE, --outfile OUTFILE
                        output file path
  -d, --debug           shows the results of work
```

## Examples
### Convert .csv file to .parquet file
```
python converter.py -toprq -i data/minwage.csv -o data/prq_result.parquet
```
### Convert .parquet file to .csv file
```
python converter.py -tocsv -i data/minwage.parquet -o data/csv_result.csv
```
### Show .parquet file's schema
```
python converter.py -s -i data/minwage.parquet
```