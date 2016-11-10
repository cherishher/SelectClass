function checkNum(){
    var re = /^(\d\d)[0-9A-Z]1(4|5)\d(\d\d)$/;
    document.getElementById("msg").innerHTML = 
    	re.test(document.getElementById("studentnum").value)?"":"学号格式错误！";
}

function checkPwd(){
  	var re = /^2131(2|3|4|5|6)\d\d\d\d$/;
    document.getElementById("msg").innerHTML = 
    	re.test(document.getElementById("cardnum").value)?"":"一卡通号格式错误！";
}

function checkPhone(){
	var re = /^1[3|5|7|8][0-9]\d{4,8}$/;
	document.getElementById("msg").innerHTML = 
		re.test(document.getElementById("phonenum").value)?"":"手机号格式错误！";
}

function login(){
	var req = ajax();
//	var data = "studentnum=" + document.getElementById("studentnum").value + "&cardnum=" + document.getElementById("cardnum").value
//	 + "&college=" + document.getElementById("college") + "&phonenum=" + document.getElementById("phonenum");

//	var mydata = {
//		'studentnum':document.getElementById("studentnum").value,
//		'cardnum':document.getElementById("cardnum").value,
//		'college':document.getElementById("college").value,
//		'phonenum':document.getElementById("phonenum").value
//	}
//	console.log(mydata);
    $.post("./login",
    {
    	'studentnum':document.getElementById("studentnum").value,
		'cardnum':document.getElementById("cardnum").value,
		'college':document.getElementById("college").value,
		'phonenum':document.getElementById("phonenum").value
    },
        function(data,status){
        alert("数据: \n" + data + "\n状态: " + status);
    });

	req.open("POST", "./login", true);
	req.send(data);

	/*req.onreadystatechange = function(){
		if(req.readyState == 4 && req.status == 200)
			var response = JSON.parse(req.responseText);
		else
			alert("发生错误：" + req.status);
	}*/
		console.log(req.responseText);
	var response = JSON.parse(req.responseText);

	//处理JSON
	if (response.code == 200){
		window.location.href = "../select";
	}
	else{
		alert("发生错误：" + response.code + "\n" + response.text);
	}
}

function select(){
	var req = ajax();
	var timestamp = Date.parse(new Date());
	var data = "className=" + document.getElementById("courseName").innerHTML + "&selecttime=" + timestamp
	 + "&handle=" + 0;

	req.open("POST", "./select", true);
	req.send(data);

	/*req.onreadystatechange = function(){
		if(req.readyState == 4 && req.status == 200)s
			var response = JSON.parse(req.responseText);
		else
			alert("发生错误：" + req.status);
	}*/
	var response = JSON.parse(req.responseText);

	//处理JSON
	if (response.code == 200){
		var sel = document.getElementById("sel");
		var dis = document.getElementById("dis");

		sel.style.display = "none";
		dis.style.display = "block";

		alert("选课成功！");
	}
	else{
		alert("发生错误：" + response.code + "\n" + response.text);
	}


}

function dissel(){
	var req = ajax();
	var data = "className=" + document.getElementById("courseName").innerHTML + "&selecttime=" + timestamp
	 + "&handle=" + 1;

	req.open("POST", "./select", true);
	req.send(data);
	console.log(req.response)
	/*req.onreadystatechange = function(){
		if(req.readyState == 4 && req.status == 200)
			var response = JSON.parse(req.responseText);
		else
			alert("发生错误：" + req.status);
	}*/
	var response = JSON.parse(req.responseText);
	
	//处理JSON
	if (response.code == 200){
		var sel = document.getElementById("sel");
		var dis = document.getElementById("dis");

		dis.style.display = "none";
		sel.style.display = "block";

		alert("退课成功！");
	}
	else{
		alert("发生错误：" + response.code + "\n" + response.text);
	}
}
