# Resources I used
- [Awk](https://www.google.com/search?q=awk+linux&oq=awk+linux&aqs=chrome..69i57j0i512l9.3315j0j7&sourceid=chrome&ie=UTF-8)
- [quick-sed-intro](https://angel.hashnode.dev/short-sed-intro)
- [HOW TO SETUP SSL-HTTPS ON HAPROXY LOAD_BALANCER](https://mustaphaaliyugaladima.medium.com/how-to-setup-ssl-https-on-haproxy-load-balancer-a47bee7bc146)
# Fixing Errors
- [HAproxy SSL/TLS Warning: Setting tune.ssl.default-dh-param to 1024 by default]([https://](https://www.digitalocean.com/community/tutorials/haproxy-ssl-tls-warning-setting-tune-ssl-default-dh-param-to-1024-by-default))

- This command will start haproxy in the foreground with debug logging enabled, which may provide more information about **why it is failing to start**.  
`sudo haproxy -f /etc/haproxy/haproxy.cfg -d`


- Reference Article below for more debugging commands
  - [How To Troubleshoot Common HAProxy Errors](https://www.digitalocean.com/community/tutorials/how-to-troubleshoot-common-haproxy-errors)
