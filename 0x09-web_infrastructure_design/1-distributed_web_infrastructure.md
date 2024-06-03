The distribution algorithm the load balancer is configured and how it works?
- The load-balancer is configured with the Round Robin distribution algorithm. This alorithm works by using each server behind the load-balancer in turns

The setup enabled by load-balancer?
- The HAproxy is enabling an Active-Passive setup rather than a Active-Active setup because in an Active-Passive setup not all nodes are going to be active. Example, if the first node is active the second node must be on standby

How a database Primary-Replica cluster Works?
- A Primary-Replica setup configures one server to act as the Primary server and the other servers to act as a replica to the primary server. However the primary is capable of doing read/write requests whilst the replica is only capable of read requests

The difference between primary and Replica node?
- The primary node can do read/write requests while the replica can only perform read requests

ISSUES

SPOF (Single Point of failure)
- If the primary mySQL database server is down the website is incapable of making any changes

Security Issues
- The data transmitted isn't encrypted so hackers can spy on the network

No monitoring
- There is no way of knowing the status of the servers without monitoring
