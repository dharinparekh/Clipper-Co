
![alt tag](https://github.com/dharinparekh/Clipper-Co./blob/master/design/top.png) <br />
# Clipper-Co.
This is an app that can be used to share clipboard between various users. A user can share his/her clipboard among his/her device via his/her login credentials, also a particular user can share the clipboard without sharing the credentials using a OTP. 
Now, what do we mean by sharing your clipboard? Well, you copy some text on one device (via CTRL + C or any other means) and that text can now be pasted on another device, or rather, a number of other devices! The ultimate simplification of sharing texts between multiple devices!

### Advantages for common clipboard that we built
* A common clipboard for all your devices, copy once, paste everywhere.
* Contents can be pasted directly into anything on the remote computer.
* Multiple users (more than 2) can be connected via sharing the same otp thus allowing multiusers to share the same clipboard.
* The clipboard contents are sent to the connected computer only which saves network bandwidth.
* Copying the same text accidently will not publish the changes to clipboard thus preventing data loss.
* The size of packets is very less as compared to other systems.
* The quality of service is optimal.
* The best part is it save a lot of time and network bandwidth as comapred to other options e.g(mailing the text) which take around 50+ seconds and ours around 6sec(connection time included), imagine the same scenario but magnitude around 100 times more.
* Also since it is open source other remote sharing applications can be built using the same backend functions.
* It's available accross all the common platforms(linux, windows, android)


##  Installation
Download the repository or clone it and go to packaged folder and then to your respective os directory, unzip it and run the executable file, that's it :)  
We have tested accross multiple systems but if it still fails to work then you can run the application by running the gui.py file.

If the double click doesn't work in linux that means you don't have the permission to execute the file just type
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
For android just install the apk. (Currently only tested on Android 7.0+)

## Demonstration of the app
Click the below image to view the video 
[![image](http://img.youtube.com/vi/SMw1c34_NJA/0.jpg)](https://youtu.be/SMw1c34_NJA)  

## Easter Egg: Live typing
Another application that we built using the same backend logic was live typing, it is exaclty the remote access to one's keyboard. The demonstration of it can be viewed in the video.  
The purpose of this application was to demonstrate that other applications along the same lines can be built using the same backend logic.

* This feature is very useful for the tech related companies to provide better customer support(to repair software related problems of pcs).
* This feature is only for windows and linux.
* Our backend send only 3 bytes per character typed which almost 1/10 th of the Normal IP packet which is around 40 bytes, thus saving a lot of network bandwidth.
* Multiple users can listen to one port and the host will type this will be propogated amongst all the users, this is best for teaching purposes(for eg teaching python the teacher will just type on his interpreter which will pe propogated to all the connected students).

## How to use this feature?
The gui isn't built yet but works standalone, go into the respective os folder and execute the following command

For the pc which is getting connected to host:

```python
>> python copy_text_receive.py
```
For the pc which is going to be the host:

```python
>> python copy_text_send.py
```


![alt tag](https://github.com/dharinparekh/Clipper-Co./blob/master/design/final_new.png) <br />
