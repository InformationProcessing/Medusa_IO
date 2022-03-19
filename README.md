# Medusa_IO
EIE2 InfoProcessing Coursework group 13

## pip packages
To run the project, following pip packages must be installed
- `intel_jtag_uart`
- `tkinter`
- `tk`
- `simpleaudio`
- `pydub`

## Setup
In order run the game, firstly run the server by running the following command from the `SnakeVisualiser` directory.

````shell
python3 SnakeServer.py
````

To run the game client, run the following command from the root diretory `Medusa_IO` directory.

````shell
python3 SnakeVisualiser/SnakeClient.py
````

## Notes

Working for one food only
We are currently deleting all other foods
Sometimes bugs and food no longer generates

# Networking allocation UDP

In order to setup the networking on Windows go to Windows Defender Firewall with Advanced Security and perform two following steps:

- Go to `Inbound rules`
  - Click on `New rule`
  - Select `Port` and click `Next`
  - Select `UDP`,set the inbound port and click `Next`
  - Select `Allow the connection` and click `Next`
  - Leave everything as it is and click `Next`
  - Name the rule and click `Finish`
- Go to `Outbound rules`
  - Click on `New rule`
  - Select `Port` and click `Next`
  - Select `UDP`,set the inbound port and click `Next`
  - Select `Allow the connection` and click `Next`
  - Leave everything as it is and click `Next`
  - Name the rule and click `Finish`

The following setup was introduced for each member of the team. 

- Alex: inbound - 12000 (local main server); outbound - 514 (client side server)
- Vaclav: inbound - 12010 (local main server); outbound - 515 (client side server)
- James: inbound - 12020 (local main server); outbound - 516 (client side server)

# Snake coordinates protocol

The snake coordinates file protocol has the following format: `client name|snake coordinates|food configuration`
Example of the coordinates file protocol
````
Client 0|190,200;190,190;190,180;190,170;190,160;190,150;190,140;190,130;190,120;190,110;|0,0,0,0,0
````