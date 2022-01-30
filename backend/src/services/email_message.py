def html_message(message_type, url, username, token):
    if message_type == "reset":
        message_html = f"""\
            <html>
                <head></head>
                <body>
                    <div>
                    <div style="margin: 5em;">
                        <div style="color: #fff">
                            <h1 style="color: #111">Olá, {username}!</h1>
                            <h3 style="color: #111;">Recebemos seu pedido de redefinição de senha!</h3>
                                <h4 style="color: #111;">Clique no link abaixo para prosseguir:</h4>
                                <a href="{url}forgot/password?token={token}">Link para nova senha</a><br>
                                Caso não tenha sido você quem pediu, desconsidere esse e-mail.
                        </div>
                    </div>
                </body>
            </html>"""
        return message_html
