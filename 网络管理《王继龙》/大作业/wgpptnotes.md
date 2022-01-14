## 图的描述

白色圆圈表示网络路径中的中间主机未被端口扫描。

绿色圆圈代表开放端口少于 3 个的端口。

网络距离显示为同心灰色环。 每增加一个环就意味着距离中心主机多一个网络跃点。

如果跃点没有 RTT（缺少 traceroute 条目），则连接以蓝色虚线显示，建立连接的未知主机以蓝色轮廓显示。

使用了traceroute测试

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20211221010219830.png" alt="image-20211221010219830" style="zoom: 67%;" />

202.112.38.69 ![image-20211221011923390](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20211221011923390.png)

219.224.103.38 ![image-20211221011731682](C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20211221011731682.png)

182.61.255.40 <img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20211221012013360.png" alt="image-20211221012013360" style="zoom:67%;" />

<img src="C:\Users\ligeo\AppData\Roaming\Typora\typora-user-images\image-20211221010619985.png" alt="image-20211221010619985" style="zoom:67%;" />

## 命令描述

```
-sn - 禁用端口扫描
-T4  -T<0-5>: 设置timing template(时序模板)（越高越快），提高质量和性能
-A - 启用操作系统检测、版本检测、脚本扫描和跟踪路由
-v - 增加详细程度 (print more information about the scan in progress )
```

