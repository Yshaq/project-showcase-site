inputs = document.querySelectorAll('div.form__field input')
console.log(inputs)
for (let f of inputs) {
    f.classList.add("input");
}
document.querySelector('textarea').classList.add("input")