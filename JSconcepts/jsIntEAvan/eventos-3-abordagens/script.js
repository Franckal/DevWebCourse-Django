function executar(){
    console.log("Clique botao")
    //botao.removeEventListener('click', executar)
}

function executar2(){
    console.log("Clique body")
}

//const botao = document.getElementById('botao')
const botao = document.querySelector('[botao-acao]')
//const body = document.querySelector('body')
//botao.onclick = executar
botao.addEventListener('click', executar)
//body.addEventListener('click', executar2)

if( botao.addEventListener ){
    botao.addEventListener('click', executar)
}else{
    botao.attachEvent('click', executar)
}