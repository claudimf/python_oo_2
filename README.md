# Orientação a Objetos com Python

👋 Olá, Seja Bem-vindo(a) ao 'Orientação a Objetos com Python'.

# Projeto 'Orientação a Objetos com Python' do curso:

## [Python 3: Avançando na orientação a objetos](https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos)

### Aulas

<details>
    <summary>Relembrando classes e objetos Ver primeiro vídeo</summary>
    <ul>
        <li>Introdução</li>
        <li>Relembrando classes e objetos</li>
        <li>Com e sem inicializador</li>
        <li>Adicionando atributos e métodos</li>
        <li>Titularizando nomes</li>
        <li>Encapsulando comportamento</li>
        <li>Vantagens do property</li>
        <li>Para saber mais: Atributos de classe</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Removendo duplicação com herança</summary>
    <ul>
        <li>Arquivo da aula anterior</li>
        <li>Removendo duplicação</li>
        <li>Sobre Herança</li>
        <li>Reutilizando ainda mais</li>
        <li>Vantagens de herança</li>
        <li>Explicando a herança</li>
        <li>Estendendo a superclasse</li>
        <li>Para saber mais: Métodos estáticos e de classe</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Reduzindo ifs com polimorfismo</summary>
    <ul>
        <li>Arquivo da aula anterior</li>
        <li>Polimorfismo</li>
        <li>Polimorfismo</li>
        <li>Reduzindo ifs</li>
        <li>Identificando o polimorfismo</li>
        <li>Representação textual de objetos</li>
        <li>Representação string</li>
        <li>Para saber mais: Outra forma de representação</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Quando não usar herança</summary>
    <ul>
        <li>Arquivo da aula anterior</li>
        <li>Criando a playlist</li>
        <li>Herdando list</li>
        <li>Reaproveitando um list</li>
        <li>Por que herdar um list?</li>
        <li>Fugindo da complexidade</li>
        <li>Desvantagens na herança</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Duck Typing e um modelo de dados</summary>
    <ul>
        <li>Arquivo da aula anterior</li>
        <li>Se anda como um pato...</li>
        <li>Atributos protegidos</li>
        <li>Vantagens de iterável</li>
        <li>Modelo de dados Python</li>
        <li>Quando não usar herança</li>
        <li>Composição x Extensão</li>
        <li>Analisando Duck Typing</li>
        <li>Classes abstratas ou ABCs</li>
        <li>Garantias das ABCs</li>
        <li>Para saber mais: Criando ABC</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Herança múltipla</summary>
    <ul>
        <li>Arquivo da aula anterior</li>
        <li>Mais de uma classe mãe</li>
        <li>Herança múltipla, pra quê?</li>
        <li>Resolução de métodos</li>
        <li>Mixins</li>
        <li>Sobre herança múltipla</li>
        <li>Mãos na massa</li>
        <li>O que aprendemos?</li>
        <li>Conclusão</li>
        <li>Arquivo completo do curso</li>
    </ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)