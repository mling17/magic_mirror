# 魔镜
### 功能：
   1. - [x] 显示日期时间
   2. - [x] 显示农历和节日
   3. - [x] 显示城市实时天气情况
   4. - [x] 显示城市未来三天天气情况
   5. - [x] 检测并显示室内温湿度
   6. - [x] 显示待办事项
   7. - [x] 显示树莓派的运行情况，包括cpu温度、cpu使用量、内存使用量和剩余,存储使用量和剩余
   8. - [x] cpu达到一定温度自动开启风扇散热
   

### 硬件清单
- 树莓派4B
- TF存储卡
- Type-C电源线
- 散热风扇
- 显示屏,型号：微雪 7DP-CAPLCD不带外壳 内缩接口
- 显示器电源线
- Micro HDIMI线
- DHT11温湿度传感器
- 电源模块（两路USB接口5v输出）
- 12v3A适配器充电器
- NPN三极管S8550，用来控制风扇
- 移动硬盘（选配）
### 
## 使用要求

常规方式要求有 Python 环境、Redis 环境，具体要求如下：
### 系统环境
- 树莓派官方镜像：2019-2-1
- Python>=3.6
- Redis

## 

## 系统安装
运行一下命令：
``` shell script
git clone https://github.com/mling17/magic_mirror.git
cd magic_mirror
sudo ./install.sh
```
安装脚本会更新系统、安装redis、安装依赖包、配置开机自启动
### 环境变量配置
#### redis
本地安装 Redis、Docker 启动 Redis、远程 Redis 都是可以的，只要能正常连接使用即可。

首先可以需要一下环境变量，代理池会通过环境变量读取这些值。

设置 Redis 的环境变量有两种方式，一种是分别设置 host、port、password，另一种是设置连接字符串，设置方法分别如下：

设置 host、port、password，如果 password 为空可以设置为空字符串，示例如下：

```shell script
export MIRROR_REDIS_HOST='localhost'
export MIRROR_REDIS_PORT=6379
export MIRROR_REDIS_PASSWORD=''
export MIRROR_REDIS_DB=0
```

或者只设置连接字符串：

```shell script
export MIRROR_REDIS_CONNECTION_STRING='redis://localhost'
```

这里连接字符串的格式需要符合 `redis://[:password@]host[:port][/database]` 的格式，
中括号参数可以省略，port默认是6379，database默认是0，密码默认为空。

以上两种设置任选其一即可。

#### 配置web服务

```shell script
export API_HOST='0.0.0.0'
export API_THREADED=True
```

#### 配置所属城市

```shell script
export PI_LOCATION='潍坊'
```
## 启动魔镜


两种方式运行运行，自动运行和手动运行。

自动运行：树莓派开机时会自动启动。

手动运行，命令如下：

```shell script
python3 run.py
```

运行之后会启动 信息获取模块和信息展示模块，这时访问 [http://localhost:5555/](http://localhost:5555/) 即可。

## 可配置项

可以通过修改settings.py来配置一些参数。

### 开关

- ENABLE_PI：树莓派功能总开关（风扇、树莓派资源利用信息、温湿度传感器），默认 True
- ENABLE_WEATHER：允许 获取天气功能模块 启动，默认 True
- ENABLE_DHT11：允许 获取室内温湿度模块 启动，默认 True
- ENABLE_FAN：允许 风扇散热模块 启动，默认 True
- ENABLE_PI_INFO：允许 树莓派资源利用信息模块 启动，默认 True
- ENABLE_LUNAR：允许 获取农历信息模块 启动，默认 True
- ENABLE_SERVER：允许 web服务器模块 启动，默认 True


### 环境

- APP_ENV：运行环境，可以设置 dev、test、prod，即开发、测试、生产环境，默认 dev
- APP_DEBUG：调试模式，可以设置 true 或 false，默认 true
- APP_PROD_METHOD: 正式环境启动应用方式，默认是`gevent`，
  可选：`tornado`，`meinheld`（分别需要安装tornado或meinheld模块）

### Redis 连接


### 处理器

CYCLE_INFO: # 获取pi信息的频率,默认 10秒
CYCLE_DHT11: # 获取室内温湿度的频率,默认 1800秒
CYCLE_FAN:  # 风扇检测频率,默认 10秒
CYCLE_WEATHER: # 获取天气信息的频率,默认 1800秒
CYCLE_LUNAR: # 农历日期更新频率,默认 1秒

### 设置GPIO接口
GPIO_DHT11: # DHT11温湿度传感器引脚，默认BCM17
GPIO_FAN: # 风扇控制引脚，默认BCM26

## 待开发

- [ ] 室内温度持久化存储
- [ ] 前端展示历史上的今天、微博热搜、金句

如有一起开发的兴趣可以在 Issue 留言，非常感谢！
