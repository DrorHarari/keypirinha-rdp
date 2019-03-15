Keypirinha Plugin: Rdp
=========
# Launch previously opened Rdp sessions

This plugin for Keypirinha lets you type Rdp and part of the name of a machine you previously connected to and it will launch the Windows RDP program (MSTSC) to connect to that machine.

## Usage ##
Open the LaunchBox and type:
```
Rdp <tab> <partial-machine-name> <enter>
```
## Installation and Setup ##
The easiest way to install Rdp is to use the [PackageControl](https://github.com/ueffel/Keypirinha-PackageControl) plugin's InstallPackage command. 

For manual installation simply download the rdp.keypirinha-package file from the Releases page of this repository to:

* `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**

**Or** 

* `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** 


## Credits ##

* Icon by David Cross, Hungary (https://webhostingmedia.net/)

## Release Notes ##

**V0.1**
- Initial release
