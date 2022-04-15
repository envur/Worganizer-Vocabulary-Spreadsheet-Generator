def html_message(message_type, url, username, token):
    if message_type == "reset":
        message_html = f"""\
            <html>
                <head></head>
                <body>
                    <div>
                    <div style="margin: 5em;">
                        <div style="color: #fff">
                            <h1 style="color: #111">Hey, {username}!</h1>
                            <h3 style="color: #111;">We received your password reset request!</h3>
                                <h4 style="color: #111;">Click on the link below to proceed:</h4>
                                <a href="{url}forgot/password?token={token}">Link to new password</a><br>
                                If you didn't asked to reset your password, disregard this email.
                        </div>
                    </div>
                </body>
            </html>"""
        return message_html
