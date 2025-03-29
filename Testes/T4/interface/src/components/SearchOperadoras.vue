<template>
  <div class="app-container">
    <!-- Criação de um header simples com a logo da IntuitiveCare que ficará centralizada -->
    <header class="header">
      <img src="@/assets/logo.png" alt="Logo da Empresa" class="logo" />
    </header>

    <!-- Container principal aonde ficará o input de busca além do checamento de erros -->
    <main class="container">
      <h2>Buscar Operadoras</h2>
      <div class="search-box">
        <input v-model="query" placeholder="Digite o CNPJ, Nome Fantasia ou Razão Social..." />
        <button @click="search">Buscar</button>
      </div>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Carregando...</p>
      </div>

      <div v-if="error" class="error">{{ error }}</div>

      <ul v-if="results.length" class="results-list">
        <li v-for="(item, index) in results" :key="index" class="result-item">
          <strong>{{ item.nome_fantasia || item.razao_social }}</strong> - {{ item.cnpj }}
        </li>
      </ul>

      <div v-if="results.length === 0 && query && !loading" class="no-results">
        Nenhum resultado encontrado.
      </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; {{ new Date().getFullYear() }} IntuitiveCare. Todos os direitos reservados.</p>
    </footer>
  </div>
</template>

<script>
// Importando o axios para realizar as requisições HTTP
import axios from "axios";


export default {
  data() {
    return {
      query: "",
      results: [],
      loading: false,
      error: null
    };
  },
  methods: {
    async search() {
      // Validando se o campo de busca não está vazio e se possui pelo menos 2 caracteres
      if (this.query.length < 2) {
        this.error = "Digite pelo menos 2 caracteres.";
        return;
      }

      this.loading = true;
      this.error = null;
      this.results = [];

      try {
        // Realizando a requisição para a API de busca
        const response = await axios.get(`http://127.0.0.1:8000/search`, {
          params: { query: this.query }
        });
        this.results = response.data;
      } catch (err) {
        this.error = "Erro ao buscar dados.";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
/* Layout principal */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #f5f5f5;
}

/* Header estilizado */
.header {
  background: #c9c4c4;
  padding: 15px;
  text-align: center;
}

.logo {
  max-width: 180px;
  height: auto;
}

/* Container principal */
.container {
  flex: 1;
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  text-align: center;
  background: #ffffff;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  font-family: 'Poppins', sans-serif;
}

/* Título */
h2 {
  margin-bottom: 20px;
  color: #333;
}

/* Estilização do campo de busca */
.search-box {
  display: flex;
  gap: 10px;
  justify-content: center;
}

/* Estilização do input */
input {
  width: 350px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

/* Estilização do input quando estiver em foco (clicado) */
input:focus {
  border-color: #007bff;
  outline: none;
}

/* Botão de busca */
button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
  font-family: 'Poppins', sans-serif;
}

/* O botão terá um leve efeito de mudança suave de cor quando o cursor do mouse estiver encima dele */
button:hover {
  background-color: #0056b3;
}

/* Estilização da lista de resultados */
.results-list {
  list-style: none;
  padding: 0;
  margin-top: 20px;
}

/* Estilização do item de resultado */
.result-item {
  background: #f8f9fa;
  margin: 5px 0;
  padding: 10px;
  border-radius: 6px;
  font-size: 16px;
  transition: background 0.3s;
}

.result-item:hover {
  background: #e9ecef;
}

/* Mensagem de erro */
.error {
  color: #d9534f;
  margin-top: 10px;
  font-weight: bold;
}

/* Mensagem de nenhum resultado */
.no-results {
  color: #6c757d;
  font-style: italic;
  margin-top: 10px;
}

/* Loading spinner */
.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin-top: 20px;
}

/* Animação do loading spinner */
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid #007bff;
  border-top: 3px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 5px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Footer estilizado */
.footer {
  background: #000000;
  color: white;
  text-align: center;
  padding: 15px;
  font-size: 14px;
  margin-top: auto;
  font-family: 'Poppins', sans-serif;
}
</style>
