inputs = document.querySelectorAll('input')
errors = document.querySelectorAll('div.input-error')
button = document.querySelector('button')

function on_input(event) {
    element = event.target

    if (!element.validity.valid) {
        error = errors[inputs.indexOf(element)]
        error.style.display = 'block'
    }
}


for (var i = 0; i < inputs.length; i++) {

    inputs[i].oninput = on_input
}