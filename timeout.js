console.log("here we go");
const timeO=new Promise(resolve=>{
	setTimeout(()=>{
		resolve('hello ');
	},2000);
}).then(value=>{
	console.log(value+'world');
});



 
