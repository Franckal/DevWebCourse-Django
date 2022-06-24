function executar(){
	console.log("Clique no botao")
	//botao.removeEventListener('click', executar )
}

function executar2(){
	console.log("Clique Body")
}

/* 2) Rotinas DOM tradicionais */
//const botao = document.getElementById('botao')
//const botao = document.querySelector('[botao-acao]')
//botao.onclick = executar
//botao.onclick = function(){executar()}


const botao = document.querySelector('[botao-acao]')
//const body = document.querySelector('body')

/* 3) Rotinas de eventos DOM */
//body.addEventListener('click', executar2 )

if( botao.addEventListener ){
	botao.addEventListener('click', executar )
}else{
	botao.attachEvent('click', executar )
}







