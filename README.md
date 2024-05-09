# StarryNift自动交互脚本



## 主要功能

- 邀请自动Mint
- 每日签到
- 每日抽奖
- 每日Quests任务（关注、在线浏览）
- 账号状态获取

## 使用方法

- 设置代理，推荐直接使用梯子自带的代理，比如我的HTTP代理开放在本地的10809端口，就需要在`/data/proxies.txt`中设置如下代理，注意每个账号对应一个代理，代理可重复。

![image-20240507104344725](https://typora-mine.oss-cn-beijing.aliyuncs.com/typoraimage-20240507104344725.png)

- 安装python环境，并下载该项目
- 安装依赖 `pip install -r requirements.txt `
- 填入私钥 `/data/private_keys.txt`
- 填入代理 `data/proxies.txt`(注意与私钥数量对应)
- 邀请设置 `/modules/setting.py`



## 其他说明

### 1、关于代理

经过实际测试，动态IP的流量消耗过大，推荐直接使用梯子自带的代理，比如我使用的V2ray，我的HTTP代理开放在本地的10809端口，就需要在/data/proxies.txt中设置如下代理

![image-20240507103612025](https://typora-mine.oss-cn-beijing.aliyuncs.com/typoraimage-20240507103612025.png)

### 2、关于CloudFlare验证码

原计划使用yescaptcha来处理CloudFlare验证码，但是实测CloudFlare验证码并没有进行严格的限制，不会造成太大的影响，因此暂不加入



### 3、原项目
修改自项目：https://github.com/3asyPe/starrynift-automation 在此致谢

<p align="center">
  <a href="https://twitter.com/gIt17bbyal4Hvop"> <img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/gIt17bbyal4Hvop">
</p>


