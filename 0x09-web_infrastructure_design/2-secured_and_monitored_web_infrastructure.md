The purpose of firewalls?
- Firewalls are for protecting your network from unauthorized users by acting as an intermediary between the internal and external networks and blocking the incoming traffic

The purpose of the SSL certificate?
- The SSL certificate is for encrypting the traffic between the servers and the external network to prevent MITL attacksand network sniffers from sniffing traffic which could expose important information.

The purpose of monitoring clients?
- The clients are for monitoring the servers and external networks. They analyse and measure the health of the servers and alert admins if the servers are not working as intended. The client monitors the servers and provides key metrics about the servers operations

ISSUES

- Terminating SSL at the load-balancer will leave the traffic between the load-balancer and servers unencrypted
- Having one mySQL server is an issue because its not scalable
- Having servers running the same components can lead to an increase in resources like CPU and Memory usage which can lead to performance drops
