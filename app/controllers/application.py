from flask import render_template, redirect, url_for
# from app.controllers.datarecord import DataRecord  # Descomente se for usar

class Application:
    def __init__(self):
        self.pages = {
            'home.html': self.home,
            'pagina.html': self.pagina,
            'helper.html': self.helper,
            'login.html' : self.login,
            'register.html' : self.register,
            'auth.html' : self.auth,
            '404.html': self.pagina_inexistente
        }


    def render(self, page, parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)

    def helper(self):
        return render_template('helper.html')

    def pagina(self, parameter=None):
        if not parameter:
            return render_template('pagina.html', transfered=False)
        else:
            # info = self.models.work_with_parameter(parameter)  # Adapte seu model se necessário
            info = None  # Temporário - substitua pela linha acima quando adaptar DataRecord
            if not info:
                return redirect(url_for('action_pagina'))
            else:
                return render_template('pagina.html', transfered=True, data=info)

    def home(self):
        return render_template('home.html')

    def auth(self):
        return render_template('auth.html')

    def login(self):
        return render_template('login.html')

    def register(self):
        return render_template('register.html')

    def pagina_inexistente(self):
        return render_template('404.html')