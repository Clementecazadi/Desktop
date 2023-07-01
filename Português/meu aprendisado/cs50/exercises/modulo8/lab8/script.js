document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#free').addEventListener('submit', function(){
        let answer_in = document.querySelector('#answer_in');
        if (answer_in.value != 'lorenço')
        {
            answer_in.style.backgroundColor = 'red';
            let verificador = document.querySelector('#corrector1');
            verificador.style.visibility = 'visible';
            verificador.textContent = 'Incorreto!';
        }
        else
        {
            answer_in.style.backgroundColor = 'green';
            let verif = document.querySelector('#corrector1');
            verif.style.visibility = 'visible';
            verif.textContent = 'Correto!';
        }
    });

    let btn1 = document.querySelector('#btn1');
    let btn2 = document.querySelector('#btn2');
    let btn3 = document.querySelector('#btn3');
    btn1.addEventListener('click', function(){
        btn1.style.backgroundColor = 'red';
        btn2.style.backgroundColor = '#d9edff';
        btn3.style.backgroundColor = '#d9edff';
        let verif = document.querySelector('#corrector0');
        verif.style.visibility = 'visible';
        verif.innerText = 'Incorreto!';

    });
    btn2.addEventListener('click', function(){
        btn1.style.backgroundColor = '#d9edff';
        btn2.style.backgroundColor = 'green';
        btn3.style.backgroundColor = '#d9edff';
        let verif = document.querySelector('#corrector0');
        verif.style.visibility = 'visible';
        verif.innerText = 'Correto!';
    });
    btn3.addEventListener('click', function(){
        btn1.style.backgroundColor = '#d9edff';
        btn2.style.backgroundColor = '#d9edff';
        btn3.style.backgroundColor = 'red';
        let verif = document.querySelector('#corrector0');
        verif.style.visibility = 'visible';
        verif.innerText = 'Incorreto!';
    });
})