目前选用的AS：AS58539 China Telecom Changsha 

治域地址查询网站https://bgp.he.net/



Intro https://threatit.com/articles/masscan-mass-ip-port-scanner/

https://resources.infosecinstitute.com/topic/masscan-scan-internet-minutes/

https://captmeelo.com/pentest/2019/07/29/port-scanning.html

# Masscan 

使用SYN包检测技术

tcp 端口扫描器，异步传输SYN包

更适合扫描较大的网络

不等三次握手

## Downloading

```
sudo apt-get install masscan
```

## Example

```
masscan -p 53,8080 -oX top_ports.xml -Pn -n 0.0.0.0/0 --exclude 255.255.255.255 --rate 10000
```

`-p 53, 8080` ports that are being targted

`-oX top_ports.xml` output data to xml file

`-Pn` not pinging bc more time

`-n` not resolving dns names （no dns resolution)

`0.0.0.0/0` range being scanned

` --exclude 255.255.255.255` have to exclude at least one ip address

`--rate 100000` rate in kilo-packets per second, kpps (can go up to 10 million packets per second)

## How to Use

Single IP Port Scan / Multiport Scan  / Range 

```
masscan 111.225.208.0/24 -p53-80
```

Rate and Save to Output

```
masscan 111.225.208.0/24 -p53 --rate 10000 > result.txt
```

Configuration File

```
# Example Scan examplescan.conf
rate = 10000.00
output-format = txt
output-status = all
output-filename = result.txt
ports = 0-8080
range = 111.225.208.0-111.225.208.255
excludefile = exclude.txt

... 
masscan -c examplescan.conf
```

可以先使用masscan扫描开启的端口，再用nmap进行详细的扫描

和Nmap主要区别

- 必须指定目标的ports
- masscan速度快，但只能扫描端口
- 不允许用dns名字
- 性能可能因操作系统而异，linux最好
- 以高速率扫描大端口范围时，结果不准确

永久启用了这些功能

- `-n` no DNS resolution, process of translating ip address to domain name
- `-Pn` doesn't ping host first
- `-sS` does syn scan only (usually omitted when running as root), same as Nmap
- `-randomize-hosts` scans completely randomly, SYN scan is relatively unobtrusive and stealthy, since it never completes TCP connections. 

有python库https://github.com/MyKings/python-masscan































# Nmap

Foot-printing tool that gets more information about target, IP, website, etc

nmap better for scanning smaller network rangers, for example, /24 range, slower

## Downloading

```
sudo apt-get install nmap
```

- very noisy, easily detectable by firewall/scanner, have to learn how to scan undetected

## Example

```
nmap -v -A scanme.nmap.org
```

- `-v` version number
- `-A` aggressive scanning, enable OS detection, version detection, script scanning

```
scan -v -sn 192.168.0.0/16 10.0.0/8
```

- scan a range of IP addresses, perhaps an organization

## How to Use

Scan a network at 

```
nmap -v -F 192.168.31.124
...
Nmap scan report for 192.168.31.124
Host is up (0.019s latency).
Not shown: 93 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
515/tcp  open  printer
548/tcp  open  afp
5000/tcp open  upnp
```















Zenmap is just the GUI for Nmap

