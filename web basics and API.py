'''
#1)
An access token is an object that describes the security context of a process or thread. 
The information in a token includes the identity and privileges of the user account associated with the process or thread.
When a user logs on, the system verifies the user's password by comparing it with information stored in a security database.
If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has acopyof this access token.

#2)
facebook=151.101.65.121  #ip address
Google-->
Google uses the following public IP address ranges:
64.233.160.0 – 64.233.191.255
66.102.0.0 – 66.102.15.255
66.249.64.0 – 66.249.95.255
72.14.192.0 – 72.14.255.255
74.125.0.0 – 74.125.255.255
209.85.128.0 – 209.85.255.255
216.239.32.0 – 216.239.63.255
Ip address ofInstagram-->
31.13.76.84
Only certain addresses from Google's pool work at any given time depending on how Google chooses to deploy its web server network, which is why a random example above one of these ranges may or may not work for you at a specific time.
When you find an IP address that works for you, make a note of it for future use.
Why You Might Want Google's IP Address-->
If all is working normally, you can visit the Google search engine at Google.com.
However, it's also possible to reach it using one of Google's IP addresses, even when the domain can't be reached by name.
If there's an issue with DNS, and Google's IP address can't be found by entering "google.com," you can instead enter the URL as a valid IP address in the form http://74.125.224.72/.
Some IP addresses work better than others depending on your locale.
Testing connections to websites by addresses instead of names can be a helpful troubleshooting step to verify whether the connection has an issue with name resolution rather than some other kind of technical glitch.
Also, website administrators are often curious to know when Google web crawlers visit their sites.
Analyzing web server logs reveals the IP addresses of crawlers but not their domains.
#3)
What is HTTP?
The Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers.
HTTP works as a request-response protocol between a client and server
A web browser may be the client, and an application on a computer that hosts a web site may be the server.
The GET Method-->
GET is used to request data from a specified resource.
GET is one of the most common HTTP methods.
**Note that the query string (name/value pairs) is sent in the URL of a GET request:
/test/demo_form.php?name1=value1&name2=value2**
Some other notes on GET requests-->
1.GET requests can be cached
2.GET requests remain in the browser history
3.GET requests can be bookmarked
4.GET requests should never be used when dealing with sensitive data
5.GET requests have length restrictions
6.GET requests is only used to request data (not modify)
The POST Method-->
POST is used to send data to a server to create/update a resource.
POST is one of the most common HTTP methods.
**The data sent to the server with POST is stored in the request body of the HTTP request:
POST /test/demo_form.php HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2**
Some other notes on POST requests-->
1.POST requests are never cached
2.POST requests do not remain in the browser history
3.POST requests cannot be bookmarked
4.POST requests have no restrictions on data length
The PUT Method-->
PUT is used to send data to a server to create/update a resource.
-->The difference between POST and PUT is that PUT requests are idempotent. 
-->That is, calling the same PUT request multiple times will always produce the same result.
-->In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.
The DELETE Method-->
The DELETE method deletes the specified resource.
#4)
API( is a part of library which defines how an application communicates with external code)
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
For further reading : https://stackoverflow.com/questions/3678665/is-there-still-a-difference-between-a-library-
We can create our own APIs using Python Framework like Django and Flask which can be used in websites.
You can follow documentation of Django in order to create your own website with Python. Check this out:
https://docs.djangoproject.com/en/2.0/
'''
