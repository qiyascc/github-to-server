


# Setup

1. Clone the repo you want to set up.
   - ```git clone https://github.com/username/reponame/```

3. Get the code and customize it to your liking.
   - Requirements:
      - Flask: ```pip install flask```
      - If you are using a web server like nginx, set up the necessary configurations in the configuration files.
          - Example nginx configurations;
           ```
        location /github-to-server {
                proxy_pass http://localhost:5000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           }
           ```

5. Go to the cloned github repo and open the settings section.
![Webhook](https://graph.org/file/29d1686aa0035b4aa1dae.jpg)
6. Click on Webhook and create a new webhook.
    - Enter the address you set up on the server.
    - Set up a secret key for yourself.

7. Add the key you have set up to your code and run the code.
