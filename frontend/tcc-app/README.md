# 🤖 TCC Chatbot App

Aplicativo desenvolvido em **React Native + Expo** para o TCC, com foco em chat com IA como funcionalidade principal e área administrativa para gerenciamento.

O projeto utiliza:

- **React Native** e **Expo**
- **React Navigation (Drawer)** para navegação
- **React Native Paper** para componentes prontos e consistentes
- **NativeWind (Tailwind para React Native)** para estilização rápida
- **WebView** para integrar páginas externas
- **Axios** para comunicação com APIs
- **JWT Decode** para autenticação de usuários

---

## 📂 Estrutura do Projeto

```
/src
  /navigation
    RootNavigation.tsx
    DrawerNavigation.tsx
  /screens
    ChatScreen.tsx       # Tela principal do chat
    LoginScreen.tsx      # Tela de login
    HomeScreen.tsx       # Tela inicial
    WebViewScreen.tsx    # Tela com WebView para sites
    AdminScreen.tsx      # Tela de configurações do admin
  /components
  /services
  /context
  /styles
    global.css           # Estilos globais para NativeWind
  /assets
```

---

## 🚀 Tecnologias e Bibliotecas

- **React Native** – Desenvolvimento mobile multiplataforma
- **Expo** – Simplifica a construção e testes do app
- **React Navigation (Drawer)** – Navegação com menu lateral
- **React Native Paper** – Componentes prontos (botões, inputs, cards)
- **NativeWind** – Tailwind CSS para React Native
- **react-native-webview** – Para renderizar páginas web dentro do app
- **Axios** – Chamadas HTTP
- **JWT Decode** – Decodificar tokens JWT para autenticação

---

## 💻 Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/VagnerGGJ/tcc-cc
cd tcc-chatbot-app
```

2. Instale as dependências:

```bash
npm install
```

> Certifique-se de que está usando **Node 20+** e **npm 9+** ou **yarn 3+**.

3. Inicie o Expo:

```bash
npx expo start
```

4. Abra o app no seu dispositivo ou emulador:

- **Android:** pressione `a`
- **iOS:** pressione `i`
- **Web:** pressione `w`

---

## 📌 Observações

- A navegação principal é feita via **Drawer Navigation**.
- **NativeWind** foi usado para facilitar estilização com classes Tailwind.
- **React Native Paper** garante consistência visual e componentes interativos de forma rápida.
- **WebViewScreen** permite abrir links externos dentro do app.

---

## 🔧 Scripts úteis

- `npm start` → Inicia o projeto no Expo
- `npm run android` → Abre o app no Android
- `npm run ios` → Abre o app no iOS
- `npm run web` → Abre o app no navegador

---

## 📝 Próximos passos

- Implementar integração do **chat com IA**
- Criar tela de **Admin** com configuração de usuários e permissões
- Refatorar componentes do chat para melhor performance e UI
- Adicionar testes unitários e de integração

