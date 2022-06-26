# DDOS-Attack-code-with-python
DDOS Attack code with python

     
``` what is DDOS Attack?  ```


A distributed denial-of-service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service or network by overwhelming the            target or its surrounding infrastructure with a flood of Internet traffic.


``` How does a DDoS attack work? ```

DDoS attacks are carried out with networks of Internet-connected machines.

These networks consist of computers and other devices (such as IoT devices)which have been infected with malware, allowing them to be controlled remotely by an attacker. These individual devices are referred to as bots (or zombies), and a group of bots is called a botnet.

Once a botnet has been established, the attacker is able to direct an attack by sending remote instructions to each bot.

# in our code example you can see a loop with for i in range (500) 500 is the number of zombies we have ;)  

When a victim’s server or network is targeted by the botnet, each bot sends requests to the target’s IP address, potentially causing the server or network to become overwhelmed, resulting in a denial-of-service to normal traffic.

Because each bot is a legitimate Internet device, separating the attack traffic from normal traffic can be difficult.

 ``` first three variables are for ```

 first one is for the target you can change it with the target domaine name ( yes DDOS work using DNS too not only IP adress ) 
 second one is for the port as it's known the port web is 80 
 fake_ip is for creating an fake IP adress for you as an attacker to not be easy to identify by caps ( this code is not created to be used for illegal reasons you take the full responsability on the way you use it ) 

those three variables should be changed to be addapted for each attack in this example i tryed it on my self when i putted my local ip adress in the first variable 



```How to identify a DDoS attack```
The most obvious symptom of a DDoS attack is a site or service suddenly becoming slow or unavailable. But since a number of causes — such a legitimate spike in traffic — can create similar performance issues, further investigation is usually required. Traffic analytics tools can help you spot some of these telltale signs of a DDoS attack:

    Suspicious amounts of traffic originating from a single IP address or IP range
    A flood of traffic from users who share a single behavioral profile, such as device type, geolocation, or web browser version
    An unexplained surge in requests to a single page or endpoint
    Odd traffic patterns such as spikes at odd hours of the day or patterns that appear to be unnatural (e.g. a spike every 10 minutes)

There are other, more specific signs of DDoS attack that can vary depending on the type of attack.
