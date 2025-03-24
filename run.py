"""
Módulo principal do aplicativo.

Este módulo cria uma instância do aplicativo Flask e executa-o em modo de depuração.

Funções:
    run: Executa o aplicativo em modo de depuração.

Notas:
    O aplicativo é criado com a função create_app, que é importada do módulo app.
    O aplicativo é executado com a função run,
    que é chamada quando o script é executado diretamente.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
