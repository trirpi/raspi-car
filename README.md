# raspi car

Raspi car is a little Raspberry pi powered robot. You can control it trough a web interface.

The backend is powered by flask, gevent and flask-socketio.

Parts needed:
- raspberry pi
- Pimoroni explorer hat pro
- motors 
- battery pack
- chassis for robot

You should install a few packages:
    
    sudo apt install python-dev nginx git python-pip

Now you need to clone this repository and enter it:

    git clone https://github.com/trirpi/raspi-car.git
    cd raspi-car

Then you need to install the requirements. When you are in the home directory:

    sudo pip install -r requirements.txt
    
Then you need to setup nginx as a reverse proxy. So you need to edit `/etc/nginx/sites-enabled/default` to look like the following. Change <the ip of your pi> with your ip. You can retrieve your ip by typing `hostname -I`.

    server {
        listen 80;
        root /home/pi;
    
        server_name <ip of your pi>;
    
        access_log  /var/log/nginx/access.log;
        error_log  /var/log/nginx/error.log;
    
        location / {
            proxy_pass         http://127.0.0.1:5000/;
            proxy_redirect     off;
            proxy_set_header   Host                 $host;
            proxy_set_header   X-Real-IP            $remote_addr;
            proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto    $scheme;
        }   
    }  

Then you need to start and restart nginx:

    sudo service nginx start
    sudo service nginx restart
    
As a final step you should edit the sockets.js file located in `raspi-car/rcar/static/js/`. To have the socket connect to your raspberry pi's ip.

Then you just run the program:

    python start_rcar.py
    
When everything is working correctly you can navigate to the raspberry pi's ip in the browser and there is your web interface where you can drive forward/backword/left/right.


Enjoy!

Give my repo a star :) it helps me a lot.