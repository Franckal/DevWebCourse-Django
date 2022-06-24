/* $(document).ready(function(){
    $('[acao-clique]').on('click', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
}) 

$(function(){
    $('[acao-clique]').on('click', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
}) 


$(window).on('load',function(){
    console.log('load')
})

$(window).on('unload',function(){
    console.log('unload')
})

$(window).on('error', function(){
    console.log('error')
})

$(window).on('resize', function(){
    console.log('resize')
})

$(window).on('scroll', function(){
    console.log('scroll')
})

$(function(){
    $('[acao-clique]').on('dblclick', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
})

$(function(){
    $('[acao-clique]').on('mouseup', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
})


$(function(){
    $('[acao-clique]').on('mousedown', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
})

$(function(){
    $('[acao-clique]').on('mousehover', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
})

$(function(){
    $('[acao-clique]').on('mousemove', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
})

$(function(){
    $('[acao-clique]').on('mouseout', function(){
        $('h1').addClass('destaque')
        console.log('clique')
    })
})

function mouseenter(){
    console.log('mouseenter')
}

function mouseleave(){
    console.log('mouseleave')
}

$(function(){
    $('[acao-clique]').hover(mouseenter, mouseleave)
})*/


/******************************************************/
/******************************************************/
/*
$(function(){
    $('[name=entrada]').on('blur', function(){
        //focus, blur
        //console.log('focus')
        console.log('blur')
    })
})


$(function(){
    $('[name=entrada]').on('change', function(){
        console.log('change')
    })
})

$(function(){
    $('[name=entrada]').on('select', function(){
        //copy, paste, cut, select
        console.log('select')
    })
})

$(function(){
    $('[name=selecao]').on('focus', function(){
        //change, focus, blur
        console.log('focus')

    })
})

$(function(){
    $('[name=idade]').on('focus', function(){
        //change, focus, blur
        console.log('focus')

    })
})

$(function(){
    $('[name=termo]').on('focus', function(){
        //change, focus, blur
        console.log('focus')

    })
})

$(function(){
    $('body').on('submit', function(e){
        
        //e.preventDefault()
        console.log('submit')
        
    })
})

$(function(){
    $('[name=entrada]').on('keydown', function(e){
       //input, keydown, keyup, keypress
        console.log('keypress: ' + e.key)
    })
})

$(function(){
    $('body').on('keydown', function(e){
       //input, keydown, keyup, keypress
        console.log('keypress: ' + e.key)
    })
})

$(function(){
    $('[name=enviar]').on('click', function(e){
        e.preventDefault()
        let nome = $('[name=entrada]').val()
        let selecao = $('[name=selecao]').val()
        let idade = $('[name=idade]:checked').val()
        let termo = $('[name=termo]:checked').val()
        console.log(`nome: ${nome}, sexo: ${selecao}, idade: ${idade}, termo: ${termo}`)
    })
})


$(function(){
    $('[acao-clique]').on('click', function(){
        let duracao = 1000
        $('#animacao').hide(duracao, function(){
            console.log('animacao finalizou')
        }) 

        //$('#animacao').show(duracao)
        //$('#animacao').toggle(duracao)
        //$('#animacao').fadeIn(duracao)
        //$('p').fadeOut(duracao)
        //$('p').fadeTo(duracao, 0.5)
        //$('#animacao').fadeToggle(duracao)
        //$('#animacao').slideDown(duracao)
        //$('p').slideUp(duracao)
        //$('p').slideToggle(duracao)
    })
})*/

function callback(){
    console.log("Animacao terminou")
}

$(function(){

    $('[acao-direita]').on('click', function(){
        $('#conteudo').animate(
            {
                left: "+=40",
                right: "-=40"
            }
        )
    })

    $('[acao-esquerda]').on('click', function(){
        $('#conteudo').animate(
            {
                right: "+=40",
                left: "-=40"
            }
        )
    }) 

    let val = $('body').on('keydown', function(e){
        let codigo = e.keyCode
        if(codigo==39){
            $('#conteudo').animate(
                {
                    left: "+=40",
                    right: "-=40"
                }
            )
        }
        else if(codigo==37){
            $('#conteudo').animate(
                {
                    right: "+=40",
                    left: "-=40"
                }
            )
        }
        
    })

    $('#conteudo').on('click', function(){
        $('#conteudo').animate(
            //{width: 600},
            //{width:'100%'},
            {
                right: 20,
                bottom: 20,
                padding: "+=50", // "-=30"
                opacity: 0.2
            },
            1000,
            callback
        )
    })
})


