# explaining kung para saan yung ating code
from pyscript import display, document


def ordering_form(e):
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    name = document.getElementById('name').value
    add = document.getElementById('address').value
    num = document.getElementById('contact').value

    total = (float(item1.value) * item1.checked + 
             float(item2.value) * item2.checked + 
             float(item3.value) * item3.checked)

    display(f'Order for: {name}', target='output')
    display(f'Address: {add}', target='output')
    display(f'Contact number: {num}', target='output')
    display(f'Total amount: ₱ {total}', target='output')