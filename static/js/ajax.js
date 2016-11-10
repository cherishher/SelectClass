function ajax(){
	var req;
	
	if (window.XMLHttpRequest){
	  req = new XMLHttpRequest();
	}
	else{
	  req = new ActiveXObject("Microsoft.XMLHTTP");
	}
	
	return req;
}