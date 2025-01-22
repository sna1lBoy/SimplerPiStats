# SimplerPiStats
An even simple UI designed for people running their Raspberry Pi as a server, and who quick and easy to read stats and control of their system.

## Please ensure that git is installed before running the install command

## How to install/update
Simply change directory (`cd`) into the directory where you want to store SimplerPiStats, then run the following command:

`bash <(curl -s https://codeberg.org/snailboy/SimplerPiStats/raw/branch/main/install.sh)`

If you with to use SimplerPiStats without a virtual environment (venv), use the following command instead:

`bash <(curl -s https://codeberg.org/snailboy/SimplerPiStats/raw/branch/main/non-venv_install.sh)`

## How to use
Type the following into a web browser `<your pi's local ip address>:5556`. If you need help finding your Pi's local IP address, simply ssh into the Pi, and type in `hostname -I`, your Pi's local IP address is everything before the space.

### How to read the CPU state
:] Means your Pi's CPU is happy! (Under 40%)

:| Means your Pi's CPU is under a bit of load, but it's still okay (Between 40% and 75%)

\>:[ Means your Pi is Angry. (Over 75%)

### How to read the temperature
🔥 Means your Pi's temperature is around normal. (Below 50°C)

🔥🔥 Means your Pi's temperature is a little bit warm. (Between 50 and 70°C)

🔥🔥🔥 Means your Pi's H O T! (above 70°C, and you should probably do something rather quickly.)

## Possible features