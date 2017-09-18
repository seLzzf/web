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

function give_praise(){
	var praise=document.getElementById('praise');
	praise.onclick=function(){
		praise.setAttribute('src',"/static/images/praise2.png");
	}
}

addLoadEvent(give_praise);
addLoadEvent(test);
