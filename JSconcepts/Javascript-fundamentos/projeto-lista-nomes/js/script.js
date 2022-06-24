let nomes = [
    "jamilton",
    "josé",
    "leticia",
    "maria",
    "carlos",
    "pedro",
    "marcela",
    "carla",
    "carlos"
]

function pesquisarNome(){
    
    let nomePesquisa = document.getElementById('campoNome').value
    let itensLista = ''
    for(indice in nomes){
        let nome = nomes[indice]
        if(nomePesquisa == nome){
            itensLista += `
            <li class="list-group-item">
                ${nome}
            </li>`
        }
    }
    document.getElementById('lista').innerHTML = itensLista
}

function carregarNomes(){
    let itensLista = ''
    for(indice in nomes){
        let nome = nomes[indice]
        itensLista += `
        <li class="list-group-item">
            ${nome}
        </li>`
    
    }
   
    document.getElementById('lista').innerHTML = itensLista
}