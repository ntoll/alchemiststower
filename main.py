from pypercard import Card, CardApp

cards = [
    Card("hello", text="Hello"),
]

app = CardApp(stack=cards)
app.run()
