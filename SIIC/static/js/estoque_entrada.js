//BLOCO FUNCIONAL
//Botões para adicionar mais iten
{ % comment % }
$(document).ready(function() {
    //insere classe no primeiro item
    $('#id_estoque-0-produto').addClass('clProduto');
    $('#id_estoque-0-quantidade').addClass('clQuantidade');

    $('#add-item').click(function(ev) {
        ev.preventDefault();
        var count = $('#estoque').children().length;
        var tmplMarkup = $('#item-estoque').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#estoque').append(compiledTmpl);
        // atualização da contagem
        $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

        //animação do scroll
        $('html, body').animate({
            scrollTop: $('#add-item').position().top - 200
        }, 800);

        //Adicionando valores
        $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
        $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');

    });
});

let estoque
let saldo
let campo
let quantidade

$(document).on('change', '.clProduto', function() {
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'

    $.ajax({
        url: url,
        type: 'GET',
        success: function(response) {
            estoque = response.data[0].estoque
            campo = self.attr('id').replace('produto', 'quantidade')
            estoque_inicial = self.attr('id').replace('produto', 'inicial')
                // Estoque inicial
            $('#' + estoque_inicial).val(estoque)
                // Remove o valor do campo 'quantidade'
            $('#' + campo).val('')
        },
        error: function(xhr) {
            // body...
        }
    })
});

$(document).on('change', '.clQuantidade', function() {
    quantidade = $(this).val();
    // Aqui é feito o cálculo de soma do estoque
    saldo = Number(quantidade) + Number(estoque);
    campo = $(this).attr('id').replace('quantidade', 'saldo')
    campo_estoque_inicial = $(this).attr('id').replace('quantidade', 'inicial')
    estoque_inicial = $('#' + campo_estoque_inicial).val()
    saldo = Number(quantidade) + Number(estoque_inicial)
    $('#' + campo).val(saldo)
    campo2 = $(this).attr('id').replace('quantidade', 'saldo-span')
        // Atrubui o saldo ao campo 'id_estoque-x-saldo-span'
    $('#' + campo2).text(saldo)
}); { % endcomment % }

// Link JS externo
//<script src="{% static 'js/estoque_entrada.js' %}"></script>