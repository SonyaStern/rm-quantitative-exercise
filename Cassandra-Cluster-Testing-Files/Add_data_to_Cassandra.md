# How to add data to Cassandra

## Key Space

To add data to **Cassandra** we will need to create a **Key space** in our Cassandra instance. Just to to `cqlsh` and write this command.

```sql
CREATE KEYSPACE IF NOT EXISTS mykeyspace WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };
```

> You need to change the `mykeyspace` with your own name of your key space. And make what ever changes you need in the `class` and `replication_factor`

## Create the Table

Now you need to use this key space tha you created so to create your new table.

Firs run:
`USE <your_key_space>;`

And now that you are using this key space you can create your table using this command:
```sql
CREATE TABLE IF NOT EXISTS mytable (
    rownames TEXT PRIMARY KEY,
    name TEXT,
    syct INT,
    mmin INT,
    mmax INT,
    cach INT,
    chmin INT,
    chmax INT,
    perf INT,
    estperf INT
);
```

Here you need to change the `mytable` with your name of table you want. And you need to change the columns names so to fit with your column names.

## Add Data from a CSV file

Now we need to add data into our Data table. The easiest way is to add data form a csv file. We will use the `COPY` command for this purpose.

```sql
COPY mytable (rownames, name, syct, mmin, mmax, cach, chmin, chmax, perf, estperf) 
FROM '/path_to_your_file/yourfile.csv' WITH DELIMITER=',' AND HEADER=TRUE;
```

Here you need to change only the column names and the path where your csv is located.

