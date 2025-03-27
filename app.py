from flask import Flask, render_template, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

# Lista de usuários para o exemplo de FOR e IF
users = [
    {"name": "Alice", "is_admin": True, "email": "alice@example.com"},
    {"name": "Bob", "is_admin": False, "email": "bob@example.com"},
    {"name": "Charlie", "is_admin": False, "email": "charlie@example.com"},
    {"name": "Diana", "is_admin": True, "email": "diana@example.com"},
    {"name": "Eve", "is_admin": False, "email": "eve@example.com"}
]

@app.route('/')
def index():
    return render_template('index.html')

# 1. Demonstração básica de template com nome de usuário (Seguro)
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user_profile.html', username=username)

# 2. Demonstração de FOR e IF em um template
@app.route('/users')
def users_list():
    return render_template('users_list.html', users=users)

# 3. Exemplo vulnerável a SSTI - via parâmetro na URL
@app.route('/vulnerable')
def vulnerable():
    name = request.args.get('name', 'Guest')
    
    # Vulnerável: constrói o template dinamicamente com entrada do usuário
    template = f'''
    {{% extends "base.html" %}}
    
    {{% block title %}}Exemplo Vulnerável{{% endblock %}}
    
    {{% block heading %}}Demonstração de SSTI - Exemplo Vulnerável{{% endblock %}}
    
    {{% block content %}}
        <div class="vulnerable-box">
            <h3>Área Vulnerável</h3>
            <p>Olá, {name}!</p>
            <p><small>Este é um exemplo vulnerável a SSTI!</small></p>
        </div>
        
        <div style="margin-top: 20px;">
            <h3>Como isso funciona?</h3>
            <p>Esta página é vulnerável porque constrói dinamicamente o template, incorporando a entrada do usuário diretamente no código do template.</p>
            
            <div class="code-block">
                # Código vulnerável - perigoso!<br>
                name = request.args.get('name', 'Guest')<br><br>
                
                # O problema está aqui, onde a entrada do usuário é incorporada diretamente no template<br>
                template = f"&lt;p&gt;Olá, {name}!&lt;/p&gt;"<br><br>
                
                return render_template_string(template)
            </div>
            
            <p>Experimente usar os seguintes payloads:</p>
            <ul>
                <li><a href="?name=Maria">?name=Maria</a> - Valor normal</li>
                <li><a href="?name=%7B%7B7*7%7D%7D">?name=&#123;&#123;7*7&#125;&#125;</a> - Tentativa de injeção</li>
                <li><a href="?name=%7B%7Bconfig%7D%7D">?name=&#123;&#123;config&#125;&#125;</a> - Tentativa de acesso a objetos</li>
            </ul>
        </div>
    {{% endblock %}}
    '''
    
    # Renderiza o template string diretamente
    return render_template_string(template)

# 4. Exemplo correto (seguro) - mesmo que o anterior, mas implementado corretamente
@app.route('/safe')
def safe():
    name = request.args.get('name', 'Guest')
    
    # Seguro: usamos um template fixo e passamos os dados como contexto
    return render_template('safe_example.html', name=name)

# 5. Exemplo de vulnerabilidade com renderização de template enviado pelo usuário
@app.route('/render_template', methods=['GET', 'POST'])
def render_user_template():
    result = ""
    user_template = request.args.get('template', '')
    
    if user_template:
        # VULNERÁVEL: permite que o usuário especifique o próprio template
        try:
            result = render_template_string(user_template, users=users)
        except Exception as e:
            result = f"Erro ao renderizar template: {str(e)}"
    
    return render_template('vulnerable.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)