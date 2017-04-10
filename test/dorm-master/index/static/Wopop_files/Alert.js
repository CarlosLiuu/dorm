/**
 * Created by liu88 on 2017/4/11.
 */

var t;
var argl,funcf;
//获取指定ID的元素
function $xp(id) {
 return document.getElementById(id);
}
//通用事件获取接口
function getEvent()
{
 if(CheckBrowser()=='IE')  return window.event;
 func=getEvent.caller;
 while(func!=null)
 {
  var arg0 = func.arguments[0];
  if(arg0)
  {
   if((arg0.constructor==Event || arg0.constructor ==MouseEvent)
   || (typeof(arg0)=="object" && arg0.preventDefault && arg0.stopPropagation))
   {
    return arg0;
   }
  }
  func=func.caller;
 }
 return null;
}
//alert
function NewAlertBox(itype,msg,time){//time为消失时间
 var msgbg,msgcolor,bordercolor,content,posLeft,posTop,imgName;
 argl=arguments.length;
 if(argl>3)
 {funcf = arguments[3];}//外部方法
 //弹出窗口设置
 msgbg = "#FFF";   //内容背景
 msgcolor = "#f66f15";  //内容颜色
 bordercolor = "#d8bfd8";  //边框颜色
 //遮罩背景设置
 //判断图片类型
 if(itype.toUpperCase()=='OK') //提示通过
 	imgName = '../Img/ts_ok.png';
 else if(itype.toUpperCase()=='ERROR') //提示报错
     imgName = '../Img/ts_error.png';
 else //提示警告或者其他
     imgName = '../Img/ts_warning.png';

 content = "<img src='" + imgName + "' alt='img ' style='width:78px;height:78px;'/><br/>" + msg;
 var sWidth,sHeight;
 if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth)
	{
		sWidth = document.documentElement.clientWidth;
		sHeight = document.documentElement.clientHeight;
	}
	else
	{
		sWidth = screen.availWidth - 20;//防止溢出
		 if(screen.availHeight > document.body.scrollHeight){
		  sHeight = screen.availHeight; //少于一屏
		 }else{
		  sHeight = document.body.scrollHeight; //多于一屏
		 }
	}
 //创建遮罩背景
 var maskObj = document.createElement("div");
 maskObj.setAttribute('id','maskdiv');
 //maskObj.setAttribute('onclick','CloseMsg()');
 maskObj.style.position = "absolute";
 maskObj.style.top = "0";
 maskObj.style.left = "0";
 maskObj.style.background = "#fff";
 maskObj.style.filter = "Alpha(opacity=40);";
 maskObj.style.opacity = "0.4";
 maskObj.style.width = sWidth + "px";
 maskObj.style.height = sHeight + "px";
 maskObj.style.zIndex = "10000";
 document.body.appendChild(maskObj);
 //创建弹出窗口
 var msgObj = document.createElement("div")
 msgObj.setAttribute("id","msgdiv");
 msgObj.setAttribute("onClick","CloseMsg()");
 msgObj.style.position ="absolute";
 sWidth = 230;
 sHeight = 180;
 msgObj.style.width = sWidth + "px";
 //msgObj.style.height = sHeight + "px";
 var event = getEvent();//申明event
 if(CheckBrowser()=='IE')
 {
  //posLeft = event.clientX + 10;
  //posTop = event.clientY + document.documentElement.scrollTop;
  posLeft = (document.documentElement.clientWidth - sWidth) / 2 + "px";
  posTop = 50 + document.documentElement.scrollTop + "px";
  //posTop = (document.documentElement.clientHeight- sHeight) / 2 + "px";
 }
 else
 {
  //posLeft = event.pageX + 10 + "px";//ff下要申明px
  //posTop = event.pageY + 10 + "px";
  posLeft = (document.documentElement.clientWidth - sWidth) / 2 + "px";
  posTop = 50 + document.documentElement.scrollTop + "px";
  //posTop = (document.documentElement.clientHeight- sHeight) / 2 + "px";
 }
 msgObj.style.top = posTop;
 msgObj.style.left = posLeft;
 msgObj.style.fontSize = "18px";
 msgObj.style.background = msgbg;
 msgObj.style.border = "1px solid " + bordercolor;
 msgObj.style.zIndex = "10001";
 //创建内容
 var bodyObj = document.createElement("div");
 bodyObj.setAttribute("id","msgbody");
 bodyObj.style.padding = "10px";
 bodyObj.style.lineHeight = "1.5em";
 bodyObj.style.color = msgcolor;
 bodyObj.style.textAlign = "center";
 //var txt = document.createTextNode(content);
 //bodyObj.appendChild(txt);
 bodyObj.innerHTML = content;
 //生成窗口
 document.body.appendChild(msgObj);
 $xp("msgdiv").appendChild(bodyObj);
 if(time != '') t=setTimeout("CloseMsg()",time);
 else t=setTimeout("CloseMsg()",3000);//默认三秒后自动消失
 return false;
}
//移除对象
function CloseMsg(){
 $xp("msgdiv").removeChild($xp("msgbody"));
 document.body.removeChild($xp("msgdiv"));
 document.body.removeChild($xp("maskdiv"));
 clearTimeout(t);//停止计时器
 t = null;
 if(argl>3)
 {funcf();}//执行外部传入的函数
}
//判断浏览器类型
function CheckBrowser(){
    var cb = "Unknown";
    if(window.ActiveXObject){
        cb = "IE";
    }else if(navigator.userAgent.toLowerCase().indexOf("firefox") != -1){
        cb = "Firefox";
    }else if((typeof document.implementation != "undefined") && (typeof document.implementation.createDocument != "undefined") && (typeof HTMLDocument != "undefined")){
        cb = "Mozilla";
    }else if(navigator.userAgent.toLowerCase().indexOf("opera") != -1){
        cb = "Opera";
    }
    return cb;
}

