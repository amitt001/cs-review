# Design a Distributed Cache

```
|    | -> |       | -> |          |
|App |    | Cache |    | Database |
|    | <- |       | <- |          |
```

## Part 1: Features/Requirements/Constraints

Features that system should support. This part also involves making design requirements clear.

**Possible Questions:**
- What is the amount of data we need to cache?
  - A few TBs like Google, Twitter
- What should be the eviction strategy?
  - LRU or FIFO or Weighted LRU etc
- What is the access pattern?
  - Write through: write to db and cache both
  - Write around: write to db and get call fetches from db and writes to cache
  - Write back: write to cache. Cache syncs with the DB
- Persistent like Redis?
  - If yes? can be discussed in Part 4 about WAL, snapshot, log compaction.

## Part 2: High Level Design/Estimation

Goal of the system, system latency, availability, partition tolerance. This part involves a high level design diagram, how traffic flows through the system, some initial estimations.

```
|     | request ->  |       | -> |          |
| App |             | Cache |    | Database |
|     | <- response |       | <- |          |
```

**Possible Questions**
- Impact of latency on the system?
  - Low latency system. That's why we are using cache(duh)
- Consistency or availability?
  - Unavailability: Cache goes down. Our DB needs to handle all traffic. Adds latency.
  - Consistency: Usually for system using cache some inconsistency is often ok, so long the system is eventually consistent. Example twitter timeline.
- Total size of the cache: 30TB
- What is the expected QPS(queries/second)?
  - Lets assume for our system QPS is 10M.
  - This is required to calculate no of machines required.
- No of machines required?
  - Considering standard machines[[1]] ram can be 64GB or 128GB.
  - No of machines required: 30TB/64GB = 450 machines
  - This is absolute minimum with no replication or backup.
  - More machines might be required depending on QPS
  - For simplicity, assumption that all of the main memory will be available for caching

## Part 3: Design Core Components/Deep dive

Core components. This part involves the details about how the system will be implemented, data-structures, oop design, code

**Possible Questions**
- Single threaded or Multi threaded?
  - Single
- How LRU cache will work?
  - Should support O(1) `GET` and `PUT`.
  - `GET` should also move the data to front of cache.
  - `PUT` should add to the front.
  - Since we only have a limited space available, if the cache is full we need to design system in a way that it discards the oldest data.
- How to implement LRU cache?
  - Simple system where value is not that big
    - We can use hashmap and maintain an array of keys.
    - Maintain an array of keys and follow the move to front and discard operations described above.
  - Complex cached data
    - Use hash map and doubly linked list(dll).
    - On `PUT`, add a key to cache and data to linked list front.
    - On `GET`, move the dll node to the front.
    - When cache is full, discard the last node and pop the key from hashmap.
- Why doubly linked list?
  - `GET` and `PUT` involves move to front and discard operations respectively.
  - Both `GET` and `PUT` needs to be O(1) operation.
  - Double linked list nicely support movement of nodes without access to previous or next node.
- What if system is multi-threaded?
  - Multi threaded system has an advantage that move to front and discard operations can be done asynchronously.
  - But this makes the system very complex with locking, race condition and deadlock issues.
  - Decide what do you want to lock?
    - Whole hash-table?
    - Read lock or write lock?
    - Key level lock?
  - Locks should be on as granular level as possible. As this has system performance impact.

## Part 4: Scale The Design

Collecting all the parts and making a system design. This part involves scalability discussion, failures and what are the tradeoffs, rough calculations.

*Possible Questions**
- How to shard?
  - Machines required: 30TB/64GB = 450 machines
  - QPS/machine: 10M/450 = 22,000
  - CPU time/machine for 22k QPS: 4 * 1 seconds = 4 seconds
  - CPU time/machine/query: (4 * 1000 * 1000) / 22000 => 4 microsecond/22000 = 181us
  - Assuming 4 core standard machine[[1]]
  - Can a machine handle GET and SET operation(with locking, node movement to front, etc) in 181ms? No, we know this from [readme]. This means we need more machines to handle 10M QPS
- How to shard?
  - Increase CPU per machine i.e. from 4 to 8. With cloud providers like AWS and GCP you can choose different configurations.
  - Assuming 8 cores:
    - CPU time/machine/query: 363us
    - Not good enough considering context switch and other system tasks
  - Assuming machines with 16GB RAM and 4 cores:
    - No of machines required: 1875
    - QPS/machine: 5,000
    - CPU time/machine/query: 800us
    - This seems doable.
  - How to distribute keys in shards?
    - A simple approach: hash(key) % shard count
  - How to handle key collision?
    - Can use chaining with linked list
    - Other option, open addressing(don't!)
- Failure: What happens if a machine goes down?
  - Maintain replicas. Costly but reliable, out of sync data problem, more overhead, data missing and server goes down
  - Master-slave arch. Slave takes over if master down.



### Links

[1]: https://aws.amazon.com/ec2/instance-types/

[2]: https://github.com/amitt001/cs-review#latency