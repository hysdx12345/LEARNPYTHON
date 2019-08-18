var http=require("http");

http.createServer(function (request,response) {
	// body...
	//发送HTTP头部
	// HTTP状态值：200：OK
	// 内容类型：text/plain
	response.writeHead(200,{'Content-Type':'text/plain'});

	// 发送响应数据”Hello World“
	response.end('Hello World!\n');
}).listen(8888);//使用listen绑定8888端口

//终端打印信息
console.log('Sever running at htto://127.0.0.1:8888/');

