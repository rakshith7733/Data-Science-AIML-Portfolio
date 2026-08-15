### Expense Tracker [CLI]:
- This mini project helps in understanding the procedure of the expenses were saved, retrived, add/delete, fetch according to requirement.

- The topics covers are lists, dictionary, i/o files, functions, conditionals, try-except concepts, Loops (for,while), enumerate(), defaultdict.


##### Features:

    - Add Expenses
    - View Expenses
    - Delete Expense
    - Category Summary
    - Monthly Total

##### Initial Notes before starting the project.

```PY
>> 1. Initialize once (empty)
        records = defaultdict(list)
>> 2. Directly append new categories without defining them first
        records["Food"].append({"amount": 500, "date": "2026-07-18"}) 
        "Food" key is created automatically here

        records["Travel"].append({"amount": 200, "date": "2026-07-19"}) 
        "Travel" key is created automatically here

>> 3. Append to existing categories
        records["Food"].append({"amount": 50, "date": "2026-07-20"})

print(dict(records))
# # Output: {'Food': [{...}, {...}], 'Travel': [{...}]}
```
