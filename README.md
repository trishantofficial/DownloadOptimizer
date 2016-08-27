<h1>DownloadOptimizer</h1>
<h3>Optimizes download speed for a particular connection.</h3>
<h2>Requirements:</h2>
<h4>
<ul>
<li>Python 2.x</li>
<li>Modules:
<ol type="i">
<li>multiprocessing</li>
<li>os</li>
<li>psutil</li>
<li>urllib</li>
<li>urllib2</li>
</ol>
</li>
</ol>
</h4>
<h3>
How to install:
<ol type="a">
<li>Install Python 2.x, from <a href="https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi">here (python.org)</a>.</li>
<li>Install a package manager like pip or easyinstall for python.<ul><li><a href="https://pip.pypa.io/en/latest/installing/">pip</a></li>
<li><a href="http://simpledeveloper.com/how-to-install-easy_install/">easy_install</a></li>
</ul>
</li>
<li>Install the above mentioned modules using the installed package manager.(Only psutil is required to be downloaded since, others are accompanied by the python installer itself).</li>
<li>Change the directory to the DownloadOptimzer package.</li>
<li>Run the program using <font color="#4169E1">python __init__.py</font></li>
<li>Enter URL of the file you wish to download and the number of desired partitions.</li>
</ol>
</h3>
<h3>Note: Number of threads should be in accordance with the no. of CPU cores to prevent lag or freezing of the computer.</h3>
<h3>Note: Number of threads should be in accordance with the file size, for further optimization of download speed. Size of the file to be downloaded &prop; Number of threads</h3>
<h3>
How does it work:
<ol type="1">
<li>Creates a connection to the URL passed to it.</li>
<li>Records the response from the request and decides on the basis of recieved HTTP headers if the hosting server supports downloading the content in N number of parts as requested by the user.</li>
<li>Manipulates the HTTP request headers to download the file in parts simultaneously, to utilize the whole CPU instead of allowing it to be idle.</li>
<li>The downloaded parts are then combined in order, to finally acquire the requested download.</li>
</ol>
</h3>
<h4>
Present shortcomings:
</h4>
<h5>
<ul>
<li>GUI under development.</li>
<li>Browser-specific integration.</li>
</ul>
</h5>