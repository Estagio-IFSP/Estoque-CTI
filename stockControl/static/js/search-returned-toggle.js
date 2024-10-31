let checkbox = document.getElementById('hide-returned-checkbox')
let returned_items = Array.from(document.getElementsByClassName('returned'))

console.log(returned_items)

checkbox.addEventListener('change', toggle)

function toggle() {
  if (checkbox.checked) {
    returned_items.forEach(element => { element.style.display = 'none' })
  } else {
    returned_items.forEach(element => element.style.display = '' )
  }
}
