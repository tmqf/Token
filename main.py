from website import createApp
app = createApp()

if __name__ == "__main__":
    context = ('server.crt', 'server.key')
    app.run(ssl_context=context)