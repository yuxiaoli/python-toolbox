http://ilab.cs.byu.edu/python/threadingmodule.html

Windows Compatibility
Note: File objects on Windows are not acceptable, but sockets are. On Windows, the underlying select() function is provided by the WinSock library, and does not handle file descriptors that don’t originate from WinSock.

