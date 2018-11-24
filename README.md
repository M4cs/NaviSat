<p align="center">
  <img src="https://i.imgur.com/dRgR69y.png" alt="navsat"></br>
  <a href="https://github.com/M4cs/NaviSat/network"><img src="https://img.shields.io/github/forks/M4cs/NaviSat.svg" alt="Forks"></a>
  <a href="https://github.com/M4cs/NaviSat/stargazers"><img src="https://img.shields.io/github/stars/M4cs/NaviSat.svg" atl="Stars"></a>
  <a href="https://github.com/M4cs/NaviSat/issues"><img src="https://img.shields.io/github/issues/M4cs/NaviSat.svg" alt="Issues"></a>
  <a href=""><img src="https://img.shields.io/badge/version-1.0.0-green.svg?syle=popout"></a>
  <a href="https://github.com/M4cs/NaviSat/blob/master/LICENSE.md"><img src="https://img.shields.io/github/license/M4cs/NaviSat.svg" alt="License"></a>
  <a href="http://www.python.org/download/"><img alt="Python 3.6+" src="https://img.shields.io/badge/Python-3.6+-yellow.svg"></a>
  <a href="https://discord.gg/7VN9VZe"><img src="https://img.shields.io/badge/discord-join-blue.svg?syle=popout"></a>
</p>
<p align="center">
  <b>NaviSat is a tool you can use to find locations and passing times of any NORAD satellite. This tool can be useful for finding when optimal times to intercept satellites are. Use this for educational purposes only. Requires n2yo.com API key.</b>
  <a href="https://asciinema.org/a/bYgFFg1yDqLyNoRSB9B9VRkV1" target="_blank"><img src="https://asciinema.org/a/bYgFFg1yDqLyNoRSB9B9VRkV1.svg" /></a>
</p>

# Getting Started:

NaviSat requires API access to [N2YO](https://n2yo.com/login/register). This is a free service that grabs information about satellites orbiting the earth. You can simply register and then head to your settings.

In your settings you must set a location:
<p align="center">
  <img src="https://image.prntscr.com/image/x9cjfKwVTAeI2jsRVhJqVw.png">
</p>

After setting a location retreive your API key from below:
<p align="center">
  <img src="https://image.prntscr.com/image/MFjYc9N1SpavA9sMRSd58A.png">
</p>

After obtaining a N2YO account and getting your API key clone the repository using git:
```
git clone git://github.com/M4cs/NaviSat.git
```

After you complete cloning the repository run the following commands:
```
cd NaviSat/
chmod +x navisat.py
./navisat.py
```

It will guide you through setting up a configuration and then allow you to start using the tool.

# Tools:

**All results are predictions made by N2YO**

### Search Function

NaviSat has a search ability that allows you to search for any satellites above your designated location and grabs their NORAD ID. You can then use this NORAD ID in the `vpasses` or `rpasses` command. 

### Radio Passes Function

NaviSat will grab information about upcoming satellite radio passes. You can search by NORAD ID. Use the `search` function to find a satellite ID.

### Visual Passes Function

NaviSat will grab information about upcoming satellite visual passes. You can search by NORAD ID. Use the `search` function to find a satellite ID.

# Gen. Info

Developed by [@maxbridgland](https://twitter.com/maxbridgland)

Support E-Mail: [mabridgland@protonmail.com](mailto://mabridgland@protonmail.com)

Licensed Under GNU GPL v3 License 
