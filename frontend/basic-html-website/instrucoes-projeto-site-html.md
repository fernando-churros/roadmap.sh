# Projeto: Site Básico em HTML

## Objetivo

Criar um site simples utilizando **apenas HTML**, composto por várias
páginas.

O objetivo principal é praticar a estruturação semântica de um site e
prepará-lo para receber estilos CSS posteriormente.

## Páginas obrigatórias

O site deve possuir as seguintes páginas:

-   **Página inicial (Home)**
-   **Projetos (Projects)**
-   **Artigos (Articles)**
-   **Contato (Contact)**

## Navegação

Todas as páginas devem possuir uma **barra de navegação**.

A navegação deve:

-   Estar presente em todas as páginas.
-   Conter links para todas as páginas do site.
-   Permitir navegar entre as páginas sem depender do botão "voltar" do
    navegador.

Exemplo de estrutura de navegação:

``` html
<nav>
    <ul>
        <li><a href="index.html">Início</a></li>
        <li><a href="projects.html">Projetos</a></li>
        <li><a href="articles.html">Artigos</a></li>
        <li><a href="contact.html">Contato</a></li>
    </ul>
</nav>
```

## Requisitos

### 1. HTML semântico

Utilize elementos HTML de acordo com sua finalidade semântica.

Dê preferência a elementos como:

-   `<header>`
-   `<nav>`
-   `<main>`
-   `<section>`
-   `<article>`
-   `<footer>`
-   `<h1>` até `<h6>`
-   `<form>`
-   `<label>`

Evite utilizar `<div>` para representar elementos que possuem uma
finalidade semântica específica.

### 2. Múltiplas páginas

Crie arquivos HTML separados para cada página.

Uma possível organização é:

``` text
projeto/
├── index.html
├── projects.html
├── articles.html
└── contact.html
```

Todas as páginas devem possuir uma estrutura HTML válida e a mesma barra
de navegação.

### 3. Estrutura preparada para CSS

Neste projeto **não é necessário utilizar CSS**.

Entretanto, a estrutura HTML deve ser organizada de forma que seja fácil
adicionar estilos posteriormente.

Organize o conteúdo utilizando elementos semânticos e uma hierarquia
clara.

### 4. SEO básico

Cada página deve possuir metatags básicas de SEO dentro do `<head>`.

Inclua, no mínimo:

``` html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Descrição da página">
```

Também defina um título adequado para cada página:

``` html
<title>Título da página</title>
```

A descrição e o título devem ser relevantes ao conteúdo específico de
cada página.

### 5. Página de contato

A página de contato deve conter um formulário HTML.

O formulário deve possuir campos como:

-   Nome
-   E-mail
-   Mensagem

Utilize `<label>` associado corretamente aos respectivos campos.

Exemplo de estrutura:

``` html
<form>
    <label for="name">Nome:</label>
    <input type="text" id="name" name="name">

    <label for="email">E-mail:</label>
    <input type="email" id="email" name="email">

    <label for="message">Mensagem:</label>
    <textarea id="message" name="message"></textarea>

    <button type="submit">Enviar</button>
</form>
```

Não é necessário implementar o envio dos dados. O objetivo é apenas
construir a estrutura do formulário.

## Referência visual

Você pode utilizar o seguinte mockup como referência para organizar a
estrutura das páginas:

https://assets.roadmap.sh/guest/portfolio-design-83lku.png

A referência serve apenas para orientar a organização do conteúdo.

**Não é necessário reproduzir o visual**, pois este projeto é
exclusivamente sobre HTML.

## Checklist de entrega

Antes de considerar o projeto concluído, verifique:

-   [ ] Existem 4 páginas HTML.
-   [ ] A página inicial existe como `index.html`.
-   [ ] Existem páginas para Projetos, Artigos e Contato.
-   [ ] Todas as páginas possuem uma barra de navegação.
-   [ ] A navegação possui links para todas as páginas.
-   [ ] A estrutura utiliza HTML semântico.
-   [ ] Cada página possui `<title>` adequado.
-   [ ] Cada página possui `charset`.
-   [ ] Cada página possui `viewport`.
-   [ ] Cada página possui uma meta description.
-   [ ] A página de contato possui um formulário.
-   [ ] O formulário possui campo para nome.
-   [ ] O formulário possui campo para e-mail.
-   [ ] O formulário possui campo para mensagem.
-   [ ] Os campos possuem `<label>` associados corretamente.
-   [ ] Não foi utilizado CSS.
-   [ ] A estrutura está organizada para facilitar a adição de CSS
    posteriormente.

## Resultado esperado

Ao finalizar, você deverá ter um site HTML simples com quatro páginas
interligadas, estrutura semântica, informações básicas de SEO e um
formulário de contato.

O foco deste projeto é compreender:

-   Como criar múltiplas páginas HTML.
-   Como conectar páginas utilizando links.
-   Como estruturar uma página semanticamente.
-   Como utilizar elementos HTML apropriados para cada tipo de conteúdo.
-   Como criar formulários.
-   Como adicionar metatags básicas de SEO.
-   Como organizar HTML pensando na futura implementação de CSS.

Após concluir este projeto, o próximo passo será adicionar **CSS** para
estilizar a estrutura criada.
