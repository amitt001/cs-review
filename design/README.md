# System Design

How to solve?

1. Outline use-case and constraints.
   1. What in-scope?
   2. What's out of scope?
   3. Assumptions with some rough rounded traffic values
   4. Calculate - data size in a month & 3 years, traffic/second, read:write ratio
2. Create a high-level design
   1. A very high level core-component sketch
3. Design core component
   1. Here talk about how messages are going to flow.
   2. What db to use.
   3. What db schema is going to look like.
   4. Ask if you are supposed to write code.
   5. Also write some code.
4. Scale the design
   1. Identify and address the bottlenecks
   2. Iteratively add components to the design in part 2 by discussing about the bottlenecks.
   3. This section can be very broad. Spend most of the time here discussing ideas. Find bottlenecks, fix, repeat.

# Handy Calculations

- 2.5 million seconds per month
- 1 request/second => 2.5 million/month
- 4 request/second => 10 million/month
- 40 request/second => 100 million/month
- 400 request per second => 1 billion/month

## Core Components

- **Consistent hashing**
  - Better hashing than the modulus based hashing for handling hash map resizing
  - Modulus or any hashing that depends on size of hash table has a disadvantage that resizing requires remapping all the keys.
  - With consistent hashing ring only k/n keys needs to be remapped.
  - k -  no of keys, n -  no of hash table slots
  - Source: https://youtu.be/bBK_So1u9ew?t=755
  - Used by dynamo, couchbase, Akamai etc

- **Load Balancer**
  - L3 - IP based
  - L4 - DNS based
  - L7 - Application based, SSL termination