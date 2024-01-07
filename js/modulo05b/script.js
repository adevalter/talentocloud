const produtosVenda = document.createElement("div")
produtosVenda.innerHTML = `
  <h2 id="nome-produto">Headset Gamer HyperX Cloud II Sem Fio Som Surround 7.1</h2>
                <p class="descricao">O HyperX Cloud foi criado para ser um headset gamer ultraconfortável com um som espetacular. Pensamos muito nos detalhes, como nossa espuma memory foam exclusiva HyperX, o material sintético premium, a força de aperto do arco da cabeça reduzida e o peso equilibrado para criar um headset que fosse confortável para longas sessões de jogo. Não é de se admirar que ele tenha se tornado o headset preferido de milhões de gamers. Queira você se concentrar na competição ou relaxar com alguns dos seus jogos favoritos, há sempre um Cloud perfeito para você.</p>
                <h2 class="preco">R$ 1.099,99</h2>
`
const produtosNovos = document.querySelector(".produtos");
produtosNovos.appendChild(produtosVenda)