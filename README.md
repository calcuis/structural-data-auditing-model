#### Model-2 (basic level)
- Read the content of `file1.csv` and `file2.csv`
- Calculate the `Required Sum` of the `Score` field from `file1.csv`
- Iterate through the rows of `file2.csv`, accumulating rows until the sum of their `Score` fields matches the `Required Sum`
- Save the selected rows to `results.csv` as final output

test it out by
```
py model2.py
```
#### Model-5 (advanced level)
- Calculating `Required Sum`: the sum of non-null `Score` values from `file1.csv` is calculated
- Initialization: variables `current_sum` and `output_rows` are initialized to track the running sum of scores and store matching rows, respectively
- Auditing Logic: iterate through `file2.csv`, selecting rows where the `Score` matches and the running total remains within the `Required Sum` (adjustment will be made if necessary); if a `Score` in `file1.csv` is null, the corresponding row in `file2.csv` is skipped (null handler); if the running total reaches the `Required Sum`, the loop stops (or it will stop until all the rows are scanned)
- The selected rows are saved to `results.csv`, ensuring the sum of the `Score` field matches the sum in `file1.csv`, and the `Time` field sequence follows `file2.csv`

test it out by
```
py model5.py
```
#### Model-9b (unstable loop)
- Loop until the `current_sum` reach the `required_sum`
- Reference model only right away (not for production)

test it out by
```
py model9b.py
```
#### Coexisting record detector
- Compare each record of `file1.csv` and `file2.csv`
- Coexist column is created using a lambda function that assigns 1 to each field if a record exists in both files, and null if not
- Save the output as `results.csv`

test it out by
```
py detector.py
```
#### Unmatched record detector
- Scan all csv files within the current directory
- List out those unmatched record(s)

test it out by
```
py unmatched.py
```
