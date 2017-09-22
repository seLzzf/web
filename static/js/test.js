function addLoadEvent(func){
	var oldonload=window.onload;
	if(typeof window.onload!='function'){
		window.onload=func;
	}else{
		window.onload=function(){
			oldonload();
			func();
		}
	}
}

///////////////////////////////////////////////////

function getHTTPObject(){
	if (typeof XMLHttpRequest=='undefined') 
	XMLHttpRequest=function(){
		try {return new ActiveXObject('Msxml2.XMLHTTP.6.0');}
		catch(e){}
		try {return new ActiveXObject('Msxml2.XMLHTTP.3.0');}
		catch(e){}
		try {return new ActiveXObject('Msxml2.XMLHTTP');}
		catch(e){}
		return false;
	}
	return new XMLHttpRequest();
}

function give_praise(){
	var request=getHTTPObject();
	if (request) {
		request.open('GET',this.location.href,true);
		request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
		request.onreadystatechange=function(){
			if(request.readyState==4){
				var praise=document.getElementById('praise');
				var praise_pic=document.getElementById('praise_pic');
				praise.innerHTML='点赞数:'+request.responseText;
				praise_pic.setAttribute('src',"/static/images/praise2.png");
			}
		};
		request.send(null);
	}else{
		alert('你的浏览器不支持ajax');
	};
}

praise=document.getElementById('praise_pic')
praise.onclick=function(){
	give_praise();
}

