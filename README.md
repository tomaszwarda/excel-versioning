# excel-versioning

## Files description

- [Datbase in excel](https://github.com/tomaszwarda/excel-versioning/blob/main/database.xlsx) - actual verion of the database in excel file format. It is automatically being updated to be aligned with csv files.
- [Datbase in csv](https://github.com/tomaszwarda/excel-versioning/blob/main/database/) - actual verion of the database in csv files format. It is automatically being updated to be aligned with excel file.
- Repo setup files:
  - [Githooks](https://github.com/tomaszwarda/excel-versioning/tree/main/.githooks) - standard git hooks
  - [Virtual environment](https://github.com/tomaszwarda/excel-versioning/tree/main/.venv) - python virtual environment for conversion
  - [Config files](https://github.com/tomaszwarda/excel-versioning/tree/main/config_files) - scripts to convert xlsx to csv, and vice versa
  - [Gitignore](https://github.com/tomaszwarda/excel-versioning/blob/main/.gitignore) - stnadard gitignore file
 
## How to use

1. Change csv files or xlsx file acording to planned changes.
2. When all changes are applied execute commands:
```
git add .
git commit -m "<describe what changed>"
git push
```
> During the commit command a script will be lunched. If `database.xlxs` or `database/*.csv` files will be changed both databeses will be syncronised. Any database can be modified, but during one commit only one. This is to prevent any double changes to the same valueas, that will make the tracking difficult.  
3. Repo is updated.
