# Caching Proxy Server

This command-line interface (CLI) script enables you to create a caching proxy server. Pass in a port and an origin url and the server will act as a caching proxy for the origin.

## Installation
### Clone the repository:

`git clone https://github.com/samjove/caching-proxy.git`

`cd caching-proxy`

### Set up a virtual environment (optional):

`python3 -m venv venv`

`source venv/bin/activate` 

On Windows, use `venv\Scripts\activate`

### Install the required Python packages:

`pip install -r requirements.txt`

### Windows
#### Create a batch file

Edit the included .bat file in the 'windows' directory to run the script as a command without the .py extension. 
Replace the file path with the full path to your script.

#### Add the batch file to PATH

Place the .bat file in a directory that is already included in your system's PATH environment variable (e.g., C:\Windows\System32). This allows you to run the script from anywhere without specifying the full path.

### Unix-based Systems
#### Make the script executable

Save the script, e.g., caching_proxy.py.

Open your terminal and run:

`chmod +x caching_proxy.py`

#### Move the script to a directory in PATH

Move the script to a directory that is included in your PATH (e.g., /usr/local/bin):

`sudo mv caching_proxy.py /usr/local/bin/caching_proxy`

Now, you can run the script by typing proxy from any directory.

## Running the Application

If you added the script to your path it can be run with:

`caching_proxy --port <port> --origin <origin_url>`

For example, if you wanted to create a proxy for dummyjson.com on port 3000 you would run the following:

`caching_proxy --port 3000 --origin https://dummyjson.com`

Otherwise it should be run with:

`python caching_proxy.py --port <port> --origin <origin_url>`

If this is running on your local, any requests made to localhost:3000 will be passed on to dummyjson.com,
as long as the response has not been previously cached. [Here's](https://dummyjson.com/docs) the dummyjson api docs
if you want to try it.

The cache used is a file system cache through the Flask-Caching extension. There will be a 'cache' directory created within the app directory.

See project requirements [here](https://roadmap.sh/projects/caching-server).