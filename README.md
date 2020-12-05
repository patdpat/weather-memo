# Instructions to deploy application using Jenkins (linux)
## Step 1: Install Jenkins and extra packages
check out the contents of initial-setup.sh . This helps you install some necessary packages.
in your teminal type this command
```
$ vi initial-setup.sh
```
and Copy the contents of the [file](https://github.com/vahiwe/Django-CI-CD-Pipeline/blob/master/initial-setup.sh) to the server.

Save and close the file. Run the script to install the packages.
```
$ chmod +x initial-setup.sh

$ ./initial-setup.sh
```
Once the script is done, visit your servers public IP on port 8080 to view the Jenkins dashboard (http://<YOUR SERVER’S IP>:8080). You’ll see a screen like the one below.

![alttext](image/show.png)

To get your administrator password, run this command to get it.
```
$ sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
This will output your administrator password. The username associated with this password is admin incase you want to log in with this user. Once you input your administrator password you get a page asking for installation of plugins.

![alttext](image/show2.png)

Select Install suggested plugins to install some standard plugins that will help during your pipeline setup. Once the installation is done you are asked to create a normal user.

![alttext](image/show3.png)

After creating the user, you are asked to set your Jenkins URL. Leave it as default and now you should be logged in.

![alttext](image/show4.png)

## Step 2: Disable SELinux and extra Jenkins configuration
Run this command to check the status of SELinux:
```
$ sestatus
```
If it is enabled and set to enforcing mode, then we’ll change it to permissive mode. Nginx might not get access to your socket file if these instructions are not carried out. Open the SELinux configuration file:
```
$ sudo vi /etc/selinux/config
```
Change enforced to permissive

```
// Remove
SELINUX=enforcing

// Replace with 
SELINUX=permissive
```
Save and close the file.

You have to switch the user running the jobs from Jenkins to a user with sudo privilege. I’ll be switching to centos user. Open up the this script (using VI or other editor):
```
$ sudo vi /etc/sysconfig/jenkins
```
Find this line and change to “centos” or any user you prefer:
```
$ JENKINS_USER="centos"
```
Then change the ownership of Jenkins home, webroot and logs:
```
$ sudo chown -R centos:centos /var/lib/jenkins 

$ sudo chown -R centos:centos /var/cache/jenkins

$ sudo chown -R centos:centos /var/log/jenkins
```
Restart Jenkins and check the user has been changed:
```
$ sudo /etc/init.d/jenkins restart 

$ ps -ef | grep jenkins
```
Now you should be able to run the Jenkins jobs as the centos user. Now you can reboot the server:
```
$ sudo shutdown now -r
```
Reconnect back to your instance and check the status of SELinux:
```
$ sestatus
```
If it has changed to permissive then you’re good to go.

## Step 3: Setup Jenkins Pipeline
Log in to the Jenkins dashboard.

![alttext](image/show5.png)

On the left sidebar click on Manage Jenkins. This opens the Management dashboard of Jenkins. Click on ‘Configure Global Security’. Scroll down and enable ‘Enable proxy compatibility’ on the ‘CSRF Protection’. Apply and Save.

![alttext](image/show6.png)

Now we can setup the Jenkins pipeline. Go to Jenkins home and Click on New Item. Enter Name and select Pipeline:

![alttext](image/show7.png)

Go on to the next page. Scroll down, switch pipeline definition to `Pipeline Script from SCM`, Select Git as the SCM and Input your repository URL.

![alttext](image/show8.png)

Add a trigger to the pipeline to rerun when there’s a new commit. This is what updates the code changes to your application automatically without you manually running the commands. You can add multiple triggers like running at different times of the day. The triggers makes use of the linux cron job string format. 

![alttext](image/show9.png)

Once all this is done you can Apply and Save. Your Pipeline should start running anytime soon. If you check the README of the project used in this article there are some prerequisite steps that should be carried out to have everything running smoothly.

![alttext](image/show10.png)

The pipeline ran successfully. Though this doesn’t guarantee that everything is okay. You can check the logs of the stages in the pipeline to verify that everything is working.

![alttext](image/show11.png)

![alttext](image/show12.png)

After checking the logs of all stages looks like everything ran fine. Now we can visit the webpage using the IP Address of the server.