# Test Cassandra Cluster

So to test our **Cassandra** cluster we will need to use one build-in tool that **Cassandra** comes together and it's called **cassandra-stress**

> You can find more information for cassandra-stress [here](https://cassandra.apache.org/doc/latest/cassandra/tools/cassandra_stress.html)

## Create our stress file

For our purpose we have build one **cassandra-stress** yaml file. You can find it [here](./cpu_data_profile.yaml). Taking considering our csv file data for [cpus](../cpus.csv).

## Change our replication factor

Firstly we need to change our **replication factor**. So to take different outputs from our testings.

We can use this command for easy change of the **replication-factor**:
`cqlsh -e "ALTER KEYSPACE mykeyspace WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 3}`

With this command we can change the **replication-factor** through our command line without go in **cqlsh**. We use the `-e` and double quotes `"` so to run the command from the cmd directly.

You need to change the `mykeyspace` and replace it with yours **key space name**.

## Run the tests

Now that we have changed our replication factor we need to run our **cassandra-stress** file that we have created in the first step.

We need to just run this command:
`/usr/bin/cassandra-stress user profile=cpu_data_profile.yaml 'ops(insert=1,read1=1)' n=10000 -rate threads=50`

You need to change the `profile=cpu_data_profile.yaml` with your yaml file.

Let's break down this command.

- `/usr/bin/cassandra-stress` 
  - It gives the path to the **cassandra-stress** testing tool.
- `user profile=cpu_data_profile.yaml` 
  - `user` mode allows you to stress your own schemas.
  -  `profile=cpu_data_profile.yaml` specifies the YAML file containing the stress test profile
- `'ops(insert=1,read1=1)'`
  - It defines the operations which will stress our cluster. In this case the probability of `insert` is 50% and other half is for `read`.
- `n=10000`
  - Specifies the total number of operations that **cassandra-stress** will perform for our test.
- `rate threads=50`
  - That means that **cassandra-stress** will use 50 concurrent threads to make the operations to our Cassandra cluster.

All in all this command will make 10,000 operations half `insert` and half `read`, these operations will use 50 concurrent threads so to issue those operations.