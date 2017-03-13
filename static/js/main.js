var flag = true;

function checkNum(){
    var re = /^(\d\d)[0-9A-Z]1(1|2|3|4|5|6)\d(\d\d)$/;
    if(re.test(document.getElementById("studentnum").value))
    	document.getElementById("msg").innerHTML = "";
    else{
    	document.getElementById("msg").innerHTML = "学号格式错误！";
    	flag = false;
    }
}

function checkPwd(){
  	var re = /^2131(1|2|3|4|5|6)\d\d\d\d$/;
    if(re.test(document.getElementById("cardnum").value))
    	document.getElementById("msg").innerHTML = "";
    else{
    	document.getElementById("msg").innerHTML = "一卡通号格式错误！";
    	flag = false;
    }
}

function checkPhone(){
	var re = /^1[3|5|7|8][0-9]\d{4,8}$/;
	if(re.test(document.getElementById("phonenum").value))
    	document.getElementById("msg").innerHTML = "";
    else{
    	document.getElementById("msg").innerHTML = "手机号格式错误！";
    	flag = false;
    }
}

function login(){

	//判断输入格式是否正确，正确则发送请求
	if (flag){
    $.post("./login",
    {
    	'studentnum':document.getElementById("studentnum").value,
		'cardnum':document.getElementById("cardnum").value,
		'college':document.getElementById("college").value,
		'phonenum':document.getElementById("phonenum").value
    },
        function(data){
        console.log(data);
        loginJSON(data.code,data.text);
    },'json');
	}

}

function loginJSON(code, text){
	//处理JSON
	if (code == 200){
	window.location.href="../list";
		//window.location.href = "http://127.0.0.1:8000/list";
	}
	else{
		alert("发生错误：" + code + "\n" + text);
	}
}

function select(){
	var timestamp = Date.parse(new Date());

	if (flag){
    $.post("./select",
    {
    	'classname':document.getElementById("courseName").innerText,
    	'selecttime':timestamp,
    	'handle':0
    },
        function(data){
        selectJSON(data.code,data.text);
    },'json');
	}
}

function selectJSON(code, text){
	//处理JSON
	if (code == 200){
		var sel = document.getElementById("sel");
		var dis = document.getElementById("dis");

		alert("选课成功！");
		history.go(0);
	}
	else{
		alert("发生错误：" + code + "\n" + text);
	}
}

function dissel(){
	var timestamp = Date.parse(new Date());

	if (flag){
    $.post("./select",
    {
    	'classname':document.getElementById("courseName").innerText,
    	'selecttime':timestamp,
    	'handle':1
    },
        function(data){
        disselJSON(data.code,data.text);
    },'json');
	}
}

function disselJSON(code, text){
	//处理JSON
	if (code == 200){
		var sel = document.getElementById("sel");
		var dis = document.getElementById("dis");

		alert("退课成功！");
		         history.go(0);
	}
	else{
		alert("发生错误：" + response.code + "\n" + response.text);
	}
}