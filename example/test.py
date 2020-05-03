#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 21:20
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py.py
# @Desc    :

from web_extractor import NewsExtractor


def test(html):
    extractor = NewsExtractor()
    result = extractor.extract(html, with_body_html=True)
    print(result)


if __name__ == "__main__":
    html = ''' 


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!--publish_time:2020-04-15 09:25:08-->
<html xmlns="http://www.w3.org/1999/xhtml">
<link rel="stylesheet" type="text/css" href="//n2.sinaimg.cn/default/cf7470f9/20190830/cms_style.css?t=20200319" />
<head>
<style>
	body,button,input,select,textarea{font-size:12px !important;line-height:24px;}
</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta property="og:type" content="news" />
<meta property="og:title" content="60名火神山、雷神山医院建设者集体献血" />
<meta property="og:description" content="60名火神山、雷神山医院建设者集体献血" />
<meta property="og:url" content="http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7829167.shtml" />
<meta property="og:image" content="http://n.sinaimg.cn/hb/transform/266/w640h426/20200415/6bea-isehnnk4676563.jpg" />
<meta name="weibo: article:create_at" content="2020-04-15 07:47:06" />
<meta name="weibo: article:update_at" content="2020-04-15 09:25:06" />


<title>60名火神山、雷神山医院建设者集体献血_新浪湖北_新浪网</title>
<meta name="Keywords" content="雷神山医院,火神山医院,献血,建设者,新冠肺炎" />
<meta name="Description" content="60名火神山、雷神山医院建设者集体献血,“我要献400毫升！”“我也是，多献一点多做贡献！”4月14日，武汉中建光谷之星大楼前的“爱心献血车”旁，中建三局安装公司员工们在武汉血液中心工作人员的指导下排起了一条长队，纷纷“撸袖上阵”。" />
<meta name="tags" content="雷神山医院,火神山医院,献血,建设者,新冠肺炎" />

<link rel="stylesheet" type="text/css" href="http://n3.sinaimg.cn/jx/css/base.css?v=180807" />
	
<link rel="stylesheet" type="text/css" href="http://n3.sinaimg.cn/jx/css/news.css?v=20180919v3" />

<link rel="stylesheet" href="http://storage.fedev.sina.com.cn/components/floatBarRight/styles.css">
    <script type="text/javascript" src="http://n.sinaimg.cn/lib/core/core.js"></script>
    <script type="text/javascript" src="http://storage.fedev.sina.com.cn/components/common/common.js"></script>

    <script>
        var $SCOPE = {
            SINA_COMPONENTS: {}  //为模块化使用的对象
        };
    </script>
    <script type="text/javascript" charset="utf-8"
			src="http://static.bshare.cn/b/buttonLite.js#uuid=87843916-c2c4-45f1-ae61-c21c70f45df4"></script>
    <script type="text/javascript" src="http://i.sso.sina.com.cn/js/outlogin_layer.js"></script>
    <link rel="stylesheet" type="text/css" href="http://news.sina.com.cn/css/87/20140926/comment.3.css">
    <script type="text/javascript" src="http://news.sina.com.cn/js/87/20140926/comment.3.min.js"></script>
	
<style>
	.img_wrapper {clear: both;}
<!--
	/**/
#weibo_btn,#top_btn,#sina_survey_form span.r_submit{display:none;}
	/**/
#bdshare.line{height:24px!important; overflow:hidden!important;float:right !important;*float:none!important;font-size:14px !important;padding:0 !important;}
#bdshare.line span.bds_more{display:inline !important;padding:0 !important;float:none !important;font-family:"Microsoft YaHei","微软雅黑" !important;background-image:none !important;}

#bdshare.artic-share{display: none;}
#bdshare.artic-share span.bds_more, .bds_tools a{float:left;!important;}

#bdshare.artic-share .bds_tsina,
#bdshare.artic-share .bds_weimi,
#bdshare.artic-share .bds_weixin,
#bdshare.artic-share .bds_qzone,
#bdshare.artic-share .bds_renren,
#bdshare.artic-share span.bds_more{display:inline-block!important;width:32px!important;height:32px!important;margin-left:8px!important;;text-decoration:none !important;background:url(http://i0.sinaimg.cn/cj/dfz/dfz_news/bg.png) no-repeat!important;padding:0!important;}
#bdshare.artic-share .bds_tsina{background-position:0 -40px!important;}
#bdshare.artic-share .bds_tsina:hover{background-position:0 -80px!important;}
#bdshare.artic-share .bds_weimi{background-position:-40px -40px!important;}
#bdshare.artic-share .bds_weimi:hover{background-position:-40px -80px!important;}
#bdshare.artic-share .bds_weixin{background-position:-80px -40px!important;}
#bdshare.artic-share .bds_weixin:hover{background-position:-80px -80px!important;}
#bdshare.artic-share .bds_qzone{background-position:-120px -40px!important;}
#bdshare.artic-share .bds_qzone:hover{background-position:-120px -80px!important;}
#bdshare.artic-share .bds_renren{background-position:-160px -40px!important;}
#bdshare.artic-share .bds_renren:hover{background-position:-160px -80px!important;}
#bdshare.artic-share span.bds_more{background-position:-200px -40px!important;text-indent:-99em!important;}
#bdshare.artic-share span.bds_more:hover{background-position:-200px -80px!important; }

-->

</style>




<meta name="sudameta" content="dataid:comos:ircuyvh7829167" /></head>
		<!--//针对天津单独控制正文页左侧宽度为680 S-->
<style type='text/css'>
.con1{
	border-right: 1px solid #ebebeb;
    float: left;
    margin-bottom: -2000px;
    padding: 0 10px 2000px 0;
    width: 680px;
}


}

</style>
<!--//针对天津单独控制正文页左侧宽度为680 E-->
<body><!-- body code begin -->

<!-- SUDA_CODE_START --> 
<script type="text/javascript"> 
//<!--
(function(){var an="V=2.1.16";var ah=window,F=document,s=navigator,W=s.userAgent,ao=ah.screen,j=ah.location.href;var aD="https:"==ah.location.protocol?"https://s":"http://",ay="beacon.sina.com.cn";var N=aD+ay+"/a.gif?",z=aD+ay+"/g.gif?",R=aD+ay+"/f.gif?",ag=aD+ay+"/e.gif?",aB=aD+"beacon.sinauda.com/i.gif?";var aA=F.referrer.toLowerCase();var aa="SINAGLOBAL",Y="FSINAGLOBAL",H="Apache",P="ULV",l="SUP",aE="UOR",E="_s_acc",X="_s_tentry",n=false,az=false,B=(document.domain=="sina.com.cn")?true:false;var o=0;var aG=false,A=false;var al="";var m=16777215,Z=0,C,K=0;var r="",b="",a="";var M=[],S=[],I=[];var u=0;var v=0;var p="";var am=false;var w=false;function O(){var e=document.createElement("iframe");e.src=aD+ay+"/data.html?"+new Date().getTime();e.id="sudaDataFrame";e.style.height="0px";e.style.width="1px";e.style.overflow="hidden";e.frameborder="0";e.scrolling="no";document.getElementsByTagName("head")[0].appendChild(e)}function k(){var e=document.createElement("iframe");e.src=aD+ay+"/ckctl.html";e.id="ckctlFrame";e.style.height="0px";e.style.width="1px";e.style.overflow="hidden";e.frameborder="0";e.scrolling="no";document.getElementsByTagName("head")[0].appendChild(e)}function q(){var e=document.createElement("script");e.src=aD+ay+"/h.js";document.getElementsByTagName("head")[0].appendChild(e)}function h(aH,i){var D=F.getElementsByName(aH);var e=(i>0)?i:0;return(D.length>e)?D[e].content:""}function aF(){var aJ=F.getElementsByName("sudameta");var aR=[];for(var aO=0;aO<aJ.length;aO++){var aK=aJ[aO].content;if(aK){if(aK.indexOf(";")!=-1){var D=aK.split(";");for(var aH=0;aH<D.length;aH++){var aP=aw(D[aH]);if(!aP){continue}aR.push(aP)}}else{aR.push(aK)}}}var aM=F.getElementsByTagName("meta");for(var aO=0,aI=aM.length;aO<aI;aO++){var aN=aM[aO];if(aN.name=="tags"){aR.push("content_tags:"+encodeURI(aN.content))}}var aL=t("vjuids");aR.push("vjuids:"+aL);var e="";var aQ=j.indexOf("#");if(aQ!=-1){e=escape(j.substr(aQ+1));aR.push("hashtag:"+e)}return aR}function V(aK,D,aI,aH){if(aK==""){return""}aH=(aH=="")?"=":aH;D+=aH;var aJ=aK.indexOf(D);if(aJ<0){return""}aJ+=D.length;var i=aK.indexOf(aI,aJ);if(i<aJ){i=aK.length}return aK.substring(aJ,i)}function t(e){if(undefined==e||""==e){return""}return V(F.cookie,e,";","")}function at(aI,e,i,aH){if(e!=null){if((undefined==aH)||(null==aH)){aH="sina.com.cn"}if((undefined==i)||(null==i)||(""==i)){F.cookie=aI+"="+e+";domain="+aH+";path=/"}else{var D=new Date();var aJ=D.getTime();aJ=aJ+86400000*i;D.setTime(aJ);aJ=D.getTime();F.cookie=aI+"="+e+";domain="+aH+";expires="+D.toUTCString()+";path=/"}}}function f(D){try{var i=document.getElementById("sudaDataFrame").contentWindow.storage;return i.get(D)}catch(aH){return false}}function ar(D,aH){try{var i=document.getElementById("sudaDataFrame").contentWindow.storage;i.set(D,aH);return true}catch(aI){return false}}function L(){var aJ=15;var D=window.SUDA.etag;if(!B){return"-"}if(u==0){O();q()}if(D&&D!=undefined){w=true}ls_gid=f(aa);if(ls_gid===false||w==false){return false}else{am=true}if(ls_gid&&ls_gid.length>aJ){at(aa,ls_gid,3650);n=true;return ls_gid}else{if(D&&D.length>aJ){at(aa,D,3650);az=true}var i=0,aI=500;var aH=setInterval((function(){var e=t(aa);if(w){e=D}i+=1;if(i>3){clearInterval(aH)}if(e.length>aJ){clearInterval(aH);ar(aa,e)}}),aI);return w?D:t(aa)}}function U(e,aH,D){var i=e;if(i==null){return false}aH=aH||"click";if((typeof D).toLowerCase()!="function"){return}if(i.attachEvent){i.attachEvent("on"+aH,D)}else{if(i.addEventListener){i.addEventListener(aH,D,false)}else{i["on"+aH]=D}}return true}function af(){if(window.event!=null){return window.event}else{if(window.event){return window.event}var D=arguments.callee.caller;var i;var aH=0;while(D!=null&&aH<40){i=D.arguments[0];if(i&&(i.constructor==Event||i.constructor==MouseEvent||i.constructor==KeyboardEvent)){return i}aH++;D=D.caller}return i}}function g(i){i=i||af();if(!i.target){i.target=i.srcElement;i.pageX=i.x;i.pageY=i.y}if(typeof i.layerX=="undefined"){i.layerX=i.offsetX}if(typeof i.layerY=="undefined"){i.layerY=i.offsetY}return i}function aw(aH){if(typeof aH!=="string"){throw"trim need a string as parameter"}var e=aH.length;var D=0;var i=/(\u3000|\s|\t|\u00A0)/;while(D<e){if(!i.test(aH.charAt(D))){break}D+=1}while(e>D){if(!i.test(aH.charAt(e-1))){break}e-=1}return aH.slice(D,e)}function c(e){return Object.prototype.toString.call(e)==="[object Array]"}function J(aH,aL){var aN=aw(aH).split("&");var aM={};var D=function(i){if(aL){try{return decodeURIComponent(i)}catch(aP){return i}}else{return i}};for(var aJ=0,aK=aN.length;aJ<aK;aJ++){if(aN[aJ]){var aI=aN[aJ].split("=");var e=aI[0];var aO=aI[1];if(aI.length<2){aO=e;e="$nullName"}if(!aM[e]){aM[e]=D(aO)}else{if(c(aM[e])!=true){aM[e]=[aM[e]]}aM[e].push(D(aO))}}}return aM}function ac(D,aI){for(var aH=0,e=D.length;aH<e;aH++){aI(D[aH],aH)}}function ak(i){var e=new RegExp("^http(?:s)?://([^/]+)","im");if(i.match(e)){return i.match(e)[1].toString()}else{return""}}function aj(aO){try{var aL="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";var D="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=";var aQ=function(e){var aR="",aS=0;for(;aS<e.length;aS++){aR+="%"+aH(e[aS])}return decodeURIComponent(aR)};var aH=function(e){var i="0"+e.toString(16);return i.length<=2?i:i.substr(1)};var aP=function(aY,aV,aR){if(typeof(aY)=="string"){aY=aY.split("")}var aX=function(a7,a9){for(var a8=0;a8<a7.length;a8++){if(a7[a8]==a9){return a8}}return -1};var aS=[];var a6,a4,a1="";var a5,a3,a0,aZ="";if(aY.length%4!=0){}var e=/[^A-Za-z0-9\+\/\=]/g;var a2=aL.split("");if(aV=="urlsafe"){e=/[^A-Za-z0-9\-_\=]/g;a2=D.split("")}var aU=0;if(aV=="binnary"){a2=[];for(aU=0;aU<=64;aU++){a2[aU]=aU+128}}if(aV!="binnary"&&e.exec(aY.join(""))){return aR=="array"?[]:""}aU=0;do{a5=aX(a2,aY[aU++]);a3=aX(a2,aY[aU++]);a0=aX(a2,aY[aU++]);aZ=aX(a2,aY[aU++]);a6=(a5<<2)|(a3>>4);a4=((a3&15)<<4)|(a0>>2);a1=((a0&3)<<6)|aZ;aS.push(a6);if(a0!=64&&a0!=-1){aS.push(a4)}if(aZ!=64&&aZ!=-1){aS.push(a1)}a6=a4=a1="";a5=a3=a0=aZ=""}while(aU<aY.length);if(aR=="array"){return aS}var aW="",aT=0;for(;aT<aS.lenth;aT++){aW+=String.fromCharCode(aS[aT])}return aW};var aI=[];var aN=aO.substr(0,3);var aK=aO.substr(3);switch(aN){case"v01":for(var aJ=0;aJ<aK.length;aJ+=2){aI.push(parseInt(aK.substr(aJ,2),16))}return decodeURIComponent(aQ(aP(aI,"binnary","array")));break;case"v02":aI=aP(aK,"urlsafe","array");return aQ(aP(aI,"binnary","array"));break;default:return decodeURIComponent(aO)}}catch(aM){return""}}var ap={screenSize:function(){return(m&8388608==8388608)?ao.width+"x"+ao.height:""},colorDepth:function(){return(m&4194304==4194304)?ao.colorDepth:""},appCode:function(){return(m&2097152==2097152)?s.appCodeName:""},appName:function(){return(m&1048576==1048576)?((s.appName.indexOf("Microsoft Internet Explorer")>-1)?"MSIE":s.appName):""},cpu:function(){return(m&524288==524288)?(s.cpuClass||s.oscpu):""},platform:function(){return(m&262144==262144)?(s.platform):""},jsVer:function(){if(m&131072!=131072){return""}var aI,e,aK,D=1,aH=0,i=(s.appName.indexOf("Microsoft Internet Explorer")>-1)?"MSIE":s.appName,aJ=s.appVersion;if("MSIE"==i){e="MSIE";aI=aJ.indexOf(e);if(aI>=0){aK=window.parseInt(aJ.substring(aI+5));if(3<=aK){D=1.1;if(4<=aK){D=1.3}}}}else{if(("Netscape"==i)||("Opera"==i)||("Mozilla"==i)){D=1.3;e="Netscape6";aI=aJ.indexOf(e);if(aI>=0){D=1.5}}}return D},network:function(){if(m&65536!=65536){return""}var i="";i=(s.connection&&s.connection.type)?s.connection.type:i;try{F.body.addBehavior("#default#clientCaps");i=F.body.connectionType}catch(D){i="unkown"}return i},language:function(){return(m&32768==32768)?(s.systemLanguage||s.language):""},timezone:function(){return(m&16384==16384)?(new Date().getTimezoneOffset()/60):""},flashVer:function(){if(m&8192!=8192){return""}var aK=s.plugins,aH,aL,aN;if(aK&&aK.length){for(var aJ in aK){aL=aK[aJ];if(aL.description==null){continue}if(aH!=null){break}aN=aL.description.toLowerCase();if(aN.indexOf("flash")!=-1){aH=aL.version?parseInt(aL.version):aN.match(/\d+/);continue}}}else{if(window.ActiveXObject){for(var aI=10;aI>=2;aI--){try{var D=new ActiveXObject("ShockwaveFlash.ShockwaveFlash."+aI);if(D){aH=aI;break}}catch(aM){}}}else{if(W.indexOf("webtv/2.5")!=-1){aH=3}else{if(W.indexOf("webtv")!=-1){aH=2}}}}return aH},javaEnabled:function(){if(m&4096!=4096){return""}var D=s.plugins,i=s.javaEnabled(),aH,aI;if(i==true){return 1}if(D&&D.length){for(var e in D){aH=D[e];if(aH.description==null){continue}if(i!=null){break}aI=aH.description.toLowerCase();if(aI.indexOf("java plug-in")!=-1){i=parseInt(aH.version);continue}}}else{if(window.ActiveXObject){i=(new ActiveXObject("JavaWebStart.IsInstalled")!=null)}}return i?1:0}};var ad={pageId:function(i){var D=i||r,aK="-9999-0-0-1";if((undefined==D)||(""==D)){try{var aH=h("publishid");if(""!=aH){var aJ=aH.split(",");if(aJ.length>0){if(aJ.length>=3){aK="-9999-0-"+aJ[1]+"-"+aJ[2]}D=aJ[0]}}else{D="0"}}catch(aI){D="0"}D=D+aK}return D},sessionCount:function(){var e=t("_s_upa");if(e==""){e=0}return e},excuteCount:function(){return SUDA.sudaCount},referrer:function(){if(m&2048!=2048){return""}var e=/^[^\?&#]*.swf([\?#])?/;if((aA=="")||(aA.match(e))){var i=V(j,"ref","&","");if(i!=""){return escape(i)}}return escape(aA)},isHomepage:function(){if(m&1024!=1024){return""}var D="";try{F.body.addBehavior("#default#homePage");D=F.body.isHomePage(j)?"Y":"N"}catch(i){D="unkown"}return D},PGLS:function(){return(m&512==512)?h("stencil"):""},ZT:function(){if(m&256!=256){return""}var e=h("subjectid");e.replace(",",".");e.replace(";",",");return escape(e)},mediaType:function(){return(m&128==128)?h("mediaid"):""},domCount:function(){return(m&64==64)?F.getElementsByTagName("*").length:""},iframeCount:function(){return(m&32==32)?F.getElementsByTagName("iframe").length:""}};var av={visitorId:function(){var i=15;var e=t(aa);if(e.length>i&&u==0){return e}else{return}},fvisitorId:function(e){if(!e){var e=t(Y);return e}else{at(Y,e,3650)}},sessionId:function(){var e=t(H);if(""==e){var i=new Date();e=Math.random()*10000000000000+"."+i.getTime()}return e},flashCookie:function(e){if(e){}else{return p}},lastVisit:function(){var D=t(H);var aI=t(P);var aH=aI.split(":");var aJ="",i;if(aH.length>=6){if(D!=aH[4]){i=new Date();var e=new Date(window.parseInt(aH[0]));aH[1]=window.parseInt(aH[1])+1;if(i.getMonth()!=e.getMonth()){aH[2]=1}else{aH[2]=window.parseInt(aH[2])+1}if(((i.getTime()-e.getTime())/86400000)>=7){aH[3]=1}else{if(i.getDay()<e.getDay()){aH[3]=1}else{aH[3]=window.parseInt(aH[3])+1}}aJ=aH[0]+":"+aH[1]+":"+aH[2]+":"+aH[3];aH[5]=aH[0];aH[0]=i.getTime();at(P,aH[0]+":"+aH[1]+":"+aH[2]+":"+aH[3]+":"+D+":"+aH[5],360)}else{aJ=aH[5]+":"+aH[1]+":"+aH[2]+":"+aH[3]}}else{i=new Date();aJ=":1:1:1";at(P,i.getTime()+aJ+":"+D+":",360)}return aJ},userNick:function(){if(al!=""){return al}var D=unescape(t(l));if(D!=""){var i=V(D,"ag","&","");var e=V(D,"user","&","");var aH=V(D,"uid","&","");var aJ=V(D,"sex","&","");var aI=V(D,"dob","&","");al=i+":"+e+":"+aH+":"+aJ+":"+aI;return al}else{return""}},userOrigin:function(){if(m&4!=4){return""}var e=t(aE);var i=e.split(":");if(i.length>=2){return i[0]}else{return""}},advCount:function(){return(m&2==2)?t(E):""},setUOR:function(){var aL=t(aE),aP="",i="",aO="",aI="",aM=j.toLowerCase(),D=F.referrer.toLowerCase();var aQ=/[&|?]c=spr(_[A-Za-z0-9]{1,}){3,}/;var aK=new Date();if(aM.match(aQ)){aO=aM.match(aQ)[0]}else{if(D.match(aQ)){aO=D.match(aQ)[0]}}if(aO!=""){aO=aO.substr(3)+":"+aK.getTime()}if(aL==""){if(t(P)==""){aP=ak(D);i=ak(aM)}at(aE,aP+","+i+","+aO,365)}else{var aJ=0,aN=aL.split(",");if(aN.length>=1){aP=aN[0]}if(aN.length>=2){i=aN[1]}if(aN.length>=3){aI=aN[2]}if(aO!=""){aJ=1}else{var aH=aI.split(":");if(aH.length>=2){var e=new Date(window.parseInt(aH[1]));if(e.getTime()<(aK.getTime()-86400000*30)){aJ=1}}}if(aJ){at(aE,aP+","+i+","+aO,365)}}},setAEC:function(e){if(""==e){return}var i=t(E);if(i.indexOf(e+",")<0){i=i+e+","}at(E,i,7)},ssoInfo:function(){var D=unescape(aj(t("sso_info")));if(D!=""){if(D.indexOf("uid=")!=-1){var i=V(D,"uid","&","");return escape("uid:"+i)}else{var e=V(D,"u","&","");return escape("u:"+unescape(e))}}else{return""}},subp:function(){return t("SUBP")}};var ai={CI:function(){var e=["sz:"+ap.screenSize(),"dp:"+ap.colorDepth(),"ac:"+ap.appCode(),"an:"+ap.appName(),"cpu:"+ap.cpu(),"pf:"+ap.platform(),"jv:"+ap.jsVer(),"ct:"+ap.network(),"lg:"+ap.language(),"tz:"+ap.timezone(),"fv:"+ap.flashVer(),"ja:"+ap.javaEnabled()];return"CI="+e.join("|")},PI:function(e){var i=["pid:"+ad.pageId(e),"st:"+ad.sessionCount(),"et:"+ad.excuteCount(),"ref:"+ad.referrer(),"hp:"+ad.isHomepage(),"PGLS:"+ad.PGLS(),"ZT:"+ad.ZT(),"MT:"+ad.mediaType(),"keys:","dom:"+ad.domCount(),"ifr:"+ad.iframeCount()];return"PI="+i.join("|")},UI:function(){var e=["vid:"+av.visitorId(),"sid:"+av.sessionId(),"lv:"+av.lastVisit(),"un:"+av.userNick(),"uo:"+av.userOrigin(),"ae:"+av.advCount(),"lu:"+av.fvisitorId(),"si:"+av.ssoInfo(),"rs:"+(n?1:0),"dm:"+(B?1:0),"su:"+av.subp()];return"UI="+e.join("|")},EX:function(i,e){if(m&1!=1){return""}i=(null!=i)?i||"":b;e=(null!=e)?e||"":a;return"EX=ex1:"+i+"|ex2:"+e},MT:function(){return"MT="+aF().join("|")},V:function(){return an},R:function(){return"gUid_"+new Date().getTime()}};function ax(){var aK="-",aH=F.referrer.toLowerCase(),D=j.toLowerCase();if(""==t(X)){if(""!=aH){aK=ak(aH)}at(X,aK,"","weibo.com")}var aI=/weibo.com\/reg.php/;if(D.match(aI)){var aJ=V(unescape(D),"sharehost","&","");var i=V(unescape(D),"appkey","&","");if(""!=aJ){at(X,aJ,"","weibo.com")}at("appkey",i,"","weibo.com")}}function d(e,i){G(e,i)}function G(i,D){D=D||{};var e=new Image(),aH;if(D&&D.callback&&typeof D.callback=="function"){e.onload=function(){clearTimeout(aH);aH=null;D.callback(true)}}SUDA.img=e;e.src=i;aH=setTimeout(function(){if(D&&D.callback&&typeof D.callback=="function"){D.callback(false);e.onload=null}},D.timeout||2000)}function x(e,aH,D,aI){SUDA.sudaCount++;if(!av.visitorId()&&!L()){if(u<3){u++;setTimeout(x,500);return}}var i=N+[ai.V(),ai.CI(),ai.PI(e),ai.UI(),ai.MT(),ai.EX(aH,D),ai.R()].join("&");G(i,aI)}function y(e,D,i){if(aG||A){return}if(SUDA.sudaCount!=0){return}x(e,D,i)}function ab(e,aH){if((""==e)||(undefined==e)){return}av.setAEC(e);if(0==aH){return}var D="AcTrack||"+t(aa)+"||"+t(H)+"||"+av.userNick()+"||"+e+"||";var i=ag+D+"&gUid_"+new Date().getTime();d(i)}function aq(aI,e,i,aJ){aJ=aJ||{};if(!i){i=""}else{i=escape(i)}var aH="UATrack||"+t(aa)+"||"+t(H)+"||"+av.userNick()+"||"+aI+"||"+e+"||"+ad.referrer()+"||"+i+"||"+(aJ.realUrl||"")+"||"+(aJ.ext||"");var D=ag+aH+"&gUid_"+new Date().getTime();d(D,aJ)}function aC(aK){var i=g(aK);var aI=i.target;var aH="",aL="",D="";var aJ;if(aI!=null&&aI.getAttribute&&(!aI.getAttribute("suda-uatrack")&&!aI.getAttribute("suda-actrack")&&!aI.getAttribute("suda-data"))){while(aI!=null&&aI.getAttribute&&(!!aI.getAttribute("suda-uatrack")||!!aI.getAttribute("suda-actrack")||!!aI.getAttribute("suda-data"))==false){if(aI==F.body){return}aI=aI.parentNode}}if(aI==null||aI.getAttribute==null){return}aH=aI.getAttribute("suda-actrack")||"";aL=aI.getAttribute("suda-uatrack")||aI.getAttribute("suda-data")||"";sudaUrls=aI.getAttribute("suda-urls")||"";if(aL){aJ=J(aL);if(aI.tagName.toLowerCase()=="a"){D=aI.href}opts={};opts.ext=(aJ.ext||"");aJ.key&&SUDA.uaTrack&&SUDA.uaTrack(aJ.key,aJ.value||aJ.key,D,opts)}if(aH){aJ=J(aH);aJ.key&&SUDA.acTrack&&SUDA.acTrack(aJ.key,aJ.value||aJ.key)}}if(window.SUDA&&Object.prototype.toString.call(window.SUDA)==="[object Array]"){for(var Q=0,ae=SUDA.length;Q<ae;Q++){switch(SUDA[Q][0]){case"setGatherType":m=SUDA[Q][1];break;case"setGatherInfo":r=SUDA[Q][1]||r;b=SUDA[Q][2]||b;a=SUDA[Q][3]||a;break;case"setPerformance":Z=SUDA[Q][1];break;case"setPerformanceFilter":C=SUDA[Q][1];break;case"setPerformanceInterval":K=SUDA[Q][1]*1||0;K=isNaN(K)?0:K;break;case"setGatherMore":M.push(SUDA[Q].slice(1));break;case"acTrack":S.push(SUDA[Q].slice(1));break;case"uaTrack":I.push(SUDA[Q].slice(1));break}}}aG=(function(D,i){if(ah.top==ah){return false}else{try{if(F.body.clientHeight==0){return false}return((F.body.clientHeight>=D)&&(F.body.clientWidth>=i))?false:true}catch(aH){return true}}})(320,240);A=(function(){return false})();av.setUOR();var au=av.sessionId();window.SUDA=window.SUDA||[];SUDA.sudaCount=SUDA.sudaCount||0;SUDA.log=function(){x.apply(null,arguments)};SUDA.acTrack=function(){ab.apply(null,arguments)};SUDA.uaTrack=function(){aq.apply(null,arguments)};U(F.body,"click",aC);window.GB_SUDA=SUDA;GB_SUDA._S_pSt=function(){};GB_SUDA._S_acTrack=function(){ab.apply(null,arguments)};GB_SUDA._S_uaTrack=function(){aq.apply(null,arguments)};window._S_pSt=function(){};window._S_acTrack=function(){ab.apply(null,arguments)};window._S_uaTrack=function(){aq.apply(null,arguments)};window._S_PID_="";if(!window.SUDA.disableClickstream){y()}try{k()}catch(T){}})();
//-->
</script> 
<noScript> 
<div style='position:absolute;top:0;left:0;width:0;height:0;visibility:hidden'><img width=0 height=0 src='http://beacon.sina.com.cn/a.gif?noScript' border='0' alt='' /></div> 
</noScript> 
<!-- SUDA_CODE_END -->

<!-- SSO_GETCOOKIE_START -->
<script type="text/javascript">var sinaSSOManager=sinaSSOManager||{};sinaSSOManager.getSinaCookie=function(){function dc(u){if(u==undefined){return""}var decoded=decodeURIComponent(u);return decoded=="null"?"":decoded}function ps(str){var arr=str.split("&");var arrtmp;var arrResult={};for(var i=0;i<arr.length;i++){arrtmp=arr[i].split("=");arrResult[arrtmp[0]]=dc(arrtmp[1])}return arrResult}function gC(name){var Res=eval("/"+name+"=([^;]+)/").exec(document.cookie);return Res==null?null:Res[1]}var sup=dc(gC("SUP"));if(!sup){sup=dc(gC("SUR"))}if(!sup){return null}return ps(sup)};</script>
<!-- SSO_GETCOOKIE_END -->

<script type="text/javascript">new function(r,s,t){this.a=function(n,t,e){if(window.addEventListener){n.addEventListener(t,e,false);}else if(window.attachEvent){n.attachEvent("on"+t,e);}};this.b=function(f){var t=this;return function(){return f.apply(t,arguments);};};this.c=function(){var f=document.getElementsByTagName("form");for(var i=0;i<f.length;i++){var o=f[i].action;if(this.r.test(o)){f[i].action=o.replace(this.r,this.s);}}};this.r=r;this.s=s;this.d=setInterval(this.b(this.c),t);this.a(window,"load",this.b(function(){this.c();clearInterval(this.d);}));}(/http:\/\/www\.google\.c(om|n)\/search/, "http://keyword.sina.com.cn/searchword.php", 250);</script>
<!-- body code end -->

<div id="CCCFloatBarRight" class="CCC-float-bar-right">
</div>
	

<script>

    $SCOPE.SINA_COMPONENTS.floatBarRight = {
        // pageWidth: 1000,   //页面宽度
        "default": [
            {
                type: 'comment',   //预置功能类型设置 我要评论
                pageInfo: {
                    entry: 'news',
                    channel: 'hb',
                    newsid: 'comos-ircuyvh7829167',
                    video_url: '',
                    hideComment: false,    // 是否隐藏评论入口
                    hideCommentList: 0,    // 是否隐藏评论列表(0,1)
                    uid: '2049389352',     // 微博分享后面的@用户uid
                    docID: 'http://doc.sina.cn/?id=comos:ircuyvh7829167',  // 文章docid，用来检测是否已收藏
                    pagepubtime: '2016-05-13',
                    difDay: 180,
                    ADIDs: ["PublicRelation2", "PublicRelation3", "left_focus_ad", "PublicRelation6", "PublicRelation8", "pl_sideAd"],
                    weiboGroupID: ''       // 底部微博推荐，如果没有，不填即可
                }
            },
            {
                type: 'share',    //预置功能类型设置 分享文章
                title: '分享文案',
                summary: '分享摘要',
                pic: '分享图片地址'
            }
        ],

    };
</script>
<script type="text/javascript" src="http://storage.fedev.sina.com.cn/components/floatBarRight/floatBarRight.js"></script>	
<script type="text/javascript">
//config
DFZ = window.DFZ || {};
DFZ.CFG = {"site":"36712","appkey":"397818775","appid":157,"site_id":909,"channel":"hb","domain":"hb.sina.com.cn\/","site_name":"hb","site_cn_name":"\u6e56\u5317\u7ad9","site_province":"\u6b66\u6c49","site_province_pinyin":"wuhan","site_back_date":"2014-10-11","weibo_uid":"2049389352","bshare_uuid":"87843916-c2c4-45f1-ae61-c21c70f45df4","weibo_pic":"http:\/\/tp1.sinaimg.cn\/2049389352\/180\/5710058725\/0","erweima":"http:\/\/sc.sinaimg.cn\/sc_2013_v1.0\/other\/news_sbs_code.jpg","province":42,"city":1,"old_pid":1190,"news_rank":"http:\/\/hb.sina.com.cn\/iframe\/328\/2012\/0703\/1.html","news_rank_new":"http:\/\/top.news.sina.com.cn\/ws\/GetTopDataList.php?top_channel=other&top_type=day&top_cat=dfz_hb_news_suda&top_time=today&top_show_num=10&top_order=DESC","tttj_flag":"hb_tttj","ydph_flag":"hb_ydph","tptj_flag":"hb_tptj","sptj_flag":"hb_sptj","cnxh_flag":"hb_cnxh"};
//DFZ.CFG.newsid="comos-ircuyvh7829167";
DFZ.CFG.newsid="comos-ircuyvh7829167";
DFZ.CFG.docUrl = "http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7829167.shtml";
DFZ.CFG.docTitle = "60名火神山、雷神山医院建设者集体献血";
</script>
	<script src="http://www.sinaimg.cn/cj/dfz/js/base.js" type="text/javascript"></script>
<!--SSO-->

<script src="http://i.sso.sina.com.cn/js/ssologin.js" type="text/javascript"></script>
<script src="http://i.sso.sina.com.cn/js/sinaSSOManager.js" type="text/javascript"></script>
<script src="http://www.sinaimg.cn/cj/dfz2014/DFZ_Login.js"></script>
<!--SinaFlash-->
<script src="http://i1.sinaimg.cn/home/sinaflash.js" type="text/javascript"></script>
<!--Pagination-->
<script type="text/javascript" src="http://www.sinaimg.cn/cj/dfz/cms2012/js/pagination.js"></script>
<style>
	.finance-nav { background-color: #4D62B1; height: 50px; border-top-width: 3px; border-top-style: solid; border-top-color: #2C77DA; line-height: 50px; font-size: 16px; margin-bottom: 20px; width: 1000px; margin-right: auto; margin-left: auto; clear: both; }
.finance-nav .navitem { line-height: 50px; height: 50px; margin: 0px; padding: 0px; list-style-image: none; list-style-type: none; }
.finance-nav .navitem .cur { color: #FFFFFF; background-color: #2C77DA; }
.finance-nav .navitem li { float: left; color: #FFFFFF; border-right-width: 1px; border-right-style: solid; border-right-color: #5A7BB5; }
.finance-nav .navitem li a { color: #FFFFFF; text-decoration: none; display: block; padding-right: 15px; padding-left: 15px; transition: .2s ease-in;  }
.finance-nav .navitem li a:hover { color: #FFFFFF; text-decoration: none; display: block; padding-right: 15px; padding-left: 15px; background-color: #2C77DA; }
</style>	

<div class="top-nav-wrap">
    <div class="top-nav">
        <div class="in">
            <p class="fl">
				 
<a href="https://www.sina.com.cn/" class="sina-logo-top" target='_blank'></a>					<a href="http://www.sina.com.cn" target="_blank">新浪首页</a>

|	<a href="http://hb.sina.com.cn/" target="_blank">新浪湖北</a>

|	<a href="http://hb.sina.com.cn/news/" target="_blank">资讯</a>

|	<a href="http://hb.sina.com.cn/gy/" target="_blank">公益</a>

|	<a href="http://hb.sina.com.cn/ts/" target="_blank">投诉</a>

|	<a href="http://hb.sina.com.cn/city/" target="_blank">城市</a>

|	<a href="http://wuhan.51xiancheng.com/" target="_blank">鲜城</a>

|	<a href="http://hb.travel.sina.com.cn/" target="_blank">旅游</a>

|	<a href="http://hb.sina.com.cn/run/" target="_blank">跑步</a>

|	<a href="http://hb.sina.com.cn/weibo" target="_blank">同城</a>

|	<a href="http://hb.sina.com.cn/wdh/guide.html" target="_blank">站内导航</a>


            </p>
			<!--http://weiba.weibo.com/chengdu=>?修改为各站的地址-->
			<p class="fr" style="display:none"><a href="http://weiba.weibo.com/chengdu" target="_blank" class="acor i_nick"></a>|<a href="https://mail.sina.net/" target="_blank">邮箱</a>|<a href="javascript:;" class="i_logout">退出</a></p>
            <p class="fr" style="display:none"><a href="javascript:;" class="i_login">用户登录</a>|<a href="javascript:;" class="i_reg">注册</a></p>
        </div>
    </div>
</div>

	<!--ad01 start:PDPS000000042998-->
    <div class="wrap ad_01">
						<ins class="sinaads" data-ad-pdps="PDPS000000032780"></ins><script>(sinaads = window.sinaads || []).push({});</script>
	
	</div>
    <!--ad01 start-->

	<div id="header" class="wrap">
    <div class="fl">
		        <h2 class="sinalogo-nav hb-logo"><a href="http://hb.sina.com.cn">新浪湖北</a></h2>
		        <div class="bnav"><a href="http://hb.sina.com.cn" class="icon01">新浪湖北</a> > <a href="http://hb.sina.com.cn/news" class="bnav_child">新闻频道</a> > <a href="http://hb.sina.com.cn/news/b/list.shtml">武汉资讯</a> > 正文</div>
    </div>
</div>
<style>
	element.style {
    width: 26px;
    height: 13px;
    position: absolute;
    right: 10px;
    bottom: 1px;
    z-index: 99;
    background: url(//d2.sina.com.cn/litong/zhitou/sinaads/release/ad_logo_update_IAB.gif) no-repeat;
	</style>
	<div class="wrap">
		<div class="con" >
			<ins class="sinaads" data-ad-pdps="PDPS000000046536"></ins><script>(sinaads = window.sinaads || []).push({});</script>
			<script type="text/javascript">

//js异步加载管理 v1.1.0
eval(function(p,a,c,k,e,r){e=function(c){return(c<62?'':e(parseInt(c/62)))+((c=c%62)>35?String.fromCharCode(c+29):c.toString(36))};if('0'.replace(0,e)==0){while(c--)r[e(c)]=k[c];k=[function(e){return r[e]||e}];e=function(){return'[4-9abfgj-vx-zA-R]'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(9(){b w=g,d=document,u=\'1.1.0\',7={},j=0,cbkLen=0;5(w.k){5(w.k.u>=u){o};7=w.k.K();j=7.j};b addEvent=9(x,B,C){5(x.L){x.L("on"+B,C)}m{x.addEventListener(B,C,false)}};9 M(a,D,s){b l=d.createElement("script");l.type="text/javascript";5(s){l.s=s};l.N=l.y=9(){5(!g.E||g.E=="loaded"||g.E=="complete"){5(D){D()};l.N=l.y=null;l.parentNode.removeChild(l)}};l.src=a;b h=d.getElementsByTagName("head")[0];h.insertBefore(l,h.firstChild)};b v=9(4,a){g.4=4;g.a=a;g.6=[]};v.prototype={f:\'O\',y:9(){g.f=\'F\';b z=[];P(b i=0;i<g.6.j;i++){5(n g.6[i]==\'9\'){try{g.6[i]()}catch(e){z.A(e)}}};g.6=[];5(z.j!=0){throw z[0]}}};b k=9(q,t){b 8={};5(p.j==3){8.4=p[0];8.a=p[1];8.6=p[2]}m 5(n q===\'Q\'){8.a=q;5(n t===\'9\'){8.6=t}}m{8=q};b a=8.a||"",4=8.4||"",6=8.6||"",s=8.s||"";b r={4:4,k:9(q,t){b agms=p;b 8={};5(p.j==3){8.4=p[0];8.a=p[1];8.6=p[2]}m 5(n q===\'Q\'){8.a=q;5(n t===\'9\'){8.6=t}}m{8=q};5(!8.4){8.4=\'R\'+j;j++};b c=k({4:g.4,6:9(){k(8)}});c.4=8.4;o c}};5(4){5(!7[4]){5(!a){7[4]=G v(4);7[4].f=\'H\'}m{7[4]=G v(4,a)};j++}m 5(7[4].f==\'H\'&&a){7[4].f=\'O\'};5(8.f){7[4].f=8.f};5(7[4].f==\'I\'||7[4].f==\'H\'){5(n 6==\'9\'){7[4].6.A(6)};o r}m 5(7[4].f==\'F\'){5(n 6==\'9\'){6()};o r}}m{5(!a){o r};P(b J in 7){5(7[J].a==a){4=J;break}};5(!4){4=\'R\'+j;7[4]=G v(4,a);j++};r.4=4;5(7[4].f==\'I\'){5(n 6==\'9\'){7[4].6.A(6)};o r}m 5(7[4].f==\'F\'){5(n 6==\'9\'){6()};o r}};5(n 6==\'9\'){7[4].6.A(6)};M(a,9(){7[4].y()},s);7[4].f=\'I\';o r};w.k=k;w.k.u=u;w.k.K=9(){o 7}})();',[],54,'||||name|if|callback|data|cfg|function|url|var||||status|this|||length|jsLoader|scriptNode|else|typeof|return|arguments|op|chain|charset|fn|version|JsObj||obj|onload|errors|push|eventType|func|dispose|readyState|ok|new|waiting|loading|item|getData|attachEvent|getScript|onreadystatechange|init|for|string|noname'.split('|'),0,{}))

  
    //js地址
    var ARTICLE_JSS = {
		//jq:'http://i0.sinaimg.cn/dy/js/jquery/jquery-1.7.2.min.js',
		jq:'',
		sab:'http://n.sinaimg.cn/static/fashion/article/article_sab.js',
        sinalib:'http://news.sina.com.cn/js/87/20110714/205/sinalib.js',
        subshow:'http://i3.sinaimg.cn/ty/sinaui/subshow/subshow2012070701.min.js',
        weiboAll:'http://news.sina.com.cn/js/268/2011/1110/16/weibo-all.js',
        sdfigure:'http://n.sinaimg.cn/fashion/js/sdfigure_v2.js',
        hdfigure:'http://news.sina.com.cn/js/87/20121218/hdfigure_v2.js',
        sinflash:'http://i1.sinaimg.cn/home/sinaflash.js',
        weiboCard:'http://ent.sina.com.cn/js/20120914/weibocard.js',
        // guess:'http://ent.sina.com.cn/js/470/20130207/guess.pro.js',
        // guess:'http://tech.sina.com.cn/js/717/2013/0614/article.recommender.min.js',
        guess:'http://n.sinaimg.cn/fashion/js/article.recommender.min.js',
        // allcont:'http://ent.sina.com.cn/temp/js/470/20120922/allcontent.1.4.js',
        allcont:'http://fashion.sina.com.cn/js/4/20130912/icontent/allcontent_new.js',
        shareOnWeibo:'http://news.sina.com.cn/js/87/20111011/227/shareonweibo.js',
        slider : 'http://n.sinaimg.cn/static/fashion/article_css_common/article_icontent_slider.js',
        weiboCard2013:'http://tech.sina.com.cn/js/717/20131127/content/weibocard2013.js',
        wbUsersRec:'http://news.sina.com.cn/js/87/20140623/wbUsesRec.js'
    };


(function(){
if(navigator.userAgent.indexOf('MSIE') === -1){return};
var list = ["http://www.sinaimg.cn/home/sinaflash.js","http://d2.sina.com.cn/d1images/button/rotator.js","http://d1.sina.com.cn/litong/zhitou/sspnew.js","http://i.sso.sina.com.cn/js/ssologin.js","http://i.sso.sina.com.cn/js/outlogin_layer.js","http://tjs.sjs.sinajs.cn/open/api/js/wb.js","http://news.sina.com.cn/js/87/20110714/205/sinalib.js","http://ent.sina.com.cn/js/20120914/weibocard.js","http://static.bshare.cn/b/buttonLite.js#style=-1&uuid=b0c5503c-e613-4b0e-a152-49b35294dd08&pophcol=2&lang=zh","http://static.bshare.cn/b/bshareC0.js","http://static.bshare.cn/b/addons/bshareDrag.js?bp=sinaminiblog,qzone,qqmb,renren,kaixin001&text=","http://d3.sina.com.cn/iframe/14/2011/0301/zhongshizhengwenye.js","http://pfp.sina.com.cn/iframe/14/2011/0517/47zhongshiwangmeng.js","http://d2.sina.com.cn/d1images/button/rotator.js","http://pfp.sina.com.cn/js/17/2013/0620/fashion00_300x500.js","http://p.tanx.com/ex?i=mm_15890324_2192376_11153435","http://d5.sina.com.cn/litong/xianwei/taobao0827.js","http://pfpip.sina.com.cn/ip.js","http://pfp.sina.com.cn/pfpnew/info/res_1017.js","http://pfp.sina.com.cn/pfpnew/resstyle/resstyle_1017_20081023.js","http://www.sinaimg.cn/unipro/pub/suda_m_v629.js"];
for(var i=0;i<list.length;i++){(new Image()).src = list[i]}
})();

    //正文页面基本脚本
	//jsLoader(ARTICLE_JSS.sab);
	//jsLoader(ARTICLE_JSS.jq)
	jsLoader({url:ARTICLE_JSS.sab, 'charset':'GBK',callback:function(){
		(function($){
              $.dom.ready(function(){
                $.app.autoLogin();
                var autologinTimeOut = setInterval(function(){
                 $.app.autoLogin();
                },8*1000);
              });
          })(SAB);
	}})
    //余下全文
	//jsLoader({url:ARTICLE_JSS.allcont, charset:'GBK'});
</script>
<!--百度自动推送begin-->
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';        
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
<!--百度自动推送end-->
<div class="article-box" id="artibody">
     <div id="fixNav">
		 <ul class="nav-content">
<li ><a href="http://www.sina.com.cn" target="_blank">新浪首页</a></li>
		  		   <li ><a href="http://hb.sina.com.cn" target="_blank">新浪湖北</a></li>
		  		   <li ><a href="http://hb.sina.com.cn/news/" target="_blank">资讯</a></li>
		  		   <li ><a href="http://hb.sina.com.cn/news/b/list.html" target="_blank">武汉</a></li>
		  		   <li ><a href="http://hb.sina.com.cn/news/j/list.html" target="_blank">各地</a></li>
		  		   <li ><a href="http://hb.sina.com.cn/news/sh/list.html" target="_blank">社会</a></li>
		  		   <li  class='last'><a href="http://slide.hb.sina.com.cn/" target="_blank">图片</a></li>
		  
		</ul>
	</div>
    <div class="article-header clearfix">
		<!---->
		
		        <h1>60名火神山、雷神山医院建设者集体献血</h1>
		<p class="source-time"><span>2020-04-15&nbsp;07:47</span><span><span id="art_source">综合</span></span><span><a href="#" class="mcom_num_show">评论（<b class="mcom_num" data-comment="comos-ircuyvh7829167"></b>人参与）</a></span></p>
		
		<div class="share-sns">
            <div class="bshare-custom">
				
                <a title="分享到新浪微博" class="bshare-sinaminiblog"></a>
                <a title="分享到微信" class="bshare-weixin"></a>
                <a title="分享到QQ空间" class="bshare-qzone"></a>
                <a title="更多平台" class="bshare-more more-style-addthis"></a>
            <!--<span class="BSHARE_COUNT bshare-share-count">0</span>-->
            </div>
        </div>
        <div class="fontsize"><a href="javascript:;" class="cur" data-size="16">A<sup class="fz-small">-</sup></a><a href="javascript:;" data-size="18">A<sup class="fz-big">+</sup></a></div>
    </div>
    <div class="article-body main-body">
		<div id='share_pic' style='height:0;overflow:hidden;'>
			<img src='https://n.sinaimg.cn/default/79e952e2/20170602/QQTuPian20170602150120.png' />
		</div>
        
<script type="text/javascript">
window.sina_survey_config = {  //注释：调查组件样式引入
    surveyCss: true,               //调查问答样式true, false, http （不使用默认样式配置false或者不传此参数）
    resultCss: true,               //调查结果样式true, false, http （不使用默认样式配置false或者不传此参数）
    resultType: '_blank',          //跳转新页面查看结果, 第三方嵌套组件的不建议设置, 不设置则投完票后当前页会展示结果
    source: 'vote',                //通过来源设置图片宽高 sina(手浪), vote(默认)
    imgWidth: 100,                 //设置图片宽度(非必须, 不建议使用)
    callback: function(data){      //渲染成功和投票成功后的回调 data存在表明投票成功
        console.log(data);
    }
}
</script>





	<p>　　原标题：60名火神山、雷神山医院建设者集体献血</p>
<p>　　长江网4月14日讯&nbsp;“我要献400毫升！”“我也是，多献一点多做贡献！”4月14日，武汉中建光谷之星大楼前的“爱心献血车”旁，中建三局安装公司员工们在武汉血液中心工作人员的指导下排起了一条长队，纷纷“撸袖上阵”。</p>
<div class="img_wrapper"><img src="http://n.sinaimg.cn/hb/crawl/162/w550h412/20200415/ce51-isehnnk4675168.jpg" alt="" data-link=""><span class="img_descr"></span></div>
<div class="img_wrapper"><img src="http://n.sinaimg.cn/hb/crawl/117/w550h367/20200415/681f-isehnnk4675220.jpg" alt="“两山”建设者献热血。通讯员李颖 胥曌闻 陈慧峰供图" data-link=""><span class="img_descr">“两山”建设者献热血。通讯员李颖 胥曌闻 陈慧峰供图</span></div>
<p>　　据武汉血液中心招募科科长顾军介绍，武汉市非新冠肺炎病患的医疗救治工作正在逐步恢复正轨，门诊量、住院量均不断上升，白血病患者、产妇、肿瘤以及各类手术患者急需血液拯救生命。而在疫情防控期间，武汉采血量大幅度下降，临床用血面临极大压力，全市血液紧缺、血库告急。</p>
<div class="img_wrapper"><img src="http://n.sinaimg.cn/hb/crawl/162/w550h412/20200415/9675-isehnnk4675260.jpg" alt=""><span class="img_descr"></span></div>
<div class="img_wrapper"><img src="http://n.sinaimg.cn/hb/crawl/117/w550h367/20200415/44ce-isehnnk4675279.jpg" alt=""><span class="img_descr"></span></div>
<div class="img_wrapper"><img src="http://n.sinaimg.cn/hb/crawl/162/w550h412/20200415/9a1b-isehnnk4675310.jpg" alt="“两山”建设者献热血。通讯员李颖 胥曌闻 陈慧峰供图" data-link=""><span class="img_descr">“两山”建设者献热血。通讯员李颖 胥曌闻 陈慧峰供图</span></div>
<p>　　武汉市发出无偿献血、助力战疫的号召后，参建武汉火神山、雷神山医院的在汉央企中建三局安装公司相关负责人主动联系武汉血液中心，员工们积极响应，纷纷报名献血。截至4月14日下午，共有60名员工参与此次无偿献血，累计献血总量约12800毫升。这些员工中大多数是曾参与武汉火神山、雷神山医院的建设者，他们再次“撸袖上阵”。（记者韩玮 通讯员李颖 胥曌闻 陈慧峰）</p>
<p>　　来源：长江网</p>
		
		<style>
p.article-editor {
    float: right;
    margin-right: 50px;
    margin-top: 18px;
}

		</style>	
				
		<!--ad : PDPS000000043000-->
		
		<div class="article-video artice-pic">

			<ins class="sinaads" data-ad-pdps="PDPS000000032786"></ins><script>(sinaads = window.sinaads || []).push({});</script>
		

		</div>
		
		<!--正文页微信二维码 /判断开关s-->	
		<div class="news_weixin_ercode clear tc"><p><strong class='article_erweima_title'>			</strong></p> <div class="img_wrapper article_erweima"><img src="" class="ercodepic" width='258px' height='258px'></div></div>
			<!--正文页微信二维码 /判断开关e-->	
    </div>
    <div class="article-footer clear">
        <div class="fl" style="width:300px;height:40px; overflow:hidden;">
            <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare artic-share">
                <span class="fl">分享到：</span>
                <a href="javascript:;" class="bds_tsina" title="微博">&nbsp;</a>
                <!--<a href="javascript:;" class="bds_weixin" data-cmd="weixin" title="微信">&nbsp;</a>-->
                <a href="javascript:;" class="bds_qzone" title="qq空间">&nbsp;</a>
                <a href="javascript:;" class="bds_renren" title="人人">&nbsp;</a>
                <span class="bds_more"></span>
            </div>
        </div>
        <div class="fr article-tag">标签：<a href="http://search.sina.com.cn/?from=index_hotword&c=news&q=%C0%D7%C9%F1%C9%BD%D2%BD%D4%BA" target="_blank">雷神山医院</a><a href="http://search.sina.com.cn/?from=index_hotword&c=news&q=%BB%F0%C9%F1%C9%BD%D2%BD%D4%BA" target="_blank">火神山医院</a><a href="http://search.sina.com.cn/?from=index_hotword&c=news&q=%CF%D7%D1%AA" target="_blank">献血</a><a href="http://search.sina.com.cn/?from=index_hotword&c=news&q=%BD%A8%C9%E8%D5%DF" target="_blank">建设者</a><a href="http://search.sina.com.cn/?from=index_hotword&c=news&q=%D0%C2%B9%DA%B7%CE%D1%D7" target="_blank">新冠肺炎</a></div>
    </div>
</div>

			<div class="discuss-form"></div>
<!--评论 start-->
<script>var dfz_cmnt_stat = true;</script>
<!--评论 End-->

			
			
<h3 class="s-tit">猜你喜欢</h3>
<ul class="love-list">
	
    <li>
		<h2><a href="http://hb.sina.com.cn/news/j/2020-04-15/detail-iirczymi6373885.shtml?from=hb_cnxh" target="_blank">湖北新增新冠肺炎确诊病例0例 新增无症状感染者32例</a></h2>
        <p class="grey"><span class="fl">04-15 08:53</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-irczymi6373885"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/n/2020-04-15/detail-iirczymi6372441.shtml?from=hb_cnxh" target="_blank">31省份和新疆兵团新增确诊病例46例 10例为本土病例</a></h2>
        <p class="grey"><span class="fl">04-15 08:47</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-irczymi6372441"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/b/2020-04-15/detail-iirczymi6367951.shtml?from=hb_cnxh" target="_blank">武汉“重启”首周：城市在复苏 生活上正轨</a></h2>
        <p class="grey"><span class="fl">04-15 08:36</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-irczymi6367951"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/b/2020-04-15/detail-iirczymi6366092.shtml?from=hb_cnxh" target="_blank">武汉15日起发放2000万消费券 数百家超市百货可使用</a></h2>
        <p class="grey"><span class="fl">04-15 08:20</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-irczymi6366092"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/j/2020-04-15/detail-iircuyvh7832350.shtml?from=hb_cnxh" target="_blank">投桃报李 湖北应城向绥芬河市捐赠40万元抗疫物资</a></h2>
        <p class="grey"><span class="fl">04-15 08:09</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-ircuyvh7832350"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7830292.shtml?from=hb_cnxh" target="_blank">中欧班列(武汉)恢复常态化运营 首趟班列抵达德国</a></h2>
        <p class="grey"><span class="fl">04-15 07:55</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-ircuyvh7830292"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7830016.shtml?from=hb_cnxh" target="_blank">在汉研发的新冠疫苗开始临床试验 首批受试者已接种</a></h2>
        <p class="grey"><span class="fl">04-15 07:53</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-ircuyvh7830016"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7829169.shtml?from=hb_cnxh" target="_blank">武汉雷神山医院患者清零 最后4名危重症患者转院</a></h2>
        <p class="grey"><span class="fl">04-15 07:47</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-ircuyvh7829169"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7827536.shtml?from=hb_cnxh" target="_blank">武汉启动居民新冠病毒血清流行病学抽样调查</a></h2>
        <p class="grey"><span class="fl">04-15 07:30</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-ircuyvh7827536"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
    <li>
		<h2><a href="http://hb.sina.com.cn/news/n/2020-04-12/detail-iircuyvh7276917.shtml?from=hb_cnxh" target="_blank">援鄂护师张静静丈夫韩文涛回国 航班于今晨落地西安</a></h2>
        <p class="grey"><span class="fl">04-12 09:06</span><span class="fr"><a class="grey" href="#">评论(<b class="mcom_num" data-comment="comos-ircuyvh7276917"></b>)</a><i class="wline">|</i><span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare line"><span class="bds_more">分享</span></span></span></p>
    </li>
</ul>

			<!--ad Taobao start-->
			<div class="article-ad ad_07">
				<iframe width="640" height="350" frameborder="0" src="http://hb.sina.com.cn/iframe/76/2013/1029/288.html" marginwidth="0" marginheight="0" scrolling="no"></iframe>			</div>
            <!--ad Taobao end-->
      
		</div>
		<div class="side">
			<!--ad right 002 start : PDPS000000042999-->
			<div class="s-ad ad_02">

				<ins class="sinaads" data-ad-pdps="PDPS000000032782"></ins><script>(sinaads = window.sinaads || []).push({});</script>	
			</div>
            <!--ad right 002 end-->
			


<h3 class="s-tit">头条推荐</h3>
<ul class="ull2" id="ttList">
		<li><a href="http://hb.sina.com.cn/news/j/list.html" target="_blank">各地</a><i class="wline">|</i><a href="http://hb.sina.com.cn/news/j/2015-08-21/detail-ifxhcvsf1001011.shtml?from=hb_tttj" target="_blank">随州市纪委通报8起小官巨腐案例</a></li>
	<li><a href="http://hb.sina.com.cn/news/b/list.html" target="_blank">武汉</a><i class="wline">|</i><a href="http://hb.sina.com.cn/news/qy/2015-08-21/detail-ifxhcvry0766767.shtml?from=hb_tttj" target="_blank">武汉千台豪车亏本跑专车</a></li>
	<li><a href="http://hb.sina.com.cn/news/sh/list.html" target="_blank">社会</a><i class="wline">|</i><a href="http://hb.sina.com.cn/news/j/2015-08-21/detail-ifxhehqr6133599.shtml?from=hb_tttj" target="_blank">男子要求复婚遭拒绝刺杀前妻</a></li>
	<li><a href="http://wuhan.51xiancheng.com/" target="_blank">鲜城</a><i class="wline">|</i><a href="http://wuhan.51xiancheng.com/article/7433?from=hb_tttj" target="_blank">一口醇香的法式甜点派</a></li>
	<li><a href="http://wuhan.51xiancheng.com/" target="_blank">鲜城</a><i class="wline">|</i><a href="http://wuhan.51xiancheng.com/article/7435?from=hb_tttj" target="_blank">在小酒馆里品双塔下午茶</a></li>
	<li><a href="http://wuhan.51xiancheng.com/" target="_blank">鲜城</a><i class="wline">|</i><a href="http://wuhan.51xiancheng.com/article/7197?from=hb_tttj" target="_blank">楼中咖啡良心手作甜品</a></li>
	<li><a href="http://hb.travel.sina.com.cn/" target="_blank">旅游</a><i class="wline">|</i><a href="http://weibo.com/2049416014/CwFFYcxkt?from=hb_tttj" target="_blank">100元玩转武汉园博会</a></li>
	<li><a href="http://wh.auto.sina.com.cn/" target="_blank">汽车</a><i class="wline">|</i><a href="http://wh.auto.sina.com.cn/cshh/2015-08-21/detail-ifxhcvsc4234642.shtml?from=hb_tttj" target="_blank">车市增速放缓已成定局 </a></li>

</ul>

			<!--ad right 003 start : PDPS000000043001-->
			<div class="ad_03">
<ins class="sinaads" data-ad-pdps="PDPS000000040562"></ins><script>(sinaads = window.sinaads || []).push({});</script>
			</div>
            <!--ad right 003 end-->
						<div class="s-ad ad_04">
				<ul class="ad-tlist" style="height:auto;"><li><ins class="sinaads" data-ad-pdps="PDPS000000041071"></ins><script>(sinaads = window.sinaads || []).push({});</script>
					<ins class="sinaads" data-ad-pdps="PDPS000000041072"></ins><script>(sinaads = window.sinaads || []).push({});</script></li>
			
				</ul>
				</div>
						<!--ad right 004 end-->
			<div class="s-tit"></div>
			<ul class="w-tab" id="Tab01_Nav">
    <li class="cur"><a href="javascript:;">阅读排行</a></li>
    <li><a href="javascript:;">评论排行</a></li>
    <li><a href="javascript:;">微博热词</a></li>
</ul>

<style>
	#commentTop li{
	overflow: hidden;text-overflow: ellipsis;
	}
</style>
<div class="oll-box" id="Tab01_Block">
    <ol class="oll">
		<li><i class="i-num ii">1</i>
			<a href="http://hb.sina.com.cn/news/b/2020-04-14/detail-iirczymi6256717.shtml?from=hb_ydph" 		   title="武汉雷神山医院患者“清零” 即将关闭" target="_blank">武汉雷神山医院患者“清零” 即将关闭...</a></li><li><i class="i-num ii">2</i>
			<a href="http://hb.sina.com.cn/news/n/2020-04-14/detail-iirczymi6156077.shtml?from=hb_ydph" 		   title="全国新增新冠肺炎确诊病例89例 本土病例3例" target="_blank">全国新增新冠肺炎确诊病例89例 本土...</a></li><li><i class="i-num ii">3</i>
			<a href="http://hb.sina.com.cn/news/j/2020-04-14/detail-iirczymi6161988.shtml?from=hb_ydph" 		   title="湖北新增新冠肺炎确诊病例0例 新增无症状感染者22例" target="_blank">湖北新增新冠肺炎确诊病例0例 新增无...</a></li><li><i class="i-num ii">4</i>
			<a href="http://hb.sina.com.cn/news/b/2020-04-14/detail-iirczymi6149271.shtml?from=hb_ydph" 		   title="武汉无疫情小区占比98.1% 封控管理仍需全力以赴" target="_blank">武汉无疫情小区占比98.1% 封控管...</a></li><li><i class="i-num ii">5</i>
			<a href="http://hb.sina.com.cn/news/j/2015-07-16/detail-ifxfaswi4040937.shtml?from=hb_ydph" 		   title="襄阳坚强男孩工地搬砖挣学费 高考前爸爸突去世" target="_blank">襄阳坚强男孩工地搬砖挣学费 高考前爸...</a></li><li><i class="i-num ii">6</i>
			<a href="http://hb.sina.com.cn/news/j/2015-07-15/detail-ifxewxfu4197019.shtml?from=hb_ydph" 		   title="大冶上演真实版神雕侠侣 智障妻子走失18年回家" target="_blank">大冶上演真实版神雕侠侣 智障妻子走失...</a></li><li><i class="i-num ii">7</i>
			<a href="http://hb.sina.com.cn/news/j/2015-07-17/detail-ifxfccux2750139.shtml?from=hb_ydph" 		   title="襄阳男子烧烤摊上劝酒起冲突 回家拿刀捅伤两人" target="_blank">襄阳男子烧烤摊上劝酒起冲突 回家拿刀...</a></li><li><i class="i-num ii">8</i>
			<a href="http://hb.sina.com.cn/news/j/2015-07-16/detail-ifxfaswm0826844.shtml?from=hb_ydph" 		   title="安陆少年嫉妒朋友山地车太拉风将其偷走" target="_blank">安陆少年嫉妒朋友山地车太拉风将其偷走...</a></li><li><i class="i-num ii">9</i>
			<a href="http://hb.sina.com.cn/news/j/2015-07-15/detail-ifxewxfu4182972.shtml?from=hb_ydph" 		   title="港大狂揽22位高考状元 宜昌理科状元获47万奖学金" target="_blank">港大狂揽22位高考状元 宜昌理科状元...</a></li><li><i class="i-num ii">10</i>
			<a href="http://hb.sina.com.cn/news/b/2015-07-15/detail-ifxewnia9410755.shtml?from=hb_ydph" 		   title="武汉种菜哥炒股20年赚4套房 看淡涨跌耕种东湖边" target="_blank">武汉种菜哥炒股20年赚4套房 看淡涨...</a></li>        <!--?php echo $ph_str;?-->
    </ol>
    <ol class="oll" id="commentTop" style="display:none">
		
		    </ol>
    <ol class="oll" id="hotKey" style="display:none">
    
    </ol>
</div>
			<!--ad right 005 start : PDPS000000046543-->
			<div class="s-ad ad_05">

				<ins class="sinaads" data-ad-pdps="PDPS000000041077"></ins><script>(sinaads = window.sinaads || []).push({});</script></div>
            <!--ad right 005 end-->
			

<h3 class="s-tit"><a class="fr" href="http://slide.hb.sina.com.cn/" target="_blank">更多&gt;</a>图说湖北</h3>
<ul id="tsList" class="pic-list clear">
        <li><a href="http://hb.sina.com.cn/news/b/2015-04-20/detail-iavxeafs5851709.shtml?from=hb_tptj" target="_blank"><img src="http://n.sinaimg.cn/default/20150420/AjcQ-awzuney3864445.jpg" alt="武汉拟推水杉保护意见" /><span class="picl-tit"><em>武汉拟推水杉保护意见</em><i class="bg">&nbsp;</i></span></a></li>
            <li><a href="http://hb.sina.com.cn/news/j/2015-04-20/detail-iavxeafs5874795.shtml?from=hb_tptj" target="_blank"><img src="http://n.sinaimg.cn/default/20150420/CbsG-cczmvun9896596.jpg" alt="三峡库区再现裸体纤夫" /><span class="picl-tit"><em>三峡库区再现裸体纤夫</em><i class="bg">&nbsp;</i></span></a></li>
            <li><a href="http://hb.sina.com.cn/news/j/2015-04-20/detail-iavxeafs5855041.shtml?from=hb_tptj" target="_blank"><img src="http://n.sinaimg.cn/default/20150420/GJET-avxeafs5856043.jpg" alt="长江西陵峡岸边发现石林" /><span class="picl-tit"><em>长江西陵峡岸边发现石林</em><i class="bg">&nbsp;</i></span></a></li>
            <li><a href="http://hb.sina.com.cn/news/w/2015-04-20/detail-ichmifpy8879182.shtml?from=hb_tptj" target="_blank"><img src="http://n.sinaimg.cn/default/20150420/nJcd-avxeafs5856286.jpg" alt="武汉修长城高校现战斗机" /><span class="picl-tit"><em>武汉修长城高校现战斗机</em><i class="bg">&nbsp;</i></span></a></li>
    
</ul>

			<h3 class="s-tit"><a class="fr" href="http://hb.sina.com.cn/video/" target="_blank">更多&gt;</a>视频推荐</h3>
<ul class="pic-list video-list clear">
       	<li><a  href="http://hb.sina.com.cn/video/news/2015-04-13/090121428.html?from=" target="_blank"><img src="http://n.sinaimg.cn/default/20150413/Yx8P-chmifpy7473227.png" alt="女子被驾校教练潜规则 " /><span class="picl-tit"><em>女子被驾校教练潜规则 </em><i class="icon-video2">&nbsp;</i><i class="bg">&nbsp;</i></span></a></li>
        	<li><a  href="http://hb.sina.com.cn/video/news/2015-04-13/085921427.html?from=" target="_blank"><img src="http://n.sinaimg.cn/default/20150413/CzRo-cczmvun9190696.png" alt="男子被误当成野猪击毙" /><span class="picl-tit"><em>男子被误当成野猪击毙</em><i class="icon-video2">&nbsp;</i><i class="bg">&nbsp;</i></span></a></li>
        	<li><a  href="http://hb.sina.com.cn/video/news/2015-04-13/085721426.html?from=" target="_blank"><img src="http://n.sinaimg.cn/default/20150413/6yna-awzuney3217222.png" alt="全国道德模范变性后亮相" /><span class="picl-tit"><em>全国道德模范变性后亮相</em><i class="icon-video2">&nbsp;</i><i class="bg">&nbsp;</i></span></a></li>
        	<li><a  href="http://hb.sina.com.cn/video/news/2015-04-13/085621425.html?from=" target="_blank"><img src="http://n.sinaimg.cn/default/20150413/ONSK-cczmvun9190646.png" alt="中学生未让座被老人骂哭" /><span class="picl-tit"><em>中学生未让座被老人骂哭</em><i class="icon-video2">&nbsp;</i><i class="bg">&nbsp;</i></span></a></li>
    
</ul>

			<!--ad right 006 start-->
			<div class="s-ad ad_06"></div>
            <!--ad right 006 end-->
		</div>
	</div>
	
	<div class="share-layout">
    <a href="javascript:;" class="share-weibo">分享到微博</a>
    <!--<a href="javascript:;" class="share-erweima" style="position:relative;">二维码<span><img src="http://sc.sinaimg.cn/sc_2013_v1.0/other/news_sbs_code.jpg" /></span></a>-->
</div>
<!--Include JS-->
<script src="http://n.sinaimg.cn/jx/js/DFZ_Article_Union_min.js"></script>
<script src="http://n.sinaimg.cn/jx/js/atricle_common.js"></script>

		
<div id="footer-wrap" class="clear">
    <div class="footer-bg">
        <div class="site-link-wrap clear">
            <div class="look-back">
				<a href="http://hb.sina.com.cn/" class="logo-site hb-slogo" target="_blank">新浪湖北</a>
               
            </div>
            <dl class="site-link">
					<dt>品牌栏目</dt>
	<dd>
					<a href="http://hi.hb.sina.com.cn/hb/rzwh/rzwh.php" title="人在武汉" target=_blank>人在武汉</a>
			<a href="http://hi.hb.sina.com.cn/hb/zbkhb/zbkhb.php" title="直播看湖北" target=_blank>直播看湖北</a>
			<a href="http://hi.hb.sina.com.cn/hb/gbb/gbbns.php" title="隔壁班女生" target=_blank>隔壁班女生</a>
				</dd>
		<dt>微博矩阵</dt>
	<dd>
					<a href="http://weibo.com/weibohb" title="新浪湖北" target=_blank>新浪湖北</a>
			<a href="http://weibo.com/hbmeishi" title="湖北美食" target=_blank>湖北美食</a>
			<a href="http://weibo.com/hbtravel" title="湖北旅游" target=_blank>湖北旅游</a>
			<a href="http://weibo.com/hubeiauto" title="武汉汽车" target=_blank>武汉汽车</a>
			<a href="http://weibo.com/hbwenyu" title="人在武汉" target=_blank>人在武汉</a>
			<a href="http://weibo.com/wuhanba" title="鲜城武汉" target=_blank>鲜城武汉</a>
			<a href="http://weibo.com/u/6072764820" title="武汉同城" target=_blank>武汉同城</a>
			<a href="http://weibo.com/whdaren" title="武汉达人会" target=_blank>武汉达人会</a>
				</dd>
		<dt>合作伙伴</dt>
	<dd>
					<a href="http://wh.house.sina.com.cn/" title="武汉乐居" target=_blank>武汉乐居</a>
			<a href="http://www.cnhubei.com/" title="荆楚网" target=_blank>荆楚网</a>
			<a href="http://hb.china.com.cn/" title="中国网湖北" target=_blank>中国网湖北</a>
			<a href="http://www.hbtv.com.cn/" title="湖北网台" target=_blank>湖北网台</a>
			<a href="http://www.cjn.cn/" title="长江网" target=_blank>长江网</a>
			<a href="http://www.wesdom.me/" title="微思敦营销机构" target=_blank>微思敦营销机构</a>
			<a href="http://www.adbright.cn" title="AdBright广告" target=_blank>AdBright广告</a>
			<a href="http://www.appganhuo.com/" title="APP干货铺子" target=_blank>APP干货铺子</a>
			<a href="http://www.cnhan.com/" title="汉网" target=_blank>汉网</a>
			<a href="http://www.cnxianzai.com/" title="现在网" target=_blank>现在网</a>
			<a href="http://www.changjiangtimes.com/" title="长江商报网" target=_blank>长江商报网</a>
			<a href="http://www.whtv.com.cn/" title="黄鹤TV" target=_blank>黄鹤TV</a>
			<a href="http://www.cnchu.com/" title="荆州楚网" target=_blank>荆州楚网</a>
			<a href="http://www.jznews.com.cn/" title="荆州新闻网" target=_blank>荆州新闻网</a>
			<a href="http://www.10yan.com/" title="秦楚网" target=_blank>秦楚网</a>
			<a href="http://www.hsgd.net.cn/" title="黄石声屏网" target=_blank>黄石声屏网</a>
			<a href="http://www.cn3x.com.cn/" title="三峡宜昌网" target=_blank>三峡宜昌网</a>
			<a href="http://www.ichushang.com/" title="新楚商网" target=_blank>新楚商网</a>
			<a href="http://bbs.hbtv.com.cn/forum.php" title="楚汉论坛" target=_blank>楚汉论坛</a>
			<a href="http://hb.kankan.com/" title="看看湖北网" target=_blank>看看湖北网</a>
			<a href="http://www.chushang.gov.cn/" title="楚商网" target=_blank>楚商网</a>
			<a href="http://www.snjbs.com/" title="神农架新闻网" target=_blank>神农架新闻网</a>
			<a href="http://www.chinadzyl.com/" title="大众口腔" target=_blank>大众口腔</a>
			<a href="http://www.wuhannews.cn/" title="武汉网" target=_blank>武汉网</a>
				</dd>
		<dt class="flink-tit">新浪地方站</dt>
	<dd class="friend-link clear">
					<a href="http://city.sina.com.cn" target="_blank">新浪城市</a>
		<i>|</i>			<a href="http://henan.sina.com.cn" target="_blank">新浪河南</a>
		<i>|</i>			<a href="http://sh.sina.com.cn" target="_blank">新浪上海</a>
		<i>|</i>			<a href="http://tj.sina.com.cn" target="_blank">新浪天津</a>
		<i>|</i>			<a href="http://gd.sina.com.cn" target="_blank">新浪广东</a>
		<i>|</i>			<a href="http://sc.sina.com.cn" target="_blank">新浪四川</a>
		<i>|</i>			<a href="http://fj.sina.com.cn" target="_blank">新浪福建</a>
		<br/>			<a href="http://mn.sina.com.cn" target="_blank">新浪闽南</a>
		<i>|</i>			<a href="http://zj.sina.com.cn" target="_blank">新浪浙江</a>
		<i>|</i>			<a href="http://hb.sina.com.cn" target="_blank">新浪湖北</a>
		<i>|</i>			<a href="http://hunan.sina.com.cn" target="_blank">新浪湖南</a>
		<i>|</i>			<a href="http://ln.sina.com.cn" target="_blank">新浪辽宁</a>
		<i>|</i>			<a href="http://cq.sina.com.cn" target="_blank">新浪重庆</a>
		<i>|</i>			<a href="http://hebei.sina.com.cn" target="_blank">新浪河北</a>
		<br/>			<a href="http://sx.sina.com.cn" target="_blank">新浪陕西</a>
		<i>|</i>			<a href="http://ah.sina.com.cn" target="_blank">新浪安徽</a>
		<i>|</i>			<a href="http://jiangsu.sina.com.cn" target="_blank">新浪江苏</a>
		<i>|</i>			<a href="http://hlj.sina.com.cn/" target="_blank">新浪黑龙江</a>
		<i>|</i>			<a href="http://jl.sina.com.cn/" target="_blank">新浪吉林</a>
		<i>|</i>			<a href="http://jx.sina.com.cn" target="_blank">新浪江西</a>
		<i>|</i>			<a href="http://hainan.sina.com.cn" target="_blank">新浪海南</a>
		<br/>			<a href="http://sd.sina.com.cn" target="_blank">新浪山东</a>
		<i>|</i>			<a href="http://gx.sina.com.cn" target="_blank">新浪广西</a>
		<i>|</i>			<a href="http://qd.sina.com.cn" target="_blank">新浪青岛</a>
		<i>|</i>			<a href="http://nb.sina.com.cn" target="_blank">新浪宁波</a>
		<i>|</i>			<a href="http://sz.sina.com.cn/" target="_blank">新浪苏州</a>
		<i>|</i>			<a href="http://wx.sina.com.cn" target="_blank">新浪无锡</a>
		<i>|</i>			<a href="http://shenzhen.sina.com.cn" target="_blank">新浪深圳</a>
		<br/>			<a href="http://dl.sina.com.cn/" target="_blank">新浪大连</a>
		<i>|</i>			<a href="http://gz.sina.com.cn" target="_blank">新浪贵州</a>
		<i>|</i>			<a href="http://yn.sina.com.cn/" target="_blank">新浪云南</a>
		<i>|</i>			<a href="http://nmg.sina.com.cn/" target="_blank">新浪内蒙古</a>
		<i>|</i>			<a href="http://shanxi.sina.com.cn/" target="_blank">新浪山西</a>
		<i>|</i>			<a href="http://xj.sina.com.cn" target="_blank">新浪新疆</a>
		<br/>		</dd>

            </dl>
        </div>
        <div class="footer">
            <p id='fri_link'>
                			<a href="http://corp.sina.com.cn/chn/sina_index.html" target="_blank">新浪简介</a>
		|			<a href="http://hb.sina.com.cn/emarketing/about.html" target="_blank">新浪湖北简介</a>
		|			<a href="http://hb.sina.com.cn/zt/guest.html" target="_blank">意见反馈</a>
		|			<a href="http://hb.sina.com.cn/sales/" target="_blank">营销服务</a>
		|			<a href="http://hb.sina.com.cn/about/sinahb_lxwm.html" target="_blank">联系我们</a>
		|			<a href="http://hb.sina.com.cn/zt/zhaopin/" target="_blank">诚聘英才</a>
		|			<a href="http://corp.sina.com.cn/lawfirm/sina.htm" target="_blank">网站律师</a>
		|			<a href="http://english.sina.com/" target="_blank">SINA English</a>
		|			<a href="http://weibo.com/signup/signup.php" target="_blank">微博注册</a>
		|			<a href="http://help.sina.com.cn/" target="_blank">产品答疑</a>
		|			<a href="http://report.12377.cn:13225/toreportinputNormal_anis.do" target="_blank">有害信息举报</a>
			
            </p>
            <p>Copyright &copy; 1996 - 2020 SINA Corporation, All Rights Reserved</p>
            <p>新浪公司版权所有</p>
        </div>
    </div>
</div>
<script src="http://n.sinaimg.cn/dfz/news/js/DFZ_BackSite_min.js"></script>
<script>
$(function(){
	//首页回顾
	DFZ.UNION.SiteBack({
		channelName :	'hb',
		folderName	:	'/head/',
		page_pre	:	'hb',
		startDate	:	new Date('2014','10','11')
		});
	});
</script>
	<script type="text/javascript">
//config
DFZ = window.DFZ || {};
DFZ.CFG = {"site":"36712","appkey":"397818775","appid":157,"site_id":909,"channel":"hb","domain":"hb.sina.com.cn\/","site_name":"hb","site_cn_name":"\u6e56\u5317\u7ad9","site_province":"\u6b66\u6c49","site_province_pinyin":"wuhan","site_back_date":"2014-10-11","weibo_uid":"2049389352","bshare_uuid":"87843916-c2c4-45f1-ae61-c21c70f45df4","weibo_pic":"http:\/\/tp1.sinaimg.cn\/2049389352\/180\/5710058725\/0","erweima":"http:\/\/sc.sinaimg.cn\/sc_2013_v1.0\/other\/news_sbs_code.jpg","province":42,"city":1,"old_pid":1190,"news_rank":"http:\/\/hb.sina.com.cn\/iframe\/328\/2012\/0703\/1.html","news_rank_new":"http:\/\/top.news.sina.com.cn\/ws\/GetTopDataList.php?top_channel=other&top_type=day&top_cat=dfz_hb_news_suda&top_time=today&top_show_num=10&top_order=DESC","tttj_flag":"hb_tttj","ydph_flag":"hb_ydph","tptj_flag":"hb_tptj","sptj_flag":"hb_sptj","cnxh_flag":"hb_cnxh"};
//DFZ.CFG.newsid="comos-ircuyvh7829167";
DFZ.CFG.newsid="comos-ircuyvh7829167";
DFZ.CFG.docUrl = "http://hb.sina.com.cn/news/b/2020-04-15/detail-iircuyvh7829167.shtml";
DFZ.CFG.docTitle = "60名火神山、雷神山医院建设者集体献血";
</script>

	<script type="text/javascript" src="http://n.sinaimg.cn/default/79e952e2/20180109/dfz_article.js?v=10"></script>
<!-- Bshare button begin -->
<script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/buttonLite.js#style=-1&amp;uuid=87843916-c2c4-45f1-ae61-c21c70f45df4&amp;pophcol=2&amp;lang=zh"></script>
            <script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/bshareC0.js"></script>
<!--Bshare button end -->
<!-- Baidu Button BEGIN -->
<script type="text/javascript" id="bdshare_js" data="type=tools" ></script> 
<script type="text/javascript" id="bdshell_js"></script> 
<script type="text/javascript">
/*(function(exports){
  exports.bds_config = {
      // appkey
      "snsKey": {
          'tsina': '3840460260',
          'tqq': '',
          't163': '',
          'tsohu': ''
      },
      // @weibo id
	  'wbUid':'2049389352',
      'searchPic':false
  };
  document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000);
})(window);*/
</script>
<!-- Baidu Button END -->
<!--js异步加载  start-->	
		<script>
(function(){
	//动态更新顶部导航、右侧头条、图说、视频、底部link
	$.ajax({
		url:'http://interface.sina.cn/dfz/hb/news/js_all.d.html',
		data : {flag:'is_article'},
		dataType:'jsonp',
		success:function(json){
			if(!json||!json.result||!json.result.data) return;
			var data = json.result.data;
			if(data.top_html){
				//topnav
				$('.top-nav>.in>.fl').html(data.top_html);
			};
			if(data.top_neibu_html){
				//topnav_neibu
				$('.nav-content').html(data.top_neibu_html);
			};
			if(data.right_tttj_html){
				//toutiao
				$('#ttList').html(data.right_tttj_html);
			};
			if(data.right_tushuo_html){
				//tushuo
				$('#tsList').html(data.right_tushuo_html);
			};
			if(data.right_video_html){
				//shipin
				$('.video-list').html(data.right_video_html);
			};
			if(data.foot_link_html){
				//footlink
				$('.site-link').html(data.foot_link_html);
			};
			if(data.fri_link_html){
				//fri_link
				$('#fri_link').html(data.fri_link_html);
			};
			
		}
	});
	
//正文页微信二维码开关判断 s
		//正文页微信二维码js s
	$.ajax({
		url:'http://interface.sina.cn/dfz/outside/news/erweima.d.html',
		data : {cid:36712},
		dataType:'jsonp',
		success:function(json){
			if(!json||!json.result||!json.result.data || json.result.data.article_erweima_html=='' || json.result.data.article_erweima_title_html==''){ 
				$('.news_weixin_ercode').hide();return;}	
			//return;
			var data = json.result.data;
			if(data.article_erweima_html){
				//正文页微信二维码图片
				$('.article_erweima img').attr('src',data.article_erweima_html);
			};
			if(data.article_erweima_title_html){
				//正文页微信二维码标题
				$('.article_erweima_title').html(data.article_erweima_title_html);
			};
		}
	})

	//正文页微信二维码js e
		//正文页微信二维码开关判断 e
})();
	
	

	
</script>
		
<script>
	//判断面包线和域名一致
$(function() {
  var loc_host = window.location.host.split('.')[0];
  if (loc_host == 'nx' || loc_host == 'gs' || loc_host == 'gz' || loc_host == 'yn' || loc_host == 'nmg') {

    if (window.location.pathname.split('/')[1] != $('.bnav_child').eq(0).attr('href').split('/')[3]) {

      if (window.location.pathname.split('/')[1] == 'edu') {
        console.log('面包线与域名不一致');
        $('.bnav_child').eq(0).html('教育频道');
        if (loc_host == 'nx') {
          $('.bnav_child').eq(0).attr('href', '/edu/list.shtml');
        } else {
          $('.bnav_child').eq(0).attr('href', '/edu');
        }

      } else if (window.location.pathname.split('/')[1] == 'finance') {
        console.log('面包线与域名不一致');
        $('.bnav_child').eq(0).html('财经频道');
        $('.bnav_child').eq(0).attr('href', '/finance');
      } else if (window.location.pathname.split('/')[1] == 'health') {
        console.log('面包线与域名不一致');
        $('.bnav_child').eq(0).html('健康频道');
        $('.bnav_child').eq(0).attr('href', '/health');
      } else if (window.location.pathname.split('/')[1] == 'ypin') {
        console.log('面包线与域名不一致');
        $('.bnav_child').eq(0).html('云品');
        $('.bnav_child').eq(0).attr('href', '/ypin');
      }
    }
  }
})
	</script>
	<!--js异步加载  end-->
<!—$$ 20140808 SAX BASE $-->
<ins class="sinaads" data-ad-pdps="fill-with-pdps"></ins>
<script>
    (function (d, s, id) {
        var s, n = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        s = d.createElement(s);
        s.id = id;
        s.setAttribute('charset', 'utf-8');
        s.src = '//d' + Math.floor(0 + Math.random() * (9 - 0 + 1)) + '.sina.com.cn/litong/zhitou/sinaads/release/sinaads.js';
        n.parentNode.insertBefore(s, n);
    })(document, 'script', 'sinaads-script');
    (sinaads = window.sinaads || []).push({});
</script>
	<!--地方站富媒体加载-->
	<!--淘宝 begin-->
<script src="http://hb.sina.com.cn/iframe/new_common.js"></script>
<script language="javascript">
$(function(){                                
    var oNewP = $('<div class="s-ad ad_taobao"><iframe width="300" height="250" frameborder="0" src="http://hb.sina.com.cn/iframe/76/2014/0922/348.html" marginwidth="0" marginheight="0" scrolling="no"></iframe></div>');
    oNewP.insertAfter("#Tab01_Block");
	
	
});
</script>


<style>
/** 右侧浮标 **/
.backToTop {width:100px; height:100px; position:fixed;z-index:99; left:10px;top:10px;  position: fixed; _position: absolute; _bottom: "auto"; display:none}

</style>
<a href="http://xy10086.tmall.com/index.htm?spm=a1z10.3.w5002-8798857201.2.6neqhK" target="_blank" class="backToTop" id="xyfb"> <img src="http://n.sinaimg.cn/default/xy100100b.jpg" width="100" height="100" /></a>  

<!--淘宝 end-->


<script type="text/javascript" src="http://dm.city.sina.com.cn/js/crawl.js" charset="utf-8"></script>
<script src="https://pluto.sina.cn/gk/match?id=1"></script></body>
</html>
 '''
    test(html=html)

