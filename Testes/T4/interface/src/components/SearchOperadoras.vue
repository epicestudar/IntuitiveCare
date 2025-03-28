<template>
  <div class="container">
    <h2>Buscar Operadoras</h2>
    <input v-model="query" placeholder="Digite o CNPJ, Nome Fantasia ou Razão Social..." />
    <button @click="search">Buscar</button>

    <div v-if="loading">Carregando...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <ul v-if="results.length">
      <li v-for="(item, index) in results" :key="index">
        <strong>{{ item.nome_fantasia || item.razao_social }}</strong> - {{ item.cnpj }}
      </li>
    </ul>

    <div v-if="results.length === 0 && query">Nenhum resultado encontrado.</div>
  </div>
</template>

<script>
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
      if (this.query.length < 2) {
        this.error = "Digite pelo menos 2 caracteres.";
        return;
      }

      this.loading = true;
      this.error = null;
      this.results = [];

      try {
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
.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  text-align: center;
}
input {
  width: 80%;
  padding: 8px;
  margin: 10px 0;
}
button {
  padding: 8px 15px;
  cursor: pointer;
}
.error {
  color: red;
}
</style>
