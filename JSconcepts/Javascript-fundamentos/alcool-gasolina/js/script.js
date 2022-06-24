function calcularMelhorPreco() {
    // validar campos
    let precoAlcool = document.getElementById('alcool').value
    let precoGasolina = document.getElementById('gasolina').value

    if (precoAlcool != '') {
        if (precoGasolina != '') {
            let resultado = precoAlcool / precoGasolina
            if (resultado >= 0.7) {
                //alert("É melhor utilizar Alcool")
                document.getElementById('resultado').innerHTML = "Melhor utilizar Gasolina!"
            } else {
                //alert("É melhor utilizar Gasolina")
                document.getElementById('resultado').innerHTML = "É melhor utilizar Alcool"
            }
        } else {
            alert("Digite o preço da gasolina!")
        }
    } else {
        alert("Digite o preço do alcool!")
    }
}