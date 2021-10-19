//Funcion destinada a hacer desaparecer los mensajes de 'success' y 'error'

var message = document.getElementById('msg');
console.log(message);

setTimeout(function(){
    if(message.length > 0){
	console.log("entroooooooo");
	message.remove();
    }//if
    else{
	console.log("entro al else");
    }
},5000);//desaparecer despues de 5 segundos

