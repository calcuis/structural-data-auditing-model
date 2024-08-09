#### Model-2 (basic level)
- Reads the content of `file1.csv` and `file2.csv`.
- Calculates the `Required Sum` of the `Score` field from `file1.csv`.
- Iterates through the rows of `file2.csv`, accumulating rows until the sum of their `Score` fields matches the `Required Sum`.
- Saves the selected rows to `results.csv` as final output.

test it out by
```
py model2.py
```
#### Model-5 (advanced level)
- Calculating `Required Sum`: The sum of non-null Score values from `file1.csv` is calculated.
- Initialization: Variables `current_sum` and `output_rows` are initialized to track the running sum of scores and store matching rows, respectively.
- Row Selection Logic: The code iterates through `file2.csv`, selecting rows where the `Score` matches and the running total remains within the `Required Sum`; if a `Score` in `file1.csv` is null, the corresponding row in `file2.csv` is skipped; if the running total reaches the `Required Sum`, the loop stops.
- Saving Results: The selected rows are saved to `results.csv`, ensuring the sum of the `Score` field matches the sum in `file1.csv`, and the `Time` field sequence follows `file2.csv`.

test it out by
```
py model5.py
```
