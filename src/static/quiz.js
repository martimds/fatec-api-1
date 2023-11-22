
  var perguntaAtual = 1;
  const form = document.querySelector("#quizForm")
  const perguntas = document.querySelectorAll(".pergunta").length

  form.addEventListener("submit", (event) => {
    event.preventDefault() // previne a página de recarregar
    const formAtual = document.forms.quizForm['resposta' + perguntaAtual] // pegar questão atual
    if (!formAtual.value) return; // caso o usuário não tenha inserido nada
    for (input of formAtual) { // pra cada alternativa da questão atual:
      if (input.parentElement.getAttribute("correct") != null) {
        input.parentElement.classList.add("certo")
      } else if (input.getAttribute("value") == formAtual.value) {
        input.parentElement.classList.add("errado") // na input que o usuário marcou
      } else {
        input.parentElement.classList.remove("errado") // remover questões erradas anteriores
      }
    }
  })

  function mudarPergunta(direcao) {
    var perguntaAtualElement = document.getElementById('pergunta' + perguntaAtual);
    perguntaAtualElement.style.display = 'none';

    perguntaAtual = Math.min(Math.max(perguntaAtual + direcao, 1), perguntas); // manter perguntaAtual entre 1 e o número de perguntas
    var novaPerguntaElement = document.getElementById('pergunta' + perguntaAtual);
    novaPerguntaElement.style.display = 'block';

    document.querySelector("#banterior").style.display = perguntaAtual == 1 && "none" || "inline-block";
    document.querySelector("#bproximo").style.display = perguntaAtual == perguntas && "none" || "inline-block";
    // document.querySelector("#bverificar").style.display = perguntaAtual == 1 && "none" || "inline-block";
  }
