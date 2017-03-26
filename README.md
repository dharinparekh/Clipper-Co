
# Clipper-Co.
![alt tag](https://github.com/dharinparekh/Clipper-Co./blob/master/design/7[new].png) <br />
This is an app that can be used to share clipboard between various users. A user can share his/her clipboard among his/her device via his/her login credentials, also a particular user can share the clipboard without sharing the credentials using a OTP.  

### Advantages for common clipboard that we built
* Contents can be pasted directly into any remote computer's application.
* Multiple users (more than 2) can be connected via sharing the same otp thus allowing multiusers to share the same clipboard.
* The clipboard contents are sent to the connected computer only which saves network bandwidth.
* Copying the same text accidently will not publish the changes to clipboard thus preventing data loss.
* The size of packets is very less as compared to other systems.
* The quality of service is optimal.
* The best part is it save a lot of time and network bandwidth as comapred to other options e.g(mailing the text) which take around 30+ seconds and ours around 6sec(connection time included), imagine the same scenario but magnitude around 100 times more.
* Also since it is open source other remote sharing applications can be built using the same backend functions.
* It's available accross all the common platforms(linux, windows, android)


##  Installation
Download the repository or clone it and go to packaged folder and then to your respective os directory, unzip it and run the executable file, that's it :)  
We have tested accross multiple systems but if it still fails to work then you can run the application by running the gui.py file

if the double click doesn't work in linux that means you don't have the permission to execute the file just type
```
-> chmod +x gui
-> ./gui
```

```python
>> pip install requirements.txt
>> # for linux
>> cd linux
>> python gui.py

>> # for windows
>> cd windows
>> python gui.py
```  
for android just install the apk

## How to use it
To see how to use the app you can watch the video
[here](link/to/youtube/video)   

## Live typing
Another application that we built using the same backend logic was live typing, it is exaclty the remote access to one's keyboard. The demonstration of it can be viewed in the video.  
The purpose of this application was to demonstrate that other applications along the same lines can be built using the same backend logic.

* This feature is very useful for the tech related companies to provide better customer support(to repair software related problems of pcs).
* This feature is only for windows and linux.
* Our backend send only 3 bytes per character typed which almost 1/10 th of the Normal IP packet which is around 40 bytes, thus saving a lot of network bandwidth.
* Multiple users can listen to one port and the host will type this will be propogated amongst all the users, this is best for teaching purposes(for eq teaching python the teacher will just type on his interpreter which will pe propogated to all the connected students).
