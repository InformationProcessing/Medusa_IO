# Medusa_IO
EIE2 InfoProcessing Coursework group 13

https://youtu.be/ykUQqOHmgx0

## pip packages
To run the project, following pip packages must be installed
- `intel_jtag_uart`
- `tkinter`
- `tk`
- `simpleaudio`
- `pydub`

## Setup
In order run the game, firstly clean coordinates of snakes from the previous game by running the following command in the `SnakeVisualiser` directory.

````shell
python3 snakecoordcleaner.py
````

Then run the server by executing the following command in the `SnakeVisualiser` directory.

````shell
python3 SnakeServer.py
````

To run the game client, run the following command from the root diretory `Medusa_IO` directory.

````shell
python3 SnakeVisualiser/SnakeClient.py
````

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

| Name   | IP address    | Inbound port | Outbound port |
|--------|---------------|--------------|---------------|
| Alex   | 192.168.0.101 | 12112        | 512           |
| Vaclav | 192.168.0.100 | 12010        | 515           |
| James  | 192.168.0.105 | 12020        | 516           |
| Michal | 192.168.0.102 | 12080        | 518           |
| Mathew | 192.168.0.104 | 12001        | 521           |
| Charmaine | 192.168.0.103 | 12102        | 522           |

# Snake coordinates protocol

The snake coordinates file protocol has the following format: `client name|snake coordinates|food configuration`
Example of the coordinates file protocol
````
Client 0|190,200;190,190;190,180;190,170;190,160;190,150;190,140;190,130;190,120;190,110;|0,0,0,0,0
````
