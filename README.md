# homographs
IDN homograph attack

```
python homo.py -h                
                                                                      
    HHHHHHHHH     HHHHHHHHH                                                          
    H:::::::H     H:::::::H                                                          
    H:::::::H     H:::::::H                                                          
    HH::::::H     H::::::HH                                                          
      H:::::H     H:::::H     ooooooooooo      mmmmmmm    mmmmmmm      ooooooooooo   
      H:::::H     H:::::H   oo:::::::::::oo  mm:::::::m  m:::::::mm  oo:::::::::::oo 
      H::::::HHHHH::::::H  o:::::::::::::::om::::::::::mm::::::::::mo:::::::::::::::o
      H:::::::::::::::::H  o:::::ooooo:::::om::::::::::::::::::::::mo:::::ooooo:::::o
      H:::::::::::::::::H  o::::o  b  o::::om:::::mmm::::::mmm:::::mo::::o     o::::o
      H::::::HHHHH::::::H  o::::o  e  o::::om::::m   m::::m   m::::mo::::o     o::::o
      H:::::H     H:::::H  o::::o  t  o::::om::::m   m::::m   m::::mo::::o v1  o::::o
      H:::::H     H:::::H  o::::o  a  o::::om::::m   m::::m   m::::mo::::o     o::::o
    HH::::::H     H::::::HHo:::::ooooo:::::om::::m   m::::m   m::::mo:::::ooooo:::::o
    H:::::::H     H:::::::Ho:::::::::::::::om::::m   m::::m   m::::mo:::::::::::::::o
    H:::::::H     H:::::::H oo:::::::::::oo m::::m   m::::m   m::::m oo:::::::::::oo 
    HHHHHHHHH     HHHHHHHHH   ooooooooooo   mmmmmm   mmmmmm   mmmmmm   ooooooooooo   
    [Homo]graph  

usage: homo.py [-h] [--version] [-d DOMAIN] [-v] [-rd RANDOM_DOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

domain:
  -d DOMAIN, --domain DOMAIN
                        Generates domain variations
  -v, --all_domain      Show all domains variations
  -rd RANDOM_DOMAIN, --random_domain RANDOM_DOMAIN
                        Random domain homograph


```


## Example:

```python homo.py -d olx.pl ```
```
sign: o, 0lx.com => 0lx.com [['69.172.201.208']], None
sign: o, ọlx.com => xn--lx-58s.com [['198.54.117.197', '198.54.117.198', '198.54.117.200', '198.54.117.199']], None
sign: l, oix.com => oix.com [['34.102.136.180']], None
sign: l, ołx.com => xn--ox-xqa.com [['78.108.180.224']], None

```

```python homo.py -d google.com -v ```


