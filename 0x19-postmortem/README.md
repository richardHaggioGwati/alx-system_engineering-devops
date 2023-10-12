<h2>Issue Summary</h2>
<p>
<strong>Duration of the outage:</strong> The outage started at 10:00 AM GMT on October 11, 2023, and ended at 12:30 PM GMT on the same day.<br>
<strong>Impact:</strong> The main website was down, causing an inability for users to access our services. Approximately 60% of our users were affected.<br>
<strong>Root cause:</strong> A misconfiguration in the Nginx server led to the outage.
</p>

<h2>Timeline</h2>
<ul>
<li><strong>10:00 AM:</strong> The issue was detected through our monitoring alert system which showed a spike in 5xx HTTP status codes.</li>
<li><strong>10:15 AM:</strong> Initial investigation began, focusing on recent deployments and database integrity.</li>
<li><strong>10:45 AM:</strong> The issue was escalated to the site reliability team after initial checks found no issues with recent deployments or database integrity.</li>
<li><strong>11:30 AM:</strong> A misleading path was taken when investigating potential DDoS attacks.</li>
<li><strong>12:00 PM:</strong> The root cause was identified as a misconfiguration in the Nginx server.</li>
<li><strong>12:30 PM:</strong> The incident was resolved after reconfiguring the Nginx server.</li>
</ul>

<h2>Root Cause and Resolution</h2>
<p>
<strong>Root cause:</strong> An incorrect rewrite rule in the Nginx configuration was causing requests to be incorrectly routed, leading to “404 Not Found” errors being returned to users.<br>
<strong>Resolution:</strong> The incorrect rewrite rule in the Nginx configuration file was identified and corrected, and the Nginx server was restarted.
</p>

<h2>Corrective and Preventative Measures</h2>
<p>
<strong>Improvements/Fixes:</strong> Improve monitoring of server configurations and implement automated checks for configuration files before deployment.
</p>

<h3>Tasks:</h3>
<ul>
<li>Patch Nginx server with correct configuration (Done)</li>
<li>Add monitoring on Nginx server configuration (To Do)</li>
<li>Implement automated checks for configuration files (To Do)</li>
</ul>
