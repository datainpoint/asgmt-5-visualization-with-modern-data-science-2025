# asgmt-5-visualization-with-modern-data-science-2025
Assignment 5: Visualization with Modern Data Science 2025.

## 01. Define a function `import_presidents_csv()` that is able to import the `presidents.csv` in working directory as a pandas dataframe.

```python
def import_presidents_csv(csv_file_path: str) -> pd.core.frame.DataFrame:
    """
    >>> presidents_csv = import_presidents_csv("presidents.csv")
    >>> presidents_csv.shape
    (53385, 7)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `return_presidents_csv_shape()` that is able to find the shape of `presidents_csv` based on the `import_presidents_csv()` function.

```python
def return_presidents_csv_shape(df: pd.core.frame.DataFrame, dim_name: str) -> int:
    """
    >>> presidents_csv = import_presidents_csv("presidents.csv")
    >>> return_presidents_csv_shape(presidents_csv, "rows")
    53385
    >>> return_presidents_csv_shape(presidents_csv, "columns")
    7
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `return_presidents_csv_head_tail()` that is able to extract the first/last 5 rows of `presidents_csv` based on the `import_presidents_csv()` function.

```python
def return_presidents_csv_head_tail(df: pd.core.frame.DataFrame, head_or_tail: str) -> pd.core.frame.DataFrame:
    """
    >>> presidents_csv = import_presidents_csv("presidents.csv")
    >>> return_presidents_csv_head_tail(presidents_csv, "head").shape
    (5, 7)
    >>> return_presidents_csv_head_tail(presidents_csv, "tail").shape
    (5, 7)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `return_presidents_csv_columns()` that is able to extract the column names of `presidents_csv` based on the `import_presidents_csv()` function.

```python
def return_presidents_csv_columns(df: pd.core.frame.DataFrame):
    """
    >>> presidents_csv = import_presidents_csv("presidents.csv")
    >>> "candidate_id" in return_presidents_csv_columns(presidents_csv)
    True
    >>> "votes" in return_presidents_csv_columns(presidents_csv)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `summarize_presidents_csv()` that is able to extract the column summaries of `presidents_csv` based on the `import_presidents_csv()` function.

```python
def summarize_presidents_csv(df: pd.core.frame.DataFrame, column_name: str):
    """
    >>> presidents_csv = import_presidents_csv("presidents.csv")
    >>> summarize_presidents_csv(presidents_csv, "number")
    (1, 2, 3)
    >>> summarize_presidents_csv(presidents_csv, "candidate_id")
    (329, 330, 331)
    >>> summarize_presidents_csv(presidents_csv, "votes")
    {1: 3690466, 2: 5586019, 3: 4671021}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `create_sqlite3_connection()` that is able to create a SQLite connection to `taiwan_election_2024.db` in working directory via `sqlite3` standard module.

```python
def create_sqlite3_connection():
    """
    >>> conn = create_sqlite3_connection()
    >>> type(conn)
    <class 'sqlite3.Connection'>
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `import_presidents_from_sqlite_db()` that is able to import the `presidents` table in `taiwan_election_2024.db`, in working directory as a pandas dataframe based on `create_sqlite3_connection()` function.

```python
def import_presidents_from_sqlite_db(connection: sqlite3.Connection) -> pd.core.frame.DataFrame:
    """
    >>> conn = create_sqlite3_connection()
    >>> presidents = import_presidents_from_sqlite_db(conn)
    >>> presidents.shape
    (53385, 7)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `import_table_from_sqlite_db()` that is able to import any table in `taiwan_election_2024.db`, in working directory as a pandas dataframe based on `create_sqlite3_connection()` function.

```python
def import_table_from_sqlite_db(connection: sqlite3.Connection, table_name: str) -> pd.core.frame.DataFrame:
    """
    >>> conn = create_sqlite3_connection()
    >>> election_types = import_table_from_sqlite_db(conn, "election_types")
    >>> election_types.shape
    (5, 2)
    >>> parties = import_table_from_sqlite_db(conn, "parties")
    >>> parties.shape
    (35, 2)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `extract_table_columns_from_sqlite_db()` that is able to extract the column names of any table in `taiwan_election_2024.db`, in working directory as a pandas dataframe based on `create_sqlite3_connection()` function.

```python
def extract_table_columns_from_sqlite_db(connection: sqlite3.Connection, table_name: str):
    """
    >>> conn = create_sqlite3_connection()
    >>> "id" in extract_table_columns_from_sqlite_db(conn, "election_types")
    True
    >>> "election_type" in extract_table_columns_from_sqlite_db(conn, "election_types")
    True
    >>> "id" in extract_table_columns_from_sqlite_db(conn, "parties")
    True
    >>> "name" in extract_table_columns_from_sqlite_db(conn, "parties")
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `show_table_shapes_from_sqlite_db()` that is able to show the shape of tables in `taiwan_election_2024.db`, in working directory as a `dict` based on `create_sqlite3_connection()` function e.g.

```
{
    "election_type": (5, 2),
    "parties": (35, 2),
    ...
}
```

Given table names as following: `["aboriginal_legislators", "candidates", "districts", "election_types", "parties", "party_legislators", "polling_places", "presidents", "regional_legislators", "villages"]`

```python
def show_table_shapes_from_sqlite_db(connection: sqlite3.Connection) -> dict:
    """
    >>> conn = create_sqlite3_connection()
    >>> len(show_table_shapes_from_sqlite_db(conn))
    10
    >>> "election_types" in show_table_shapes_from_sqlite_db(conn).keys()
    True
    >>> "parties" in show_table_shapes_from_sqlite_db(conn).keys()
    True
    >>> show_table_shapes_from_sqlite_db(conn)["election_types"]
    (5, 2)
    >>> show_table_shapes_from_sqlite_db(conn)["parties"]
    (35, 2)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```