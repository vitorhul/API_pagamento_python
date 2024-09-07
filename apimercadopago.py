import mercadopago
def gerar_link_pagamento():

  sdk = mercadopago.SDK("TEST-5877490592533006-090620-3134e9fd5a0129e3d251736116c8f993-1205276395")

  payment_data = {
    "items": [
      {"title":"camisa",
        "id":"1",
        "quantity":1,
        "currency_id": "BRL",
        "unit_price": 159.90
      }
    ],
      "back_urls":{
          "success": "http://127.0.0.1:5500/compracerta.html",
          "failure": "http://127.0.0.1:5500/compraerrada.html",
          "pending" : "http://127.0.0.1:5500/compraerrada.html"
      },
    "auto_return": "all"
  }

  result = sdk.preference().create(payment_data)
  payment = result["response"]
  iniciar_link_pagamento = payment["init_point"]
  print(payment)
  return  iniciar_link_pagamento
  print(payment)

  gerar_link_pagamento()