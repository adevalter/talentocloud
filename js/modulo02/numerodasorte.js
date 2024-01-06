numerosDaSorte = [37, 14, 26, 5, 94, 87]

let resultado = 0;

for (let i = 0; i < numerosDaSorte.length; i++) {

    resultado = numerosDaSorte[i] % 2;

    if (resultado == 0 && numerosDaSorte[i] < 50) {
        console.log(numerosDaSorte[i] + " é par e menor que 50");
    } else if (numerosDaSorte[i] < 50) {
        console.log(numerosDaSorte[i] + " é  menor que 50");
    } else if (numerosDaSorte[i] > 50) {
        console.log(numerosDaSorte[i] + " é  maior que 50");
    }

    // console.log(numerosDaSorte[i]);

}