## What is the project?

I've created a little MicroPython-based project on that combines the following:

* An ESP32 microcontroller running MicroPython
    * a basic RC servo class for converting position commands to a PWM signal
    * the microdot web "micro" framework for serving a simple web app for controlling gait parameters
    * The ability to work on either an existing wifi network or standalone as an access point.

Here's how to get it running:

1. Install a code editor for working with the ESP32.  I prefer VSCode with the Pymakr-preview plugin; Thonny is a rudimentary yet functioning alternative
1. Flash micropython v1.20 or newer on to your ESP
1. Open up the project and define an internet-connected wifi access point to connect to (for the first time).
1. Upload the project to the microcvontroller and reset the ESP.

> I have tutorials for each of these steps.  Please reach out if you would like more details.

The ESP, when started up, will download a couple libraries from the internet and then soft reset itself. Once restarted, it will host a webpage at its ip address.  You can use the page to control various aspects of the servos.

> Once the libraries are downloaded, you can also reprogram the ```boot.py``` file so that the ESP acts as its own wifi-access point.

I have provided a basic example with four servos.  The schematic can be seen here:

![Schematic](images/servos_schem.png) 

![Breadboard](images/servos_bb.png)

## Sinusoidal Control

Each servo is controlled by the following equation

$\text{y}=A\sin\left(2\pi(ft-l_x)\right)+b$

where $y$ is the desired angle, $t$ is the current time in seconds, and the other variables in the expression correspond to the following adjustable parameters:

| Parameter | Meaning             |
| --------- | ------------------- |
| $A$       | Amplitude           |
| $f$       | frequency           |
| $b$       | Y-offset          |
| $l_x$     | Servo x time offset |

This gives you the ability to control the amplitude of your signal with $A$:

![Amplitude](images/plt-amplitude.png)

You can also change the frequency of your signal using $f$:

![Frequency](images/plt-frequency.png)

You can shift the output of the desired output up or down with $b$

![Y-Offset](images/plt-offset.png)

You can also shift the timing of your signal by playing with $l_x$

![Time Offset](images/plt-time-offset1.png)

## Gaits

The time offset paramters, $l_x$, are specified in fractions of a full cycle.  Thus, $l_x=0$ means the sinusoid crosses the x axis traveling in the positive direction at t=0, $l_x=0.5$ means the sinusoid is shifted in x by $\frac{f}{2}$ (crosses teh x axis traveling in the negative direction), and $l=1$ means your signal has wrapped around back to the beginning again.  Thus, if you want to program a series of motors to be time-shifted in terms of fractions of a gait, you just have to play with the $l_x$ parameters to achieve very different results.

You can adjust all $l_1$, $l_2$, $l_3$, $l_4$ to be evenly distributed in time:

![Four Servos](images/four-servos.png)

Or you can sequence two to be nearly on top of one another:

![Different Timings](images/four-servos2.png)

## Videos

<!-- ### Programming the ESP -->

### Controlling Gait parameters

<iframe width="560" height="315" src="https://www.youtube.com/embed/m382Uk8sjKo?si=YJiVvnw2934qE8wO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
