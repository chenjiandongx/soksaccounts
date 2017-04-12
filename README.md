# Shadowsocks账号爬虫
### 运行环境 
* Windows 10
* python 3.5.2  
* shadowsocks 4.0.2

### 爬虫介绍  
* 众所周知，免费的 shadowsocks 账号基本上是会不定时更换密码的，为了免去手动操作的过程，这个爬虫爬取了几个提供免费 shadowsocks 账号的网站，并自动生成配置文件，只需设置自己的 shadowsocks 安装目录便行  
* 由于爬取的账号网速未知，所以采用**高可用**策略

### 安装
1. git clone https://github.com/chenjiandongx/soksaccounts.git  
2. 将 main( ) 里面 path 配置成自己的 shadowsocks 的路径  
3. cd 到 soksaccounts 目录下  ```python setup.py install```

### 使用
1. 运行soks
```
C:\Users\54186>soks 
>>  Generate gui-config.json successful
``` 

2. 启动 shadowsocks ( 每次启动 soks 均要重启一次 shadowsocks，我也不知为什么它不会自动刷新数据 )


### 效果
* 毕竟是免费的，速度肯定没有那么稳定，不过有时 youtube 还是可以达到720P的  
 
  ![youtube测速](https://img.js.cn/images/2017/04/09/9461634def7e4924d2794f25eb19fc59.png)

#### 欢迎fork和star