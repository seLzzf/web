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

// 点赞
function give_praise(){
	var request=getHTTPObject();
	if (request) {
		request.open('GET',this.location.href+'give_praise',true);
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

// 收藏
function get_favorite(){
	var request=getHTTPObject();
	if (request) {
		request.open('GET',this.location.href+'get_favorite/',true);
		request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
		request.onreadystatechange=function(){
			if(request.readyState==4){
				var favorite_pic=document.getElementById('favorite');
				is_favo=favorite_pic.getAttribute('alt');
				if(is_favo=='is'){
					favorite_pic.setAttribute('src',"/static/images/favorite1.png");
					favorite_pic.setAttribute('alt',"is_not");
				}else{
					favorite_pic.setAttribute('src',"/static/images/favorite2.png");
					favorite_pic.setAttribute('alt',"is");
				};
				alert(request.responseText);
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
favorite=document.getElementById('favorite')
favorite.onclick=function(){
	get_favorite();
}

// 邮箱验证
$(function(){
	$('#send_email').click(function(){
		var email=$('#email_num').val();
		var btn=$('#send_email').attr('class','btn disabled');
		$.get('/users/register_confirm/',{'email':email},function(response){
			alert('发送成功');
		})
	});
});

