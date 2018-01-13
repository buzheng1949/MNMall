### 创建项目
 - 打开命令行，进入到你需要想放项目的任意位置，执行django-admin startproject xxx(xxx是你的项目的名称)
  
  工程创建成功后会有以下的目录
  
  - manage.py 工程的管理脚本 可以用来用命令行开启应用  
  - urls.py 配置前端链接跳转
  - settings.py 设置数据库等等
  - 应用里面的views （先不讲）

### 创建应用

- python manage.py startapp MNMall 
- 添加应用名到settings.py的应用列表中INSTALLED_APPS


### 开启项目

- python manage.py runserver 9999 后面的9999是你要启动的这个项目的端口号 


### 请求示例

- 现在views里面写函数
- 在urls.py 配置url


### 数据通信
- 创建数据库
  - 创建数据库
  - 创建数据表
  
```
CREATE TABLE `mall_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8_bin NOT NULL comment "商品名称",
  `title` varchar(200) COLLATE utf8_bin NOT NULL comment "商品标题",
  `sales` varchar(200) COLLATE utf8_bin NOT NULL comment "商品销量",
  `price` varchar(200) COLLATE utf8_bin NOT NULL comment "商品价格",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
```
  
- 实现前端请求到后端的交互
 - 实现获取所有的商品信息
 - 实现获取复合条件的商品信息
 - 实现插入一条商品信息
 - 实现删除一条商品信息
