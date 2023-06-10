# Nanodrop

nanodrop.py runs a simple HTTP server on port 8000 that allows anyone (0.0.0.0/0) to connect to it. This is practical for quick sharing of files in one direction.

To use this code, run it with Python. If art.txt exists in the same directory as the code file, its contents will be printed to the console. The HTTP server will start listening on port 8000 regardless of whether or not art.txt exists.

To view the contents of the working directory, go to http://IP_OF_SERVER:8000/ in your browser. Make sure to refresh the page to get the latest contents of the directory.

The program "screen" can be used to run Nanodrop in the background

1. screen -R nanodrop
2. python3 nanodrop.py
3. key combo CTRL-A then CTRL-D to detach from screen session.
4. session can be reaccessed using "screen -x nanodrop"
