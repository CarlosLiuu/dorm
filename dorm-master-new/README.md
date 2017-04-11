# 智能宿舍
通过433MHz模块进行控制单片机，最终通过网页进行显示
## 接收数据格式
信息类型 : 1 Byte (data[0])  
设备ID : 2 Byte (data[1:3])  
预留位（数据位、中继指示位等） : 3 Byte (data[3:6])  
节点位置指针位 : 1 Byte (data[6])  
路由表 : 5 Byte (data[7] ~ data[11])  
停止位（信息类型低四位取反） : 1 Byte (data[12])  
## 框架
[Django](https://www.djangoproject.com/)  
[Materialize](http://materializecss.com/)  
[pySerial](https://pythonhosted.org/pyserial/)  
[nginx](http://nginx.org/)  
[Supervisor](http://supervisord.org/)  
[uWSGI](https://uwsgi-docs.readthedocs.io)  
## TODO：
- [x] Materialize网页
- [x] 显示数据库
- [x] 数据格式V2.0
- [x] Django+nginx+uwsgi部署
- [x] 数据库删除指令
- [x] supervisor配置文件(uwsgi、nginx、serialrecv)
- [x] 打印日志
- [ ] 根据组网信息更新路由表
- [ ] 流程图
- [ ] 网站登录
- [ ] 设备ID与房间号绑定操作
- [ ] 查询相关房间号的信息
- [ ] 网页监视程序运行状态
- [ ] 网页图表显示温度等信息
- [ ] 网页发送下行指令
- [ ] 定时查询
- [ ] 移动端适配
- [ ] 微信接口
- [ ] 一键部署
