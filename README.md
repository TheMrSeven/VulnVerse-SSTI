# Demonstração de Server-Side Template Injection (SSTI)

Este projeto é uma demonstração educacional de vulnerabilidades SSTI (Server-Side Template Injection) em aplicações Flask que utilizam Jinja2 como engine de template.

> **AVISO**: Este aplicativo contém vulnerabilidades intencionais para fins educacionais. NÃO utilize este código em ambientes de produção ou em servidores públicos.

## Sobre o projeto

Este aplicativo demonstra diferentes aspectos do SSTI:

1. **Uso seguro de templates** - Demonstração de como utilizar templates de forma segura
2. **Exemplos de FOR/IF** - Demonstração de loops e condicionais em templates
3. **Vulnerabilidade SSTI** - Uma rota vulnerável que pode ser explorada
4. **Implementação segura** - A versão correta da rota vulnerável
5. **Template customizado** - Uma rota extremamente vulnerável que permite renderizar templates fornecidos pelo usuário

## Requisitos

- Python 3.7+
- Flask
- Jinja2

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/TheMrSeven/VulnVerse-SSTI.git
   cd VulnVerse-SSTI
   ```

2. Crie um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute o aplicativo:
   ```
   python app.py
   ```

5. Acesse [http://localhost:5000](http://localhost:5000) no seu navegador.

## Uso educacional