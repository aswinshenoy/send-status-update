# Send Status Update
A python based script to make the process of sending status update much more easier with beautiful predefined templates.

## How to Use?
1. Clone this repository.
2. Make sure required python libraries are installed.
3. Create and update intro.html, work.html, signature.html as per requirment.
4. Add your email credentials to mail.py, and also the reciever's email.
5. Run the python file :) 

*you can skip the steps 1 to 4 from the next day, except that you have to update daily work done in work.html.*

## Template Files 

**intro.html** - Contains general salutation & introduction
~~~
<b> Nama Shivayah </b>
~~~
**work.html** - Contains general salutation
~~~
<ul>
  <li> I did this today </li>
</ul>
<div><b>Hours Worked: </b> 24</div>
~~~
**signature.html** - Contains email signature
~~~
<div>
  <b>With Regards,</b><br>
  <div style="display: flex; align-items: center; padding-top: 0.5rem;">
    	<div style="width:5vw; min-width: 45px;">
    		  <img src="https://aswinshenoy.com/assets/img/profile-pic.jpg" style="width: 80%; border-radius: 100vmax;">
    	</div>
    	<div style="max-width:95vw;">
      		Ashwin S Shenoy,<br>
      		Amrita Vishwa Vidyapeetham, Amritapuri Campus<br>
      		<a href="https://aswinshenoy.com">Website</a> | <a href="https://github.com/aswinshenoy">GitHub</a> | <a href="https://linkedin.com/in/aswinshenoy">LinkedIn</a>
    	</div>
  </div>
</div>
~~~

