let checkbox = document.getElementById('id_permanent')
let warranty_date = document.getElementById('id_warranty_expiry_date').parentNode
let warranty_description = document.getElementById('id_warranty_details').parentNode
let elements = [warranty_date, warranty_description]

checkbox.addEventListener('change', toggle)

function toggle() {
  if (checkbox.checked) {
    elements.forEach(element => element.style.display = 'block' )
  } else {
    elements.forEach(element => element.style.display = 'none' )
  }
}

toggle()
