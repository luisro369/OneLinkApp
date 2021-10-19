//Funcion destinada a hacer desaparecer los mensajes de 'success' y 'error'

var message = document.getElementById('mensaje');
console.log(message);

setTimeout(function(){
    console.log(message.length)
    if(message.innerHTML.length > 0){
	message.remove();
    }//if
    else{
	console.log("Problemas detectando el mensaje");
    }
},3000);//desaparecer despues de 5 segundos

